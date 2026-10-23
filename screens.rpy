################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

init python:
    ## Named dialogue-box layouts. "1" is the furthest-left position, "2" is the
    ## split-the-difference nudge-back, "3" is a little further right still —
    ## used when a character's current sprite/costume pose reaches further into
    ## the text area than the default.
    DIALOGUE_POSITIONS = {
        1: {"name_xpos": 175, "dialogue_xpos": 185, "dialogue_width": 1333},
        2: {"name_xpos": 193, "dialogue_xpos": 203, "dialogue_width": 1315},
        3: {"name_xpos": 223, "dialogue_xpos": 233, "dialogue_width": 1315},
        "mc": {"name_xpos": 166, "dialogue_xpos": 176, "dialogue_width": 1333},
    }

    def dialogue_position(who):
        if who == store.player_character:
            return "mc"
        if who == "Pudding the Pig" and store.pig_costume in ("piggy_icon", "stars_stripes"):
            return 2
        if who == "Daisy the Goat" and store.goat_costume in ("g_o_a_t", "high_noon"):
            return 2
        if who == "Annabelle the Cow" and store.cow_costume == "macabre_bovine":
            return 3
        if who == "Annabelle the Cow":
            return 2
        if who == "Penny the Mouse":
            return 2
        return 1

screen say(who, what):

    $ _dialogue_pos = DIALOGUE_POSITIONS[dialogue_position(who)]

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                xpos _dialogue_pos["name_xpos"]
                text who id "who"

        text what id "what":
            xpos _dialogue_pos["dialogue_xpos"]
            xsize _dialogue_pos["dialogue_width"]


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() at tutorial_portrait xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width

################################### SPLASH SCREENS ################################################################################

screen splash_adult_warning():
    add "images/Backgrounds/UI/Splash_1.png"

screen splash_character_age():
    add "images/Backgrounds/UI/Splash_2.png"

################################### MAPS ################################################################################
############# MAPS ###############################################################

screen Fields_map:
    on "show" action SetVariable("current_map", "Fields_map")
    on "hide" action [SetVariable("default_mouse", "default"), SetVariable("active_tool", None), Function(flush_harvest_flyers)]  # <-- new
    add "images/Backgrounds/Farm/Grass_1_blur.jpg"

    # Inventory row
    frame:
        xpos (472 - 4 - 2)
        ypos (20 - 4 - 2)
        xsize (741 + 8 + 4)
        ysize (83 + 8 + 4)
        background "#000000ff"

    frame:
        xpos (472 - 4)
        ypos (20 - 4)
        xsize (741 + 8)
        ysize (83 + 8)
        background Frame("images/Textures/gold1.jpg", 0, 0)

    frame:
        xpos 472
        ypos 20
        xsize 741
        ysize 83
        padding (16, 10)
        background Frame("images/Textures/bwood3.jpg", 0, 0)

        hbox:
            spacing 16

            for crop in ["apple", "carrot", "wheat", "corn", "pumpkin"]:
                hbox:
                    spacing 6
                    add f"images/Maps/Fields/{crop}_item.png":
                        xsize 63
                        ysize 63
                        at (counter_pulse_transform if counter_pulse[crop] else Transform())
                    frame:
                        xsize 60
                        yalign 0.5
                        background None
                        text str(player_inventory[crop]) color "#ffffff" yalign 0.5
                    if counter_pulse[crop]:
                        timer 0.3 action Function(reset_counter_pulse, crop)

    # Farm grid
    grid 10 3:
        xalign 0.2
        yalign 0.4
        spacing 8

        for i in range(30):
            fixed:
                xsize 128
                ysize 256

                imagebutton:
                    yalign 1.0
                    idle get_plot_image(i)
                    hover get_plot_hover(i)
                    sensitive tutorial_plot_sensitive(i)
                    action [Function(use_tool, i), Function(tutorial_check_plot, i)]

                if get_plant_image(i):
                    add get_plant_image(i) xalign 0.5 yalign 1.0

    # Harvest flyers - animate from the harvested plot to that crop's counter
    for flyer in harvest_flyers:
        $ fx, fy = flyer_position(flyer)
        add f"images/Maps/Fields/{flyer['crop']}_item.png":
            xsize 40
            ysize 40
            xanchor 0.5
            yanchor 0.5
            xpos fx
            ypos fy

    if harvest_flyers:
        timer 0.03 repeat True action Function(tick_flyers)

    # Tool panel
    # Tool panel
    frame:
        xalign 0.95
        yalign 0.5
        xsize 160
        background "images/Maps/Fields/Toolmat.png"

        vbox:
            xalign 0.5
            spacing 16

            text "Tools" xalign 0.5 color "#ffffff"

            imagebutton:
                idle "images/Maps/Fields/seedbag_idle.png"
                hover "images/Maps/Fields/seedbag_hover.png"
                selected_idle "images/Maps/Fields/seedbag_hover.png"
                selected (active_tool == "seeds")
                sensitive tutorial_target("fields_pick_tool")
                action [Function(renpy.sound.play, audio.click_1), If(active_tool == "seeds",
                    true=[SetVariable("active_tool", None), SetVariable("default_mouse", "default")],
                    false=[SetVariable("active_tool", "seeds"), Function(tutorial_advance_if, "fields_pick_tool", "fields_pick_seed")])]      # <-- cursor NOT set here anymore

            if player_inventory["sprinkler"] > 0:
                imagebutton:
                    idle "images/Maps/Fields/sprinkler_idle.png"
                    hover "images/Maps/Fields/sprinkler_hover.png"
                    action Function(use_sprinkler)
            else:
                imagebutton:
                    idle "images/Maps/Fields/wateringcan_idle.png"
                    hover "images/Maps/Fields/wateringcan_hover.png"
                    selected_idle "images/Maps/Fields/wateringcan_hover.png"
                    selected (active_tool == "water")
                    sensitive tutorial_target("fields_pick_water")
                    action [Function(renpy.sound.play, audio.click_1), If(active_tool == "water",
                        true=[SetVariable("active_tool", None), SetVariable("default_mouse", "default")],
                        false=[SetVariable("active_tool", "water"), SetVariable("default_mouse", "water"), Function(tutorial_advance_if, "fields_pick_water", "fields_water_plot")])]

            if show_water_anim:
                timer 0.1 action [SetVariable("show_water_anim", False), SetVariable("default_mouse", "water")]

            if player_inventory["tractor"] > 0:
                imagebutton:
                    idle "images/Maps/Fields/tractor_idle.png"
                    hover "images/Maps/Fields/tractor_hover.png"
                    action Function(use_tractor)
            else:
                imagebutton:
                    idle "images/Maps/Fields/scythe_idle.png"
                    hover "images/Maps/Fields/scythe_hover.png"
                    selected_idle "images/Maps/Fields/scythe_hover.png"
                    selected (active_tool == "scythe")
                    sensitive tutorial_target("fields_pick_scythe")
                    action [Function(renpy.sound.play, audio.click_1), If(active_tool == "scythe",
                        true=[SetVariable("active_tool", None), SetVariable("default_mouse", "default")],
                        false=[SetVariable("active_tool", "scythe"), SetVariable("default_mouse", "scythe"), Function(tutorial_advance_if, "fields_pick_scythe", "fields_harvest_click")])]  # <-- added cursor

            imagebutton:
                idle "images/Maps/Fields/hoe_idle.png"
                hover "images/Maps/Fields/hoe_hover.png"
                selected_idle "images/Maps/Fields/hoe_hover.png"
                selected (active_tool == "hoe")
                sensitive tutorial_target("fields_pick_hoe")
                action [Function(renpy.sound.play, audio.click_1), If(active_tool == "hoe",
                    true=[SetVariable("active_tool", None), SetVariable("default_mouse", "default")],
                    false=[SetVariable("active_tool", "hoe"), SetVariable("default_mouse", "hoe"), Function(tutorial_advance_if, "fields_pick_hoe", "fields_hoe_click")])]  # <-- added cursor

            imagebutton:
                idle "images/Maps/Fields/cancel_idle.png"
                hover "images/Maps/Fields/cancel_hover.png"
                sensitive tutorial_locked_out()
                action [SetVariable("active_tool", None), SetVariable("default_mouse", "default")]  # <-- resets cursor

    # Seed selector - only visible when seeds tool is active
    if active_tool == "seeds":
        frame:
            xalign 0.85
            yalign 0.5
            xsize 160
            background "images/Maps/Fields/Toolmat.png"

            vbox:
                xalign 0.5
                spacing 8

                text "Seeds" xalign 0.5 color "#ffffff"

                hbox:
                    spacing 6
                    xoffset 8
                    imagebutton:
                        idle "images/Maps/Fields/wheat_seed.png"
                        hover "images/Maps/Fields/wheat_seed_hover.png"
                        selected_idle "images/Maps/Fields/wheat_seed.png"
                        insensitive At("images/Maps/Fields/wheat_seed.png", seed_greyed)
                        selected (selected_seed == "wheat")
                        sensitive tutorial_target("fields_pick_seed") and player_inventory["wheat_seed"] > 0
                        action [SetVariable("selected_seed", "wheat"), SetVariable("default_mouse", "seeds"), Function(renpy.restart_interaction), Function(tutorial_advance_if, "fields_pick_seed", "fields_plant")]   # <-- added cursor
                    text ("x" + str(player_inventory["wheat_seed"])) color "#ffffff" yalign 0.5 size 19 xoffset -10 xsize 44

                hbox:
                    spacing 6
                    xoffset 8
                    imagebutton:
                        idle "images/Maps/Fields/corn_seed.png"
                        hover "images/Maps/Fields/corn_seed_hover.png"
                        selected_idle "images/Maps/Fields/corn_seed.png"
                        insensitive At("images/Maps/Fields/corn_seed.png", seed_greyed)
                        selected (selected_seed == "corn")
                        sensitive tutorial_locked_out() and player_inventory["corn_seed"] > 0
                        action [SetVariable("selected_seed", "corn"), SetVariable("default_mouse", "seeds"), Function(renpy.restart_interaction)]    # <-- added cursor
                    text ("x" + str(player_inventory["corn_seed"])) color "#ffffff" yalign 0.5 size 19 xoffset -10 xsize 44

                hbox:
                    spacing 6
                    xoffset 8
                    imagebutton:
                        idle "images/Maps/Fields/carrot_seed.png"
                        hover "images/Maps/Fields/carrot_seed_hover.png"
                        selected_idle "images/Maps/Fields/carrot_seed.png"
                        insensitive At("images/Maps/Fields/carrot_seed.png", seed_greyed)
                        selected (selected_seed == "carrot")
                        sensitive tutorial_locked_out() and player_inventory["carrot_seed"] > 0
                        action [SetVariable("selected_seed", "carrot"), SetVariable("default_mouse", "seeds"), Function(renpy.restart_interaction)]  # <-- added cursor
                    text ("x" + str(player_inventory["carrot_seed"])) color "#ffffff" yalign 0.5 size 19 xoffset -10 xsize 44

                hbox:
                    spacing 6
                    xoffset 8
                    imagebutton:
                        idle "images/Maps/Fields/pumpkin_seed.png"
                        hover "images/Maps/Fields/pumpkin_seed_hover.png"
                        selected_idle "images/Maps/Fields/pumpkin_seed.png"
                        insensitive At("images/Maps/Fields/pumpkin_seed.png", seed_greyed)
                        selected (selected_seed == "pumpkin")
                        sensitive tutorial_locked_out() and player_inventory["pumpkin_seed"] > 0
                        action [SetVariable("selected_seed", "pumpkin"), SetVariable("default_mouse", "seeds"), Function(renpy.restart_interaction)] # <-- added cursor
                    text ("x" + str(player_inventory["pumpkin_seed"])) color "#ffffff" yalign 0.5 size 19 xoffset -10 xsize 44

                hbox:
                    spacing 6
                    xoffset 8
                    imagebutton:
                        idle "images/Maps/Fields/apple_seed.png"
                        hover "images/Maps/Fields/apple_seed_hover.png"
                        selected_idle "images/Maps/Fields/apple_seed.png"
                        insensitive At("images/Maps/Fields/apple_seed.png", seed_greyed)
                        selected (selected_seed == "apple")
                        sensitive tutorial_locked_out() and player_inventory["apple_seed"] > 0
                        action [SetVariable("selected_seed", "apple"), SetVariable("default_mouse", "seeds"), Function(renpy.restart_interaction)]   # <-- added cursor
                    text ("x" + str(player_inventory["apple_seed"])) color "#ffffff" yalign 0.5 size 19 xoffset -10 xsize 44

screen Farm_map:
    on "show" action SetVariable("current_map", "Farm_map")
    add "images/Maps/Farm/Farm3_map.png"

    frame:
        xalign 0.0
        yalign 0.0
        xsize 400
        ysize 70
        background "images/Backgrounds/UI/wood4.png"

        text "Malik's Farm" xalign 0.0 yalign 0.5 xoffset 8 yoffset -3 font "name.otf" color "#ffffff" size 40

        hbox:
            xalign 0.0
            yalign 0.5
            xoffset 231
            spacing 6
            add "images/Maps/Market/cash.png" yalign 0.5 xsize 32 ysize 32
            text str(player_gold) color "#ffffff" yalign 0.5 size 22

    imagebutton:
        idle "images/Maps/Farm/Farmhouse3_idle.png"
        hover "images/Maps/Farm/Farmhouse3_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_target("farm_to_house")
        action [Function(renpy.sound.play, audio.click_1), Function(go_to_map, "FHhallway_map"), Function(tutorial_advance_if, "farm_to_house", "house_intro")]

    imagebutton:
        idle "images/Maps/Farm/Stables3_idle.png"
        hover "images/Maps/Farm/Stables3_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_target("farm_to_stables")
        action [Function(renpy.sound.play, audio.click_1), Function(go_to_map, "Stables_map"), Function(tutorial_advance_if, "farm_to_stables", "stables_info")]

    imagebutton:
        idle "images/Maps/Farm/Market3_idle.png"
        hover "images/Maps/Farm/Market3_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_target("farm_intro")
        action [Function(renpy.sound.play, audio.click_1), Function(go_to_map, "Market_map"), SetVariable("market_tab", "buy"), SetVariable("market_buy_category", "seeds"), Function(tutorial_advance_if, "farm_intro", "market_intro")]

    imagebutton:
        idle "images/Maps/Farm/Fields3_idle.png"
        hover "images/Maps/Farm/Fields3_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_target("farm_to_fields")
        action [Function(renpy.sound.play, audio.click_1), Function(go_to_map, "Fields_map"), Function(tutorial_setup_fields), Function(tutorial_advance_if, "farm_to_fields", "fields_pick_tool")]

screen FHhallway_map:
    on "show" action SetVariable("current_map", "FHhallway_map")
    use quick_menu
    add "images/Maps/FHhallway/FHhallway.png"

    imagebutton:
        idle "images/Maps/FHhallway/MCdoor_idle.png"
        hover "images/Maps/FHhallway/MCdoor_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_target("house_pick_room")
        action [Function(renpy.sound.play, audio.door_open), Function(go_to_map, "MC_map"), Function(tutorial_advance_if, "house_pick_room", "mc_bed_click")]

    imagebutton:
        idle "images/Maps/FHhallway/CTdoor_idle.png"
        hover "images/Maps/FHhallway/CTdoor_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_locked_out()
        action [Function(renpy.sound.play, audio.door_open), Function(go_to_map, "CT_map")]

    imagebutton:
        idle "images/Maps/FHhallway/MEdoor_idle.png"
        hover "images/Maps/FHhallway/MEdoor_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_locked_out()
        action [Function(renpy.sound.play, audio.door_open), Function(go_to_map, "ME_map")]

    imagebutton:
        idle "images/Maps/FHhallway/DGdoor_idle.png"
        hover "images/Maps/FHhallway/DGdoor_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_locked_out()
        action [Function(renpy.sound.play, audio.door_open), Function(go_to_map, "DG_map")]

    imagebutton:
        idle "images/Maps/FHhallway/FHexit_idle.png"
        hover "images/Maps/FHhallway/FHexit_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_locked_out()
        action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "Farm_map")]

screen Stables_map:
    on "show" action SetVariable("current_map", "Stables_map")
    use quick_menu
    add "images/Maps/Stables/Stables_map.png"

    imagebutton:
        idle "images/Maps/Stables/PGdoor_idle.png"
        hover "images/Maps/Stables/PGdoor_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_target("stables_pg_door")
        action [Function(renpy.sound.play, audio.door_open), Function(go_to_map, "PG_map"), Function(tutorial_advance_if, "stables_pg_door", "pg_intro")]

    imagebutton:
        idle "images/Maps/Stables/GTdoor_idle.png"
        hover "images/Maps/Stables/GTdoor_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_locked_out()
        action [Function(renpy.sound.play, audio.door_open), Function(go_to_map, "GT_map")]

    imagebutton:
        idle "images/Maps/Stables/CWdoor_idle.png"
        hover "images/Maps/Stables/CWdoor_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_locked_out()
        action [Function(renpy.sound.play, audio.door_open), Function(go_to_map, "CW_map")]

    imagebutton:
        idle "images/Maps/Stables/HEdoor_idle.png"
        hover "images/Maps/Stables/HEdoor_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_locked_out()
        action [Function(renpy.sound.play, audio.door_open), Function(go_to_map, "HE_map")]

    imagebutton:
        idle "images/Maps/Stables/BYdoor_idle.png"
        hover "images/Maps/Stables/BYdoor_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_locked_out()
        action [Function(renpy.sound.play, audio.door_open), Function(go_to_map, "BY_map")]

    imagebutton:
        idle "images/Maps/Stables/SPdoor_idle.png"
        hover "images/Maps/Stables/SPdoor_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_locked_out()
        action [Function(renpy.sound.play, audio.door_open), Function(go_to_map, "SP_map")]

    imagebutton:
        idle "images/Maps/Stables/Stablesexit_idle.png"
        hover "images/Maps/Stables/Stablesexit_hover.png"
        xpos 0 ypos 0
        focus_mask True
        sensitive tutorial_locked_out()
        action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "Farm_map")]

screen Market_map:
    on "show" action SetVariable("current_map", "Market_map")
    use quick_menu
    add "images/Maps/Market/Market_map_blur.jpg"
    add "images/Sprites/Chicken/cn_1.png" at fit_left

    frame:
        xpos (1050 - 8 - 2)
        xanchor 0.0
        yalign 0.5
        xsize (620 + 16 + 4)
        ysize (820 + 16 + 4)
        background "#000000ff"

    frame:
        xpos (1050 - 8)
        xanchor 0.0
        yalign 0.5
        xsize (620 + 16)
        ysize (820 + 16)
        background Frame("images/Textures/gold1.jpg", 0, 0)

    frame:
        xpos 1050
        xanchor 0.0
        yalign 0.5
        xsize 620
        ysize 820
        background Frame("images/Textures/bwood3.jpg", 0, 0)

        vbox:
            xsize 620
            xalign 0.5
            spacing 16

            hbox:
                xalign 0.5
                spacing 10
                add "images/Maps/Market/cash.png" yalign 0.5 xsize 50 ysize 50
                text str(player_gold) color "#ffffff" yalign 0.5 size 40

            hbox:
                xalign 0.5
                spacing 0

                $ buy_bg = "#df1515" if market_tab == "buy" else "#222222"
                $ sell_bg = "#2dab11" if market_tab == "sell" else "#222222"

                fixed:
                    xsize 164
                    ysize 74
                    frame:
                        xsize 164
                        ysize 74
                        background Frame("images/Textures/gold1.jpg", 0, 0)
                    button:
                        xalign 0.5
                        yalign 0.5
                        xsize 160
                        ysize 70
                        background buy_bg
                        hover_background "#7f3e3e"
                        sensitive tutorial_locked_out()
                        action SetVariable("market_tab", "buy")
                        text "Buy":
                            xalign 0.5
                            yalign 0.5
                            color "#ffffff"
                            size 60

                fixed:
                    xsize 164
                    ysize 74
                    frame:
                        xsize 164
                        ysize 74
                        background Frame("images/Textures/gold1.jpg", 0, 0)
                    button:
                        xalign 0.5
                        yalign 0.5
                        xsize 160
                        ysize 70
                        background sell_bg
                        hover_background "#3a6734"
                        sensitive tutorial_locked_out()
                        action SetVariable("market_tab", "sell")
                        text "Sell":
                            xalign 0.5
                            yalign 0.5
                            color "#ffffff"
                            size 60

            if market_tab == "buy":
                hbox:
                    xalign 0.5
                    spacing 0
                    at Transform(zoom=0.95)

                    $ seeds_bg = "#df1515" if market_buy_category == "seeds" else "#222222"
                    $ food_bg = "#2dab11" if market_buy_category == "food" else "#222222"
                    $ tools_bg = "#3a6fa0" if market_buy_category == "tools" else "#222222"
                    $ costumes_bg = "#9b59b6" if market_buy_category == "costumes" else "#222222"

                    fixed:
                        xsize 154
                        ysize 64
                        frame:
                            xsize 154
                            ysize 64
                            background Frame("images/Textures/gold1.jpg", 0, 0)
                        button:
                            xalign 0.5
                            yalign 0.5
                            xsize 150
                            ysize 60
                            background seeds_bg
                            hover_background "#7f3e3e"
                            sensitive tutorial_locked_out()
                            action SetVariable("market_buy_category", "seeds")
                            text "Seeds":
                                xalign 0.5
                                yalign 0.5
                                color "#ffffff"
                                size 34

                    fixed:
                        xsize 154
                        ysize 64
                        frame:
                            xsize 154
                            ysize 64
                            background Frame("images/Textures/gold1.jpg", 0, 0)
                        button:
                            xalign 0.5
                            yalign 0.5
                            xsize 150
                            ysize 60
                            background food_bg
                            hover_background "#3a6734"
                            sensitive tutorial_locked_out()
                            action SetVariable("market_buy_category", "food")
                            text "Food":
                                xalign 0.5
                                yalign 0.5
                                color "#ffffff"
                                size 34

                    fixed:
                        xsize 154
                        ysize 64
                        frame:
                            xsize 154
                            ysize 64
                            background Frame("images/Textures/gold1.jpg", 0, 0)
                        button:
                            xalign 0.5
                            yalign 0.5
                            xsize 150
                            ysize 60
                            background tools_bg
                            hover_background "#2c5680"
                            sensitive tutorial_locked_out()
                            action SetVariable("market_buy_category", "tools")
                            text "Tools":
                                xalign 0.5
                                yalign 0.5
                                color "#ffffff"
                                size 34

                    fixed:
                        xsize 154
                        ysize 64
                        frame:
                            xsize 154
                            ysize 64
                            background Frame("images/Textures/gold1.jpg", 0, 0)
                        button:
                            xalign 0.5
                            yalign 0.5
                            xsize 150
                            ysize 60
                            background costumes_bg
                            hover_background "#764088"
                            sensitive tutorial_locked_out()
                            action SetVariable("market_buy_category", "costumes")
                            text "Costumes":
                                xalign 0.5
                                yalign 0.5
                                color "#ffffff"
                                size 34

                $ market_buy_visible = [i for i in market_buy if i["category"] == market_buy_category]

                if len(market_buy_visible) == 0:
                    frame:
                        xsize 600
                        ysize 600
                        background None
                        text "Nothing here yet" color "#aaaaaa" size 24 xalign 0.5 yalign 0.5
                else:
                    viewport:
                        xsize 600
                        ysize 600
                        scrollbars "vertical"
                        mousewheel True

                        vbox:
                            xsize 580
                            spacing 14

                            for idx in range(len(market_buy_visible)):
                                $ item = market_buy_visible[idx]
                                frame:
                                    xsize 570
                                    background "#222222"

                                    hbox:
                                        xsize 560
                                        spacing 14
                                        yalign 0.5

                                        add item["image"] xsize 80 ysize 80 fit "contain" yalign 0.5 xoffset (14 if item["id"] in ("life_saver", "macabre_bovine") else 0)

                                        vbox:
                                            xsize 270
                                            yalign 0.5
                                            spacing 6
                                            text item["label"] color "#ffffff" size 20
                                            hbox:
                                                spacing 6
                                                add "images/Maps/Market/cash.png" yalign 0.5 xsize 50 ysize 50
                                                text str(item["price"]) color "#ffdd00" size 40 yalign 0.5

                                        if item["category"] == "costumes" and item["id"] not in ("piggy_icon", "stars_stripes"):
                                            text "Patreon Only":
                                                xalign 1.0
                                                yalign 0.5
                                                color "#ff3333"
                                                size 32
                                        elif (item["category"] in ("costumes", "tools") or item["id"] in ("truffle", "golden_truffle", "ramen", "golden_ramen", "choco", "golden_choco", "cheesecake", "golden_cheesecake")) and player_inventory[item["id"]] > 0:
                                            text "Sold Out":
                                                xalign 1.0
                                                yalign 0.5
                                                color "#ff0000"
                                                size 40
                                        else:
                                            textbutton "Buy":
                                                xalign 1.0
                                                yalign 0.5
                                                text_color "#ffffff"
                                                text_hover_color "#ffdd00"
                                                text_size 50
                                                sensitive (player_gold >= item["price"]) and tutorial_locked_out()
                                                action Function(buy_item, item)

            if market_tab == "sell":
                viewport:
                    xsize 600
                    ysize 680
                    scrollbars "vertical"
                    mousewheel True

                    vbox:
                        xsize 580
                        spacing 14

                        for idx in range(len(market_sell)):
                            $ item = market_sell[idx]
                            frame:
                                xsize 570
                                background "#222222"

                                hbox:
                                    xsize 560
                                    spacing 14
                                    yalign 0.5

                                    add item["image"] xsize 80 ysize 80 fit "contain" yalign 0.5

                                    vbox:
                                        xsize 270
                                        yalign 0.5
                                        spacing 6
                                        hbox:
                                            spacing 8
                                            text item["label"] color "#ffffff" size 20
                                            text ("x" + str(player_inventory[item["id"]])) color "#aaaaaa" size 18 yalign 0.5
                                        hbox:
                                            spacing 6
                                            add "images/Maps/Market/cash.png" yalign 0.5 xsize 50 ysize 50
                                            text str(item["price"]) color "#ffdd00" size 40 yalign 0.5

                                    if player_inventory[item["id"]] == 0:
                                        text "None in inventory":
                                            xalign 1.0
                                            yalign 0.5
                                            color "#ff0000"
                                            size 30
                                    else:
                                        textbutton "Sell":
                                            xalign 1.0
                                            yalign 0.5
                                            text_color "#ffffff"
                                            text_hover_color "#ffdd00"
                                            text_size 50
                                            sensitive tutorial_locked_out()
                                            action Function(sell_item, market_sell[idx])

screen persistent_hud():
    zorder 100

    mousearea:                                                     # <-- new, tracks hover region
        xalign 0.0
        yalign 0.0
        xsize 300
        ysize 70
        hovered SetVariable("default_mouse", "default")
        unhovered Function(restore_tool_cursor)

    frame:                                                         # <-- back to frame
        xalign 0.0
        yalign 0.0
        xsize 400
        ysize 70
        background "images/Backgrounds/UI/wood4.png"

        hbox:
            xalign 0.0
            yalign 0.5
            spacing 16
            xoffset 8

            imagebutton:
                yalign 0.5
                yoffset -5
                idle "images/Icons/farm_icon.png"
                hover "images/Icons/farm_icon_hover.png"
                at button_scale
                sensitive tutorial_target_any("market_return", "fields_return", "stables_return")
                action [Function(renpy.sound.play, audio.click_1), Function(go_to_map, "Farm_map"), Function(tutorial_go_home)]

            imagebutton:
                yalign 0.5
                yoffset -2.5
                idle "images/Inventory/inv_icon.png"
                hover "images/Inventory/inv_icon_hover.png"
                at button_scale
                sensitive tutorial_locked_out()
                action [Function(renpy.sound.play, audio.click_1), If(renpy.get_screen("inventory_screen"),
                    true=Hide("inventory_screen"),
                    false=Show("inventory_screen"))]

            imagebutton:
                yalign 0.5
                yoffset -1.9
                idle "images/Icons/bio_idle.png"
                hover "images/Icons/bio_hover.png"
                at Transform(zoom=0.37)
                sensitive tutorial_locked_out()
                action [Function(renpy.sound.play, audio.click_1), If(renpy.get_screen("bio_screen"),
                    true=Hide("bio_screen"),
                    false=Show("bio_screen"))]
            
            hbox:
                spacing 6
                yalign 0.5
                add "images/Maps/Market/cash.png" yalign 0.5 xsize 32 ysize 32
                text str(player_gold) color "#ffffff" yalign 0.5 size 22

screen inventory_screen():
    zorder 90
    on "show" action [SetVariable("active_tool", None), SetVariable("selected_seed", None), SetVariable("active_care_tool", None), SetVariable("default_mouse", "default")]

    add "#00000080"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080
        background "images/Inventory/inv_back.png"
        modal True

        text "Inventory" xalign 0.5 ypos 180 color "#ffffff" size 54

        textbutton "✕ Close":
            xalign 0.5
            yalign 0.89
            text_color "#ffffff"
            text_hover_color "#ff0000"
            text_size 50
            action Hide("inventory_screen")

        $ special_gift_ids = ("truffle", "golden_truffle", "choco", "golden_choco", "ramen", "golden_ramen", "cheesecake", "golden_cheesecake")
        $ inv_seed_items = [i for i in market_buy if i["category"] == "seeds"]
        $ inv_food_items = [i for i in market_buy if i["category"] == "food" and i["id"] not in special_gift_ids]
        $ inv_special_items = [i for i in market_buy if i["id"] in special_gift_ids]
        $ inv_tool_items = [i for i in market_buy if i["category"] == "tools" and player_inventory[i["id"]] > 0]
        $ inv_costume_items = [i for i in market_buy if i["category"] == "costumes" and player_inventory[i["id"]] > 0]

        hbox:
            xalign 0.5
            xoffset -22
            ypos 285
            spacing 16

            frame:
                xsize 260
                ysize 570
                background None

                vbox:
                    xsize 260
                    spacing 16

                    text "Seeds" xalign 0.5 color "#ffdd00" size 30

                    for item in inv_seed_items:
                        hbox:
                            spacing 8
                            xalign 0.0
                            add item["image"] xsize 56 ysize 56 yalign 0.5 fit "contain"
                            text item["label"] color "#ffffff" size 22 yalign 0.5 xsize 132
                            frame:
                                xsize 40
                                yalign 0.5
                                background None
                                text str(player_inventory[item["id"]]) color "#ffffff" size 22 yalign 0.5

            frame:
                xsize 260
                ysize 570
                background None

                vbox:
                    xsize 260
                    spacing 9

                    text "Food" xalign 0.5 color "#ffdd00" size 30

                    for item in inv_food_items:
                        hbox:
                            spacing 7
                            xalign 0.0
                            add item["image"] xsize 42 ysize 42 yalign 0.5 fit "contain"
                            text item["label"] color "#ffffff" size 18 yalign 0.5 xsize 140
                            frame:
                                xsize 36
                                yalign 0.5
                                background None
                                text str(player_inventory[item["id"]]) color "#ffffff" size 18 yalign 0.5

            frame:
                xsize 260
                ysize 570
                background None

                vbox:
                    xsize 260
                    spacing 10

                    text "Special" xalign 0.5 color "#ffdd00" size 30

                    for item in inv_special_items:
                        hbox:
                            spacing 7
                            xalign 0.0
                            add item["image"] xsize 46 ysize 46 yalign 0.5 fit "contain"
                            text item["label"] color "#ffffff" size 19 yalign 0.5 xsize 122
                            frame:
                                xsize 38
                                yalign 0.5
                                background None
                                text str(player_inventory[item["id"]]) color "#ffffff" size 19 yalign 0.5

            frame:
                xsize 260
                ysize 570
                background None

                vbox:
                    xsize 260
                    spacing 18

                    text "Tools" xalign 0.5 color "#ffdd00" size 30

                    if not inv_tool_items:
                        text "Nothing here yet" color "#aaaaaa" size 18 xalign 0.5
                    else:
                        for item in inv_tool_items:
                            hbox:
                                spacing 10
                                xalign 0.0
                                add item["image"] xsize 64 ysize 64 yalign 0.5 fit "contain"
                                text item["label"].split(" (")[0] color "#ffffff" size 28 yalign 0.5 xsize 175

            frame:
                xsize 260
                ysize 570
                background None

                vbox:
                    xsize 260
                    spacing 4

                    text "Costumes" xalign 0.5 color "#ffdd00" size 30

                    if not inv_costume_items:
                        text "Nothing here yet" color "#aaaaaa" size 18 xalign 0.5
                    else:
                        for costume_row in range(0, len(inv_costume_items), 3):
                            $ costume_row_items = inv_costume_items[costume_row:costume_row + 3]
                            hbox:
                                spacing 2
                                xalign 0.5

                                for costume_item in costume_row_items:
                                    vbox:
                                        xsize 88
                                        spacing 1
                                        add costume_item["image"] xsize 34 ysize 34 xalign 0.5 fit "contain"
                                        text costume_item["label"].replace(" Costume", "") color "#ffffff" size 11 xalign 0.5 text_align 0.5

screen bio_screen():
    zorder 90
    on "show" action [SetVariable("active_tool", None), SetVariable("selected_seed", None), SetVariable("active_care_tool", None), SetVariable("default_mouse", "default"), Hide("persistent_hud")]
    on "hide" action If(current_map != "Farm_map", true=Show("persistent_hud"), false=NullAction())

    add "#00000080"

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1920
        ysize 1080
        padding (0, 0)
        background None
        modal True

        add BIO_IMAGES[bio_character] xsize 1920 ysize 1080

        frame:
            xpos (357 - 8 - 2)
            ypos (207 - 8 - 2)
            xsize (637 + 16 + 4)
            ysize (637 + 16 + 4)
            background "#000000ff"

        frame:
            xpos (357 - 8)
            ypos (207 - 8)
            xsize (637 + 16)
            ysize (637 + 16)
            background Frame("images/Textures/gold1.jpg", 0, 0)

        frame:
            xpos 357
            ypos 207
            xsize 637
            ysize 637
            background Frame("images/Textures/leather.jpg", 0, 0)
            padding (29, 29)

            vbox:
                xsize 578
                spacing 18

                text BIO_TITLES[bio_character] color "#ffdd00" size 47 xalign 0.5 xsize 578

                text ("Care: " + str(animal_care[bio_character]["care"]) + "%") color "#ffffff" size 29 xsize 578

                text "Likes:" color "#ffdd00" size 25 xsize 578
                text BIO_LIKES[bio_character] color "#ffffff" size 24 xsize 578

                text "Scenes:" color "#ffdd00" size 25 xsize 578

                for i in range(3):
                    hbox:
                        spacing 14
                        yalign 0.5

                        frame:
                            xsize 35
                            ysize 35
                            background ("#2ecc71" if scene_viewed[bio_character][i] else "#e74c3c")
                            if scene_viewed[bio_character][i]:
                                text "✓" font "DejaVuSans.ttf" color "#ffffff" size 33 xalign 0.5 yalign 0.48 xoffset 5 yoffset -2

                        text (SCENE_LABELS[bio_character][i] if scene_viewed[bio_character][i] else "??") color "#ffffff" size 24 yalign 0.5

                        if not (bio_character == "pig" and i == 0):
                            text "Patreon Only" color "#ff3333" size 20 yalign 0.5

        imagebutton:
            idle "images/bio/Larrow_idle.png"
            hover "images/bio/Larrow_hover.png"
            xanchor 0.0
            yanchor 1.0
            xpos 60
            ypos 660
            at Transform(zoom=0.50)
            action [Function(renpy.sound.play, audio.click_1), Function(bio_prev)]

        imagebutton:
            idle "images/bio/Rarrow_idle.png"
            hover "images/bio/Rarrow_hover.png"
            xanchor 1.0
            yanchor 1.0
            xpos 1850
            ypos 650
            at Transform(zoom=0.50)
            action [Function(renpy.sound.play, audio.click_1), Function(bio_next)]

        imagebutton:
            idle "images/bio/x_idle.png"
            hover "images/bio/x_hover.png"
            xanchor 1.0
            yanchor 0.0
            xpos 370
            ypos 80
            at Transform(zoom=0.40)
            action [Function(renpy.sound.play, audio.click_1), Hide("bio_screen")]

screen MC_map:
    on "show" action SetVariable("current_map", "MC_map")
    use quick_menu

    if player_character == "Malik":
        add "images/Maps/MC/MC_Gorilla.png"
    elif player_character == "King":
        add "images/Maps/MC/MC_Bear.png"
    elif player_character == "Thunder":
        add "images/Maps/MC/MC_Horse.jpeg"
    else:
        add "images/Maps/MC/MC_Gorilla.png"

    if player_character == "Malik":
        imagebutton:
            idle "images/Maps/MC/bed_gorilla_idle.png"
            hover "images/Maps/MC/bed_gorilla_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            sensitive tutorial_target("mc_bed_click")
            action [Function(tutorial_advance_if, "mc_bed_click", "tutorial_done"), Jump("sleep_transition")]                        # <-- changed

    elif player_character == "King":
        imagebutton:
            idle "images/Maps/MC/bed_bear_idle.png"
            hover "images/Maps/MC/bed_bear_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            sensitive tutorial_target("mc_bed_click")
            action [Function(tutorial_advance_if, "mc_bed_click", "tutorial_done"), Jump("sleep_transition")]                        # <-- changed

    elif player_character == "Thunder":
        imagebutton:
            idle "images/Maps/MC/bed_horse_idle.png"
            hover "images/Maps/MC/bed_horse_hover.png"
            xpos 0
            ypos 0
            focus_mask True
            sensitive tutorial_target("mc_bed_click")
            action [Function(tutorial_advance_if, "mc_bed_click", "tutorial_done"), Jump("sleep_transition")]                        # <-- changed

############# ANIMAL MAPS ###############################################################

screen HE_map:
    on "show" action [SetVariable("current_map", "HE_map"), SetVariable("active_care_tool", None), SetVariable("show_socialize", False), SetVariable("show_gift", False), SetVariable("show_costume", False)]
    use quick_menu
    add "images/Backgrounds/Stables/HE_1_blur.jpg"

    # Interaction panel
    $ panel_yalign = 0.65 if (show_socialize or show_gift or show_costume) else 0.5

    vbox:
        xalign 0.02
        yalign panel_yalign
        spacing 45

        if show_socialize:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_gift:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_costume:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("horse_costume", "default")]
                text "Default":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26
                if horse_costume == "default":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["horse_pill"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("horse_costume", "horse_pill")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Horse Pill" xalign 0.5 yoffset (9 if player_inventory["horse_pill"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["horse_pill"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if horse_costume == "horse_pill":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["peg_is_sus"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("horse_costume", "peg_is_sus")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Peg is Sus?" xalign 0.5 yoffset (9 if player_inventory["peg_is_sus"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["peg_is_sus"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if horse_costume == "peg_is_sus":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        else:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", True)]
                text "Socialize":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Gift":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", True)]
                text "Costume":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

    # Care tool panel
    frame:
        xalign 0.98
        yalign 0.5
        xsize 224
        background "#000000eb"

        vbox:
            xalign 0.5
            spacing 22

            text "Care" xalign 0.5 color "#ffffff" size 28

            imagebutton:
                idle At("images/Maps/Stables/wash.png", tool_scale)
                hover At("images/Maps/Stables/wash_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/wash_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/wash_greyed.png", tool_scale)
                selected (active_care_tool == "wash")
                sensitive (not animal_care["horse"]["washed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "wash",
                    true=[SetVariable("active_care_tool", None), SetVariable("animal_hovered", dict(animal_hovered, horse=False))],
                    false=[SetVariable("active_care_tool", "wash"), SetVariable("animal_hovered", dict(animal_hovered, horse=False))])]

            imagebutton:
                idle At("images/Maps/Stables/brush.png", tool_scale)
                hover At("images/Maps/Stables/brush_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/brush_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/brush_greyed.png", tool_scale)
                selected (active_care_tool == "brush")
                sensitive (not animal_care["horse"]["brushed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "brush",
                    true=[SetVariable("active_care_tool", None), SetVariable("animal_hovered", dict(animal_hovered, horse=False))],
                    false=[SetVariable("active_care_tool", "brush"), SetVariable("animal_hovered", dict(animal_hovered, horse=False))])]

            imagebutton:
                idle At("images/Maps/Stables/feed.png", tool_scale)
                hover At("images/Maps/Stables/feed_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/feed_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/feed_greyed.png", tool_scale)
                selected (active_care_tool == "feed")
                sensitive (not animal_care["horse"]["fed"] and player_inventory["apple"] > 0)
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "feed",
                    true=[SetVariable("active_care_tool", None), SetVariable("animal_hovered", dict(animal_hovered, horse=False))],
                    false=[SetVariable("active_care_tool", "feed"), SetVariable("animal_hovered", dict(animal_hovered, horse=False))])]

            fixed:
                xsize 196
                ysize 80
                if player_inventory["apple"] == 0 and not animal_care["horse"]["fed"]:
                    frame:
                        xsize 196
                        yoffset -70
                        background "#00000090"
                        xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            add "images/Maps/Fields/apple_item.png" xsize 50 ysize 50 yalign 0.5
                            text "Need apple" color "#ff6b6b" size 25 xalign 0.5 yalign 0.65

            imagebutton:
                idle "images/Maps/Stables/stable_door.png"
                hover "images/Maps/Stables/stable_door_hover.png"
                action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "Stables_map")]
                xoffset 35
                yoffset -50

    # Care meter
    frame:
        xalign 0.08
        yalign 0.28
        xsize 500
        ysize 120
        background "#000000e7"

        vbox:
            xalign 0.5
            spacing 10

            text "Lady Moonbeam" xalign 0.5 color "#ffffff" size 26

            hbox:
                xalign 0.5
                spacing 12
                yalign 0.5

                add "images/Maps/Stables/heart.png" xsize 36 ysize 36 yalign 0.5

                fixed:
                    xsize 380
                    ysize 36
                    yalign 0.5

                    bar:
                        xsize 380
                        ysize 36
                        yalign 0.5
                        value animal_care["horse"]["care"]
                        range 100
                        left_bar "#ff6b6b"
                        right_bar "#333333"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 121
                        background "#ffffff"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 244
                        background "#ffffff"

    # Sprite display
    $ horse_costume_suffix = {"horse_pill": "HEC1", "peg_is_sus": "HEC2"}.get(horse_costume)
    if show_care_heart["horse"]:
        add ("images/Maps/Stables/%s_heart.png" % horse_costume_suffix if horse_costume_suffix else "images/Maps/Stables/HE_heart.png") at fit_sprite
        timer 1.0 action Function(reset_care_heart, "horse")
    else:
        add ("images/Sprites/Horse/%s.png" % horse_costume_suffix if horse_costume_suffix else "images/Sprites/Horse/he_1.png") at fit_sprite

        if active_care_tool != None and animal_hovered["horse"]:
            add ("images/Maps/Stables/%s_hover.png" % horse_costume_suffix if horse_costume_suffix else "images/Maps/Stables/HE_hover.png") at fit_sprite

        button:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 600
            background None
            hovered Function(set_animal_hovered, "horse", True)
            unhovered Function(set_animal_hovered, "horse", False)
            action If(active_care_tool != None,
                true=Function(do_care_task, "horse", active_care_tool),
                false=NullAction())

screen PG_map:
    on "show" action [SetVariable("current_map", "PG_map"), SetVariable("active_care_tool", None), SetVariable("show_socialize", False), SetVariable("show_gift", False), SetVariable("show_costume", False)]
    use quick_menu
    add "images/Backgrounds/Stables/PG_1_blur.jpg"

    $ panel_yalign = 0.65 if (show_socialize or show_gift or show_costume) else 0.5

    vbox:
        xalign 0.02
        yalign panel_yalign
        spacing 45

        if show_socialize:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (animal_care["pig"]["care"] >= 33)
                    action [Function(renpy.sound.play, audio.click_1), Hide("PG_map"), Function(renpy.jump, "Pig1")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Meet Pudding" xalign 0.5 yoffset 6 color "#ffffff" size 26 xsize 560
                    text "Care: 33%" xalign 0.5 yoffset -3 color "#aaaaaa" size 15 xsize 560

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_gift:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["truffle"] > 0 and not animal_gifted["pig"]["truffle"])
                    action Function(do_gift_task, "pig", "truffle")
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    if animal_gifted["pig"]["truffle"]:
                        text "Gifted!" xalign 0.5 color "#33ff33" size 22 xsize 560
                    else:
                        hbox:
                            xalign 0.5
                            yoffset 9
                            spacing 8
                            add "images/Maps/Market/truffle_item.png" xsize 30 ysize 30 yalign 0.5
                            text "Truffle" xalign 0.5 color "#ffffff" size 20 yalign 0.5 xsize 480
                        if player_inventory["truffle"] == 0:
                            text "(Available at the Market)" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                        else:
                            text ("x" + str(player_inventory["truffle"])) xalign 0.5 yoffset -3 color "#aaaaaa" size 15 xsize 560

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["golden_truffle"] > 0 and not animal_gifted["pig"]["golden_truffle"])
                    action Function(do_gift_task, "pig", "golden_truffle")
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    if animal_gifted["pig"]["golden_truffle"]:
                        text "Gifted!" xalign 0.5 color "#33ff33" size 22 xsize 560
                    else:
                        hbox:
                            xalign 0.5
                            yoffset 9
                            spacing 8
                            add "images/Maps/Market/golden_truffle_item.png" xsize 30 ysize 30 yalign 0.5
                            text "Golden Truffle" xalign 0.5 color "#ffffff" size 20 yalign 0.5 xsize 480
                        if player_inventory["golden_truffle"] == 0:
                            text "(Available at the Market)" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                        else:
                            text ("x" + str(player_inventory["golden_truffle"])) xalign 0.5 yoffset -3 color "#aaaaaa" size 15 xsize 560

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_costume:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("pig_costume", "default")]
                text "Default":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26
                if pig_costume == "default":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["piggy_icon"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("pig_costume", "piggy_icon")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Piggy Icon" xalign 0.5 yoffset (9 if player_inventory["piggy_icon"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["piggy_icon"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if pig_costume == "piggy_icon":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["stars_stripes"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("pig_costume", "stars_stripes")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Stars 'N' Stripes" xalign 0.5 yoffset (9 if player_inventory["stars_stripes"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["stars_stripes"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if pig_costume == "stars_stripes":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        else:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    sensitive tutorial_locked_out()
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", True)]
                text "Socialize":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    sensitive tutorial_locked_out()
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", True)]
                text "Gift":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    sensitive tutorial_locked_out()
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", True)]
                text "Costume":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

    # Care tool panel
    frame:
        xalign 0.98
        yalign 0.5
        xsize 224
        background "#000000eb"

        vbox:
            xalign 0.5
            spacing 22

            text "Care" xalign 0.5 color "#ffffff" size 28

            imagebutton:
                idle At("images/Maps/Stables/wash.png", tool_scale)
                hover At("images/Maps/Stables/wash_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/wash_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/wash_greyed.png", tool_scale)
                selected (active_care_tool == "wash")
                sensitive (not animal_care["pig"]["washed"]) and tutorial_target("pg_wash_tool")
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "wash",
                    true=[SetVariable("active_care_tool", None), SetVariable("animal_hovered", dict(animal_hovered, pig=False))],
                    false=[SetVariable("active_care_tool", "wash"), SetVariable("animal_hovered", dict(animal_hovered, pig=False)), Function(tutorial_advance_if, "pg_wash_tool", "pg_wash_click")])]

            imagebutton:
                idle At("images/Maps/Stables/brush.png", tool_scale)
                hover At("images/Maps/Stables/brush_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/brush_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/brush_greyed.png", tool_scale)
                selected (active_care_tool == "brush")
                sensitive (not animal_care["pig"]["brushed"]) and tutorial_target("pg_brush_tool")
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "brush",
                    true=[SetVariable("active_care_tool", None), SetVariable("animal_hovered", dict(animal_hovered, pig=False))],
                    false=[SetVariable("active_care_tool", "brush"), SetVariable("animal_hovered", dict(animal_hovered, pig=False)), Function(tutorial_advance_if, "pg_brush_tool", "pg_brush_click")])]

            imagebutton:
                idle At("images/Maps/Stables/feed.png", tool_scale)
                hover At("images/Maps/Stables/feed_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/feed_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/feed_greyed.png", tool_scale)
                selected (active_care_tool == "feed")
                sensitive (not animal_care["pig"]["fed"] and player_inventory["corn"] > 0) and tutorial_target("pg_feed_tool")
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "feed",
                    true=[SetVariable("active_care_tool", None), SetVariable("animal_hovered", dict(animal_hovered, pig=False))],
                    false=[SetVariable("active_care_tool", "feed"), SetVariable("animal_hovered", dict(animal_hovered, pig=False)), Function(tutorial_advance_if, "pg_feed_tool", "pg_feed_click")])]

            fixed:
                xsize 196
                ysize 80
                if player_inventory["corn"] == 0 and not animal_care["pig"]["fed"]:
                    frame:
                        xsize 196
                        yoffset -70
                        background "#00000090"
                        xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            add "images/Maps/Fields/corn_item.png" xsize 50 ysize 50 yalign 0.5
                            text "Need corn" color "#ff6b6b" size 25 xalign 0.5 yalign 0.65

            imagebutton:
                idle "images/Maps/Stables/stable_door.png"
                hover "images/Maps/Stables/stable_door_hover.png"
                sensitive tutorial_locked_out()
                action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "Stables_map")]
                xoffset 35
                yoffset -50

    # Care meter
    frame:
        xalign 0.08
        yalign 0.28
        xsize 500
        ysize 120
        background "#000000e7"

        vbox:
            xalign 0.5
            spacing 10

            text "Pudding the Pig" xalign 0.5 color "#ffffff" size 26

            hbox:
                xalign 0.5
                spacing 12
                yalign 0.5

                add "images/Maps/Stables/heart.png" xsize 36 ysize 36 yalign 0.5

                fixed:
                    xsize 380
                    ysize 36
                    yalign 0.5

                    bar:
                        xsize 380
                        ysize 36
                        yalign 0.5
                        value animal_care["pig"]["care"]
                        range 100
                        left_bar "#ff6b6b"
                        right_bar "#333333"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 121
                        background "#ffffff"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 244
                        background "#ffffff"

    # Sprite display
    $ pig_costume_suffix = {"piggy_icon": "PGC1", "stars_stripes": "PGC2"}.get(pig_costume)
    if show_care_heart["pig"]:
        add ("images/Maps/Stables/%s_heart.png" % pig_costume_suffix if pig_costume_suffix else "images/Maps/Stables/PG_heart.png") at fit_sprite
        timer 1.0 action Function(reset_care_heart, "pig")
    else:
        add ("images/Sprites/Pig/%s.png" % pig_costume_suffix if pig_costume_suffix else "images/Sprites/Pig/pg_1.png") at fit_sprite

        if active_care_tool != None and animal_hovered["pig"]:
            add ("images/Maps/Stables/%s_hover.png" % pig_costume_suffix if pig_costume_suffix else "images/Maps/Stables/PG_hover.png") at fit_sprite

        button:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 600
            background None
            hovered Function(set_animal_hovered, "pig", True)
            unhovered Function(set_animal_hovered, "pig", False)
            action If(active_care_tool != None,
                true=[Function(do_care_task, "pig", active_care_tool), Function(tutorial_check_pig_care)],
                false=NullAction())

screen GT_map:
    on "show" action [SetVariable("current_map", "GT_map"), SetVariable("active_care_tool", None), SetVariable("show_socialize", False), SetVariable("show_gift", False), SetVariable("show_costume", False)]
    use quick_menu
    add "images/Backgrounds/Stables/GT_1_blur.jpg"

    $ panel_yalign = 0.65 if (show_socialize or show_gift or show_costume) else 0.5

    vbox:
        xalign 0.02
        yalign panel_yalign
        spacing 45

        if show_socialize:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_gift:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["ramen"] > 0 and not animal_gifted["goat"]["ramen"])
                    action Function(do_gift_task, "goat", "ramen")
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    if animal_gifted["goat"]["ramen"]:
                        text "Gifted!" xalign 0.5 color "#33ff33" size 22 xsize 560
                    else:
                        hbox:
                            xalign 0.5
                            yoffset 9
                            spacing 8
                            add "images/Maps/Market/ramen.png" xsize 30 ysize 30 yalign 0.5
                            text "Ramen" xalign 0.5 color "#ffffff" size 20 yalign 0.5 xsize 480
                        if player_inventory["ramen"] == 0:
                            text "(Available at the Market)" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                        else:
                            text ("x" + str(player_inventory["ramen"])) xalign 0.5 yoffset -3 color "#aaaaaa" size 15 xsize 560

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["golden_ramen"] > 0 and not animal_gifted["goat"]["golden_ramen"])
                    action Function(do_gift_task, "goat", "golden_ramen")
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    if animal_gifted["goat"]["golden_ramen"]:
                        text "Gifted!" xalign 0.5 color "#33ff33" size 22 xsize 560
                    else:
                        hbox:
                            xalign 0.5
                            yoffset 9
                            spacing 8
                            add "images/Maps/Market/golden_ramen.png" xsize 30 ysize 30 yalign 0.5
                            text "Golden Ramen" xalign 0.5 color "#ffffff" size 20 yalign 0.5 xsize 480
                        if player_inventory["golden_ramen"] == 0:
                            text "(Available at the Market)" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                        else:
                            text ("x" + str(player_inventory["golden_ramen"])) xalign 0.5 yoffset -3 color "#aaaaaa" size 15 xsize 560

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_costume:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("goat_costume", "default")]
                text "Default":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26
                if goat_costume == "default":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["g_o_a_t"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("goat_costume", "g_o_a_t")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "G.O.A.T" xalign 0.5 yoffset (9 if player_inventory["g_o_a_t"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["g_o_a_t"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if goat_costume == "g_o_a_t":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["high_noon"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("goat_costume", "high_noon")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "High Noon" xalign 0.5 yoffset (9 if player_inventory["high_noon"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["high_noon"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if goat_costume == "high_noon":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        else:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", True)]
                text "Socialize":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", True)]
                text "Gift":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", True)]
                text "Costume":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

    frame:
        xalign 0.98
        yalign 0.5
        xsize 224
        background "#000000eb"

        vbox:
            xalign 0.5
            spacing 22

            text "Care" xalign 0.5 color "#ffffff" size 28

            imagebutton:
                idle At("images/Maps/Stables/wash.png", tool_scale)
                hover At("images/Maps/Stables/wash_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/wash_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/wash_greyed.png", tool_scale)
                selected (active_care_tool == "wash")
                sensitive (not animal_care["goat"]["washed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "wash",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "wash"))]

            imagebutton:
                idle At("images/Maps/Stables/brush.png", tool_scale)
                hover At("images/Maps/Stables/brush_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/brush_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/brush_greyed.png", tool_scale)
                selected (active_care_tool == "brush")
                sensitive (not animal_care["goat"]["brushed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "brush",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "brush"))]

            imagebutton:
                idle At("images/Maps/Stables/feed.png", tool_scale)
                hover At("images/Maps/Stables/feed_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/feed_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/feed_greyed.png", tool_scale)
                selected (active_care_tool == "feed")
                sensitive (not animal_care["goat"]["fed"] and player_inventory["pumpkin"] > 0)
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "feed",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "feed"))]

            fixed:
                xsize 196
                ysize 80
                if player_inventory["pumpkin"] == 0 and not animal_care["goat"]["fed"]:
                    frame:
                        xsize 196
                        yoffset -70
                        background "#00000090"
                        xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            add "images/Maps/Fields/pumpkin_item.png" xsize 50 ysize 50 yalign 0.5
                            text "Need pumpkin" color "#ff6b6b" size 25 xalign 0.5 yalign 0.65

            imagebutton:
                idle "images/Maps/Stables/stable_door.png"
                hover "images/Maps/Stables/stable_door_hover.png"
                action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "Stables_map")]
                xoffset 35
                yoffset -50

    frame:
        xalign 0.08
        yalign 0.28
        xsize 500
        ysize 120
        background "#000000e7"

        vbox:
            xalign 0.5
            spacing 10

            text "Daisy" xalign 0.5 color "#ffffff" size 26

            hbox:
                xalign 0.5
                spacing 12
                yalign 0.5

                add "images/Maps/Stables/heart.png" xsize 36 ysize 36 yalign 0.5

                fixed:
                    xsize 380
                    ysize 36
                    yalign 0.5

                    bar:
                        xsize 380
                        ysize 36
                        yalign 0.5
                        value animal_care["goat"]["care"]
                        range 100
                        left_bar "#ff6b6b"
                        right_bar "#333333"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 121
                        background "#ffffff"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 244
                        background "#ffffff"

    $ goat_costume_suffix = {"g_o_a_t": "GTC1", "high_noon": "GTC2"}.get(goat_costume)
    if show_care_heart["goat"]:
        add ("images/Maps/Stables/%s_heart.png" % goat_costume_suffix if goat_costume_suffix else "images/Maps/Stables/GT_heart.png") at fit_sprite
        timer 1.0 action Function(reset_care_heart, "goat")
    else:
        add ("images/Sprites/Goat/%s.png" % goat_costume_suffix if goat_costume_suffix else "images/Sprites/Goat/gt_1.png") at fit_sprite

        if active_care_tool != None and animal_hovered["goat"]:
            add ("images/Maps/Stables/%s_hover.png" % goat_costume_suffix if goat_costume_suffix else "images/Maps/Stables/GT_hover.png") at fit_sprite

        button:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 600
            background None
            hovered Function(set_animal_hovered, "goat", True)
            unhovered Function(set_animal_hovered, "goat", False)
            action If(active_care_tool != None,
                true=Function(do_care_task, "goat", active_care_tool),
                false=NullAction())

screen CW_map:
    on "show" action [SetVariable("current_map", "CW_map"), SetVariable("active_care_tool", None), SetVariable("show_socialize", False), SetVariable("show_gift", False), SetVariable("show_costume", False)]
    use quick_menu
    add "images/Backgrounds/Stables/CW_1_blur.jpg"

    $ panel_yalign = 0.65 if (show_socialize or show_gift or show_costume) else 0.5

    vbox:
        xalign 0.02
        yalign panel_yalign
        spacing 45

        if show_socialize:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_gift:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["choco"] > 0 and not animal_gifted["cow"]["choco"])
                    action Function(do_gift_task, "cow", "choco")
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    if animal_gifted["cow"]["choco"]:
                        text "Gifted!" xalign 0.5 color "#33ff33" size 22 xsize 560
                    else:
                        hbox:
                            xalign 0.5
                            yoffset 9
                            spacing 8
                            add "images/Maps/Market/choco.png" xsize 30 ysize 30 yalign 0.5
                            text "Chocolate" xalign 0.5 color "#ffffff" size 20 yalign 0.5 xsize 480
                        if player_inventory["choco"] == 0:
                            text "(Available at the Market)" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                        else:
                            text ("x" + str(player_inventory["choco"])) xalign 0.5 yoffset -3 color "#aaaaaa" size 15 xsize 560

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["golden_choco"] > 0 and not animal_gifted["cow"]["golden_choco"])
                    action Function(do_gift_task, "cow", "golden_choco")
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    if animal_gifted["cow"]["golden_choco"]:
                        text "Gifted!" xalign 0.5 color "#33ff33" size 22 xsize 560
                    else:
                        hbox:
                            xalign 0.5
                            yoffset 9
                            spacing 8
                            add "images/Maps/Market/golden_choco.png" xsize 30 ysize 30 yalign 0.5
                            text "Golden Chocolate" xalign 0.5 color "#ffffff" size 20 yalign 0.5 xsize 480
                        if player_inventory["golden_choco"] == 0:
                            text "(Available at the Market)" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                        else:
                            text ("x" + str(player_inventory["golden_choco"])) xalign 0.5 yoffset -3 color "#aaaaaa" size 15 xsize 560

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_costume:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("cow_costume", "default")]
                text "Default":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26
                if cow_costume == "default":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["life_saver"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("cow_costume", "life_saver")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Life Saver" xalign 0.5 yoffset (9 if player_inventory["life_saver"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["life_saver"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if cow_costume == "life_saver":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["macabre_bovine"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("cow_costume", "macabre_bovine")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Macabre Bovine" xalign 0.5 yoffset (9 if player_inventory["macabre_bovine"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["macabre_bovine"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if cow_costume == "macabre_bovine":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        else:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", True)]
                text "Socialize":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", True)]
                text "Gift":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", True)]
                text "Costume":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

    frame:
        xalign 0.98
        yalign 0.5
        xsize 224
        background "#000000eb"

        vbox:
            xalign 0.5
            spacing 22

            text "Care" xalign 0.5 color "#ffffff" size 28

            imagebutton:
                idle At("images/Maps/Stables/wash.png", tool_scale)
                hover At("images/Maps/Stables/wash_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/wash_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/wash_greyed.png", tool_scale)
                selected (active_care_tool == "wash")
                sensitive (not animal_care["cow"]["washed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "wash",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "wash"))]

            imagebutton:
                idle At("images/Maps/Stables/brush.png", tool_scale)
                hover At("images/Maps/Stables/brush_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/brush_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/brush_greyed.png", tool_scale)
                selected (active_care_tool == "brush")
                sensitive (not animal_care["cow"]["brushed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "brush",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "brush"))]

            imagebutton:
                idle At("images/Maps/Stables/feed.png", tool_scale)
                hover At("images/Maps/Stables/feed_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/feed_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/feed_greyed.png", tool_scale)
                selected (active_care_tool == "feed")
                sensitive (not animal_care["cow"]["fed"] and player_inventory["wheat"] > 0)
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "feed",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "feed"))]

            fixed:
                xsize 196
                ysize 80
                if player_inventory["wheat"] == 0 and not animal_care["cow"]["fed"]:
                    frame:
                        xsize 196
                        yoffset -70
                        background "#00000090"
                        xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            add "images/Maps/Fields/wheat_item.png" xsize 50 ysize 50 yalign 0.5
                            text "Need wheat" color "#ff6b6b" size 25 xalign 0.5 yalign 0.65

            imagebutton:
                idle "images/Maps/Stables/stable_door.png"
                hover "images/Maps/Stables/stable_door_hover.png"
                action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "Stables_map")]
                xoffset 35
                yoffset -50

    frame:
        xalign 0.08
        yalign 0.28
        xsize 500
        ysize 120
        background "#000000e7"

        vbox:
            xalign 0.5
            spacing 10

            text "Annabelle" xalign 0.5 color "#ffffff" size 26

            hbox:
                xalign 0.5
                spacing 12
                yalign 0.5

                add "images/Maps/Stables/heart.png" xsize 36 ysize 36 yalign 0.5

                fixed:
                    xsize 380
                    ysize 36
                    yalign 0.5

                    bar:
                        xsize 380
                        ysize 36
                        yalign 0.5
                        value animal_care["cow"]["care"]
                        range 100
                        left_bar "#ff6b6b"
                        right_bar "#333333"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 121
                        background "#ffffff"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 244
                        background "#ffffff"

    $ cow_costume_suffix = {"life_saver": "CWC1", "macabre_bovine": "CWC2"}.get(cow_costume)
    if show_care_heart["cow"]:
        add ("images/Maps/Stables/%s_heart.png" % cow_costume_suffix if cow_costume_suffix else "images/Maps/Stables/CW_heart.png") at fit_sprite
        timer 1.0 action Function(reset_care_heart, "cow")
    else:
        add ("images/Sprites/Cow/%s.png" % cow_costume_suffix if cow_costume_suffix else "images/Sprites/Cow/cw_1.png") at fit_sprite

        if active_care_tool != None and animal_hovered["cow"]:
            add ("images/Maps/Stables/%s_hover.png" % cow_costume_suffix if cow_costume_suffix else "images/Maps/Stables/CW_hover.png") at fit_sprite

        button:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 600
            background None
            hovered Function(set_animal_hovered, "cow", True)
            unhovered Function(set_animal_hovered, "cow", False)
            action If(active_care_tool != None,
                true=Function(do_care_task, "cow", active_care_tool),
                false=NullAction())

screen BY_map:
    on "show" action [SetVariable("current_map", "BY_map"), SetVariable("active_care_tool", None), SetVariable("show_socialize", False), SetVariable("show_gift", False), SetVariable("show_costume", False)]
    use quick_menu
    add "images/Backgrounds/Stables/BY_1_blur.jpg"

    $ panel_yalign = 0.65 if (show_socialize or show_gift or show_costume) else 0.5

    vbox:
        xalign 0.02
        yalign panel_yalign
        spacing 45

        if show_socialize:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_gift:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_costume:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("bunny_costume", "default")]
                text "Default":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26
                if bunny_costume == "default":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["hoops_hopper"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("bunny_costume", "hoops_hopper")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Hoops Hopper" xalign 0.5 yoffset (9 if player_inventory["hoops_hopper"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["hoops_hopper"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if bunny_costume == "hoops_hopper":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["gala_glamour"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("bunny_costume", "gala_glamour")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Gala Glamour" xalign 0.5 yoffset (9 if player_inventory["gala_glamour"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["gala_glamour"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if bunny_costume == "gala_glamour":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        else:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", True)]
                text "Socialize":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Gift":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", True)]
                text "Costume":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

    frame:
        xalign 0.98
        yalign 0.5
        xsize 224
        background "#000000eb"

        vbox:
            xalign 0.5
            spacing 22

            text "Care" xalign 0.5 color "#ffffff" size 28

            imagebutton:
                idle At("images/Maps/Stables/wash.png", tool_scale)
                hover At("images/Maps/Stables/wash_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/wash_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/wash_greyed.png", tool_scale)
                selected (active_care_tool == "wash")
                sensitive (not animal_care["bunny"]["washed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "wash",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "wash"))]

            imagebutton:
                idle At("images/Maps/Stables/brush.png", tool_scale)
                hover At("images/Maps/Stables/brush_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/brush_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/brush_greyed.png", tool_scale)
                selected (active_care_tool == "brush")
                sensitive (not animal_care["bunny"]["brushed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "brush",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "brush"))]

            imagebutton:
                idle At("images/Maps/Stables/feed.png", tool_scale)
                hover At("images/Maps/Stables/feed_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/feed_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/feed_greyed.png", tool_scale)
                selected (active_care_tool == "feed")
                sensitive (not animal_care["bunny"]["fed"] and player_inventory["carrot"] > 0)
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "feed",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "feed"))]

            fixed:
                xsize 196
                ysize 80
                if player_inventory["carrot"] == 0 and not animal_care["bunny"]["fed"]:
                    frame:
                        xsize 196
                        yoffset -70
                        background "#00000090"
                        xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            add "images/Maps/Fields/carrot_item.png" xsize 50 ysize 50 yalign 0.5
                            text "Need carrot" color "#ff6b6b" size 25 xalign 0.5 yalign 0.65

            imagebutton:
                idle "images/Maps/Stables/stable_door.png"
                hover "images/Maps/Stables/stable_door_hover.png"
                action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "Stables_map")]
                xoffset 35
                yoffset -50

    frame:
        xalign 0.08
        yalign 0.28
        xsize 500
        ysize 120
        background "#000000e7"

        vbox:
            xalign 0.5
            spacing 10

            text "Bunny" xalign 0.5 color "#ffffff" size 26  # <-- update with your bunny's name

            hbox:
                xalign 0.5
                spacing 12
                yalign 0.5

                add "images/Maps/Stables/heart.png" xsize 36 ysize 36 yalign 0.5

                fixed:
                    xsize 380
                    ysize 36
                    yalign 0.5

                    bar:
                        xsize 380
                        ysize 36
                        yalign 0.5
                        value animal_care["bunny"]["care"]
                        range 100
                        left_bar "#ff6b6b"
                        right_bar "#333333"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 121
                        background "#ffffff"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 244
                        background "#ffffff"

    $ bunny_costume_suffix = {"hoops_hopper": "BYC1", "gala_glamour": "BYC2"}.get(bunny_costume)
    if show_care_heart["bunny"]:
        add ("images/Maps/Stables/%s_heart.png" % bunny_costume_suffix if bunny_costume_suffix else "images/Maps/Stables/BY_heart.png") at fit_sprite
        timer 1.0 action Function(reset_care_heart, "bunny")
    else:
        add ("images/Sprites/Bunny/%s.png" % bunny_costume_suffix if bunny_costume_suffix else "images/Sprites/Bunny/by_1.png") at fit_sprite

        if active_care_tool != None and animal_hovered["bunny"]:
            add ("images/Maps/Stables/%s_hover.png" % bunny_costume_suffix if bunny_costume_suffix else "images/Maps/Stables/BY_hover.png") at fit_sprite

        button:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 600
            background None
            hovered Function(set_animal_hovered, "bunny", True)
            unhovered Function(set_animal_hovered, "bunny", False)
            action If(active_care_tool != None,
                true=Function(do_care_task, "bunny", active_care_tool),
                false=NullAction())

screen CT_map:
    on "show" action [SetVariable("current_map", "CT_map"), SetVariable("active_care_tool", None), SetVariable("show_socialize", False), SetVariable("show_gift", False), SetVariable("show_costume", False)]
    use quick_menu
    add "images/Backgrounds/House/CT_1_blur.jpg"

    $ panel_yalign = 0.65 if (show_socialize or show_gift or show_costume) else 0.5

    vbox:
        xalign 0.02
        yalign panel_yalign
        spacing 45

        if show_socialize:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_gift:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_costume:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("cat_costume", "default")]
                text "Default":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26
                if cat_costume == "default":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["bye_bye_clitty"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("cat_costume", "bye_bye_clitty")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Bye Bye Clitty" xalign 0.5 yoffset (9 if player_inventory["bye_bye_clitty"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["bye_bye_clitty"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if cat_costume == "bye_bye_clitty":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["katnip_kraver"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("cat_costume", "katnip_kraver")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Katnip Kraver" xalign 0.5 yoffset (9 if player_inventory["katnip_kraver"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["katnip_kraver"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if cat_costume == "katnip_kraver":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        else:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", True)]
                text "Socialize":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Gift":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", True)]
                text "Costume":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

    frame:
        xalign 0.98
        yalign 0.5
        xsize 224
        background "#000000eb"

        vbox:
            xalign 0.5
            spacing 22

            text "Care" xalign 0.5 color "#ffffff" size 28

            imagebutton:
                idle At("images/Maps/Stables/wash.png", tool_scale)
                hover At("images/Maps/Stables/wash_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/wash_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/wash_greyed.png", tool_scale)
                selected (active_care_tool == "wash")
                sensitive (not animal_care["cat"]["washed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "wash",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "wash"))]

            imagebutton:
                idle At("images/Maps/Stables/brush.png", tool_scale)
                hover At("images/Maps/Stables/brush_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/brush_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/brush_greyed.png", tool_scale)
                selected (active_care_tool == "brush")
                sensitive (not animal_care["cat"]["brushed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "brush",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "brush"))]

            imagebutton:
                idle At("images/Maps/Stables/feed.png", tool_scale)
                hover At("images/Maps/Stables/feed_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/feed_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/feed_greyed.png", tool_scale)
                selected (active_care_tool == "feed")
                sensitive (not animal_care["cat"]["fed"] and player_inventory["fish"] > 0)
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "feed",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "feed"))]

            fixed:
                xsize 196
                ysize 80
                if player_inventory["fish"] == 0 and not animal_care["cat"]["fed"]:
                    frame:
                        xsize 196
                        yoffset -70
                        background "#00000090"
                        xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            add "images/Maps/Market/fish_item.png" xsize 50 ysize 50 yalign 0.5
                            text "Need fish" color "#ff6b6b" size 25 xalign 0.5 yalign 0.65

            imagebutton:
                idle "images/Maps/Stables/stable_door.png"
                hover "images/Maps/Stables/stable_door_hover.png"
                action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "FHhallway_map")]
                xoffset 35
                yoffset -50

    frame:
        xalign 0.08
        yalign 0.28
        xsize 500
        ysize 120
        background "#000000e7"

        vbox:
            xalign 0.5
            spacing 10

            text "Misty" xalign 0.5 color "#ffffff" size 26

            hbox:
                xalign 0.5
                spacing 12
                yalign 0.5

                add "images/Maps/Stables/heart.png" xsize 36 ysize 36 yalign 0.5

                fixed:
                    xsize 380
                    ysize 36
                    yalign 0.5

                    bar:
                        xsize 380
                        ysize 36
                        yalign 0.5
                        value animal_care["cat"]["care"]
                        range 100
                        left_bar "#ff6b6b"
                        right_bar "#333333"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 121
                        background "#ffffff"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 244
                        background "#ffffff"

    $ cat_costume_suffix = {"bye_bye_clitty": "CTC1", "katnip_kraver": "CTC2"}.get(cat_costume)
    if show_care_heart["cat"]:
        add ("images/Maps/Stables/%s_heart.png" % cat_costume_suffix if cat_costume_suffix else "images/Maps/Stables/CT_heart.png") at fit_sprite
        timer 1.0 action Function(reset_care_heart, "cat")
    else:
        add ("images/Sprites/Cat/%s.png" % cat_costume_suffix if cat_costume_suffix else "images/Sprites/Cat/ct_2.png") at fit_sprite

        if active_care_tool != None and animal_hovered["cat"]:
            add ("images/Maps/Stables/%s_hover.png" % cat_costume_suffix if cat_costume_suffix else "images/Maps/Stables/CT_hover.png") at fit_sprite

        button:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 600
            background None
            hovered Function(set_animal_hovered, "cat", True)
            unhovered Function(set_animal_hovered, "cat", False)
            action If(active_care_tool != None,
                true=Function(do_care_task, "cat", active_care_tool),
                false=NullAction())

screen DG_map:
    on "show" action [SetVariable("current_map", "DG_map"), SetVariable("active_care_tool", None), SetVariable("show_socialize", False), SetVariable("show_gift", False), SetVariable("show_costume", False)]
    use quick_menu
    add "images/Backgrounds/House/DG_1_blur.jpg"

    $ panel_yalign = 0.65 if (show_socialize or show_gift or show_costume) else 0.5

    vbox:
        xalign 0.02
        yalign panel_yalign
        spacing 45

        if show_socialize:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_gift:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_costume:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("dog_costume", "default")]
                text "Default":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26
                if dog_costume == "default":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["sexual_dogma"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("dog_costume", "sexual_dogma")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Sexual Dogma" xalign 0.5 yoffset (9 if player_inventory["sexual_dogma"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["sexual_dogma"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if dog_costume == "sexual_dogma":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["best_in_show"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("dog_costume", "best_in_show")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Best in Show" xalign 0.5 yoffset (9 if player_inventory["best_in_show"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["best_in_show"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if dog_costume == "best_in_show":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        else:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", True)]
                text "Socialize":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Gift":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", True)]
                text "Costume":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

    frame:
        xalign 0.98
        yalign 0.5
        xsize 224
        background "#000000eb"

        vbox:
            xalign 0.5
            spacing 22

            text "Care" xalign 0.5 color "#ffffff" size 28

            imagebutton:
                idle At("images/Maps/Stables/wash.png", tool_scale)
                hover At("images/Maps/Stables/wash_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/wash_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/wash_greyed.png", tool_scale)
                selected (active_care_tool == "wash")
                sensitive (not animal_care["dog"]["washed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "wash",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "wash"))]

            imagebutton:
                idle At("images/Maps/Stables/brush.png", tool_scale)
                hover At("images/Maps/Stables/brush_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/brush_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/brush_greyed.png", tool_scale)
                selected (active_care_tool == "brush")
                sensitive (not animal_care["dog"]["brushed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "brush",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "brush"))]

            imagebutton:
                idle At("images/Maps/Stables/feed.png", tool_scale)
                hover At("images/Maps/Stables/feed_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/feed_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/feed_greyed.png", tool_scale)
                selected (active_care_tool == "feed")
                sensitive (not animal_care["dog"]["fed"] and player_inventory["steak"] > 0)
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "feed",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "feed"))]

            fixed:
                xsize 196
                ysize 80
                if player_inventory["steak"] == 0 and not animal_care["dog"]["fed"]:
                    frame:
                        xsize 196
                        yoffset -70
                        background "#00000090"
                        xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            add "images/Maps/Market/steak_item.png" xsize 50 ysize 50 yalign 0.5
                            text "Need steak" color "#ff6b6b" size 25 xalign 0.5 yalign 0.65

            imagebutton:
                idle "images/Maps/Stables/stable_door.png"
                hover "images/Maps/Stables/stable_door_hover.png"
                action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "FHhallway_map")]
                xoffset 35
                yoffset -50

    frame:
        xalign 0.08
        yalign 0.28
        xsize 500
        ysize 120
        background "#000000e7"

        vbox:
            xalign 0.5
            spacing 10

            text "Millie" xalign 0.5 color "#ffffff" size 26

            hbox:
                xalign 0.5
                spacing 12
                yalign 0.5

                add "images/Maps/Stables/heart.png" xsize 36 ysize 36 yalign 0.5

                fixed:
                    xsize 380
                    ysize 36
                    yalign 0.5

                    bar:
                        xsize 380
                        ysize 36
                        yalign 0.5
                        value animal_care["dog"]["care"]
                        range 100
                        left_bar "#ff6b6b"
                        right_bar "#333333"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 121
                        background "#ffffff"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 244
                        background "#ffffff"

    $ dog_costume_suffix = {"sexual_dogma": "DGC1", "best_in_show": "DGC2"}.get(dog_costume)
    if show_care_heart["dog"]:
        add ("images/Maps/Stables/%s_heart.png" % dog_costume_suffix if dog_costume_suffix else "images/Maps/Stables/DG_heart.png") at fit_sprite
        timer 1.0 action Function(reset_care_heart, "dog")
    else:
        add ("images/Sprites/Dog/%s.png" % dog_costume_suffix if dog_costume_suffix else "images/Sprites/Dog/dg_1.png") at fit_sprite

        if active_care_tool != None and animal_hovered["dog"]:
            add ("images/Maps/Stables/%s_hover.png" % dog_costume_suffix if dog_costume_suffix else "images/Maps/Stables/DG_hover.png") at fit_sprite

        button:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 600
            background None
            hovered Function(set_animal_hovered, "dog", True)
            unhovered Function(set_animal_hovered, "dog", False)
            action If(active_care_tool != None,
                true=Function(do_care_task, "dog", active_care_tool),
                false=NullAction())

screen ME_map:
    on "show" action [SetVariable("current_map", "ME_map"), SetVariable("active_care_tool", None), SetVariable("show_socialize", False), SetVariable("show_gift", False), SetVariable("show_costume", False)]
    use quick_menu
    add "images/Backgrounds/House/ME_1_blur.jpg"

    $ panel_yalign = 0.65 if (show_socialize or show_gift or show_costume) else 0.5

    vbox:
        xalign 0.02
        yalign panel_yalign
        spacing 45

        if show_socialize:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive True
                    action [Function(renpy.sound.play, audio.click_1), Function(renpy.notify, "This scene is available in the full Patreon release!")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Patreon" xalign 0.5 yoffset 6 color "#ff3333" size 26
                    text "Full Version Only" xalign 0.5 yoffset -3 color "#aaaaaa" size 18

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_gift:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["cheesecake"] > 0 and not animal_gifted["mouse"]["cheesecake"])
                    action Function(do_gift_task, "mouse", "cheesecake")
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    if animal_gifted["mouse"]["cheesecake"]:
                        text "Gifted!" xalign 0.5 color "#33ff33" size 22 xsize 560
                    else:
                        hbox:
                            xalign 0.5
                            yoffset 9
                            spacing 8
                            add "images/Maps/Market/cheesecake.png" xsize 30 ysize 30 yalign 0.5
                            text "Cheesecake" xalign 0.5 color "#ffffff" size 20 yalign 0.5 xsize 480
                        if player_inventory["cheesecake"] == 0:
                            text "(Available at the Market)" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                        else:
                            text ("x" + str(player_inventory["cheesecake"])) xalign 0.5 yoffset -3 color "#aaaaaa" size 15 xsize 560

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["golden_cheesecake"] > 0 and not animal_gifted["mouse"]["golden_cheesecake"])
                    action Function(do_gift_task, "mouse", "golden_cheesecake")
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    if animal_gifted["mouse"]["golden_cheesecake"]:
                        text "Gifted!" xalign 0.5 color "#33ff33" size 22 xsize 560
                    else:
                        hbox:
                            xalign 0.5
                            yoffset 9
                            spacing 8
                            add "images/Maps/Market/golden_cheesecake.png" xsize 30 ysize 30 yalign 0.5
                            text "Golden Cheesecake" xalign 0.5 color "#ffffff" size 20 yalign 0.5 xsize 480
                        if player_inventory["golden_cheesecake"] == 0:
                            text "(Available at the Market)" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                        else:
                            text ("x" + str(player_inventory["golden_cheesecake"])) xalign 0.5 yoffset -3 color "#aaaaaa" size 15 xsize 560

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_costume:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("mouse_costume", "default")]
                text "Default":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26
                if mouse_costume == "default":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["stew_art_little"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("mouse_costume", "stew_art_little")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Stew Art Little" xalign 0.5 yoffset (9 if player_inventory["stew_art_little"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["stew_art_little"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if mouse_costume == "stew_art_little":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["one_blind_mice"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("mouse_costume", "one_blind_mice")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "One Blind Mice" xalign 0.5 yoffset (9 if player_inventory["one_blind_mice"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["one_blind_mice"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if mouse_costume == "one_blind_mice":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        else:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", True)]
                text "Socialize":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", True)]
                text "Gift":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", True)]
                text "Costume":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

    frame:
        xalign 0.98
        yalign 0.5
        xsize 224
        background "#000000eb"

        vbox:
            xalign 0.5
            spacing 22

            text "Care" xalign 0.5 color "#ffffff" size 28

            imagebutton:
                idle At("images/Maps/Stables/wash.png", tool_scale)
                hover At("images/Maps/Stables/wash_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/wash_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/wash_greyed.png", tool_scale)
                selected (active_care_tool == "wash")
                sensitive (not animal_care["mouse"]["washed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "wash",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "wash"))]

            imagebutton:
                idle At("images/Maps/Stables/brush.png", tool_scale)
                hover At("images/Maps/Stables/brush_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/brush_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/brush_greyed.png", tool_scale)
                selected (active_care_tool == "brush")
                sensitive (not animal_care["mouse"]["brushed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "brush",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "brush"))]

            imagebutton:
                idle At("images/Maps/Stables/feed.png", tool_scale)
                hover At("images/Maps/Stables/feed_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/feed_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/feed_greyed.png", tool_scale)
                selected (active_care_tool == "feed")
                sensitive (not animal_care["mouse"]["fed"] and player_inventory["cheese"] > 0)
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "feed",
                    true=SetVariable("active_care_tool", None),
                    false=SetVariable("active_care_tool", "feed"))]

            fixed:
                xsize 196
                ysize 80
                if player_inventory["cheese"] == 0 and not animal_care["mouse"]["fed"]:
                    frame:
                        xsize 196
                        yoffset -70
                        background "#00000090"
                        xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            add "images/Maps/Market/cheese_item.png" xsize 50 ysize 50 yalign 0.5
                            text "Need cheese" color "#ff6b6b" size 25 xalign 0.5 yalign 0.65

            imagebutton:
                idle "images/Maps/Stables/stable_door.png"
                hover "images/Maps/Stables/stable_door_hover.png"
                action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "FHhallway_map")]
                xoffset 35
                yoffset -50

    frame:
        xalign 0.08
        yalign 0.28
        xsize 500
        ysize 120
        background "#000000e7"

        vbox:
            xalign 0.5
            spacing 10

            text "Penny the Mouse" xalign 0.5 color "#ffffff" size 26

            hbox:
                xalign 0.5
                spacing 12
                yalign 0.5

                add "images/Maps/Stables/heart.png" xsize 36 ysize 36 yalign 0.5

                fixed:
                    xsize 380
                    ysize 36
                    yalign 0.5

                    bar:
                        xsize 380
                        ysize 36
                        yalign 0.5
                        value animal_care["mouse"]["care"]
                        range 100
                        left_bar "#ff6b6b"
                        right_bar "#333333"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 121
                        background "#ffffff"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 244
                        background "#ffffff"

    $ mouse_costume_suffix = {"stew_art_little": "MEC1", "one_blind_mice": "MEC2"}.get(mouse_costume)
    if show_care_heart["mouse"]:
        add ("images/Maps/Stables/%s_heart.png" % mouse_costume_suffix if mouse_costume_suffix else "images/Maps/Stables/ME_heart.png") at fit_sprite
        timer 1.0 action Function(reset_care_heart, "mouse")
    else:
        add ("images/Sprites/Mouse/%s.png" % mouse_costume_suffix if mouse_costume_suffix else "images/Sprites/Mouse/me_1.png") at fit_sprite

        if active_care_tool != None and animal_hovered["mouse"]:
            add ("images/Maps/Stables/%s_hover.png" % mouse_costume_suffix if mouse_costume_suffix else "images/Maps/Stables/ME_hover.png") at fit_sprite

        button:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 600
            background None
            hovered Function(set_animal_hovered, "mouse", True)
            unhovered Function(set_animal_hovered, "mouse", False)
            action If(active_care_tool != None,
                true=Function(do_care_task, "mouse", active_care_tool),
                false=NullAction())
screen SP_map:
    on "show" action [SetVariable("current_map", "SP_map"), SetVariable("active_care_tool", None), SetVariable("show_socialize", False), SetVariable("show_gift", False), SetVariable("show_costume", False)]
    use quick_menu
    add "images/Backgrounds/Stables/SP_1_blur.jpg"

    # Interaction panel
    $ panel_yalign = 0.65 if (show_socialize or show_gift or show_costume) else 0.5

    vbox:
        xalign 0.02
        yalign panel_yalign
        spacing 45

        if show_socialize:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_gift:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Coming Soon":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_gift", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        elif show_costume:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("sheep_costume", "default")]
                text "Default":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 26
                if sheep_costume == "default":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["marriage_material"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("sheep_costume", "marriage_material")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Marriage Material" xalign 0.5 yoffset (9 if player_inventory["marriage_material"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["marriage_material"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if sheep_costume == "marriage_material":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive (player_inventory["ein_sheeple"] > 0)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("sheep_costume", "ein_sheeple")]
                vbox:
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    spacing 4
                    text "Ein Sheeple" xalign 0.5 yoffset (9 if player_inventory["ein_sheeple"] == 0 else 0) color "#ffffff" size 20 xsize 560
                    if player_inventory["ein_sheeple"] == 0:
                        text "Available at the Market" xalign 0.5 yoffset -3 color "#aaaaaa" size 14 xsize 560
                if sheep_costume == "ein_sheeple":
                    frame:
                        xsize 40
                        ysize 40
                        xpos 533
                        ypos 69
                        xanchor 0.5
                        yanchor 0.5
                        background "#ffdd00"
                        text "E" xalign 0.5 yalign 0.5 xoffset 2 color "#ffffff" size 24

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", False)]
                text "Back":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

        else:
            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_socialize", True)]
                text "Socialize":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    insensitive "images/Maps/Stables/choice_greyed.png"
                    sensitive False
                    action NullAction()
                text "Gift":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

            fixed:
                xsize 250
                ysize 70
                imagebutton:
                    idle "images/Maps/Stables/choice_idle.png"
                    hover "images/Maps/Stables/choice_hover.png"
                    at Transform(zoom=0.85, xoffset=39)
                    action [Function(renpy.sound.play, audio.click_1), SetVariable("show_costume", True)]
                text "Costume":
                    xpos 335
                    xanchor 0.5
                    ypos 67
                    yanchor 0.5
                    color "#ffffff"
                    size 40

    # Care tool panel
    frame:
        xalign 0.98
        yalign 0.5
        xsize 224
        background "#000000eb"

        vbox:
            xalign 0.5
            spacing 22

            text "Care" xalign 0.5 color "#ffffff" size 28

            imagebutton:
                idle At("images/Maps/Stables/wash.png", tool_scale)
                hover At("images/Maps/Stables/wash_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/wash_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/wash_greyed.png", tool_scale)
                selected (active_care_tool == "wash")
                sensitive (not animal_care["sheep"]["washed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "wash",
                    true=[SetVariable("active_care_tool", None), SetVariable("animal_hovered", dict(animal_hovered, sheep=False))],
                    false=[SetVariable("active_care_tool", "wash"), SetVariable("animal_hovered", dict(animal_hovered, sheep=False))])]

            imagebutton:
                idle At("images/Maps/Stables/brush.png", tool_scale)
                hover At("images/Maps/Stables/brush_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/brush_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/brush_greyed.png", tool_scale)
                selected (active_care_tool == "brush")
                sensitive (not animal_care["sheep"]["brushed"])
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "brush",
                    true=[SetVariable("active_care_tool", None), SetVariable("animal_hovered", dict(animal_hovered, sheep=False))],
                    false=[SetVariable("active_care_tool", "brush"), SetVariable("animal_hovered", dict(animal_hovered, sheep=False))])]

            imagebutton:
                idle At("images/Maps/Stables/feed.png", tool_scale)
                hover At("images/Maps/Stables/feed_hover.png", tool_scale)
                selected_idle At("images/Maps/Stables/feed_hover.png", tool_scale)
                insensitive At("images/Maps/Stables/feed_greyed.png", tool_scale)
                selected (active_care_tool == "feed")
                sensitive (not animal_care["sheep"]["fed"] and player_inventory["beer"] > 0)
                action [Function(renpy.sound.play, audio.click_1), If(active_care_tool == "feed",
                    true=[SetVariable("active_care_tool", None), SetVariable("animal_hovered", dict(animal_hovered, sheep=False))],
                    false=[SetVariable("active_care_tool", "feed"), SetVariable("animal_hovered", dict(animal_hovered, sheep=False))])]

            fixed:
                xsize 196
                ysize 80
                if player_inventory["beer"] == 0 and not animal_care["sheep"]["fed"]:
                    frame:
                        xsize 196
                        yoffset -70
                        background "#00000090"
                        xalign 0.5
                        hbox:
                            spacing 6
                            xalign 0.5
                            add "images/Maps/Market/beer_item.png" xsize 50 ysize 50 yalign 0.5
                            text "Need beer" color "#ff6b6b" size 25 xalign 0.5 yalign 0.65

            imagebutton:
                idle "images/Maps/Stables/stable_door.png"
                hover "images/Maps/Stables/stable_door_hover.png"
                action [Function(renpy.sound.play, audio.door_close), Function(go_to_map, "Stables_map")]
                xoffset 35
                yoffset -50

    # Care meter
    frame:
        xalign 0.08
        yalign 0.28
        xsize 500
        ysize 120
        background "#000000e7"

        vbox:
            xalign 0.5
            spacing 10

            text "Dolly" xalign 0.5 color "#ffffff" size 26

            hbox:
                xalign 0.5
                spacing 12
                yalign 0.5

                add "images/Maps/Stables/heart.png" xsize 36 ysize 36 yalign 0.5

                fixed:
                    xsize 380
                    ysize 36
                    yalign 0.5

                    bar:
                        xsize 380
                        ysize 36
                        yalign 0.5
                        value animal_care["sheep"]["care"]
                        range 100
                        left_bar "#ff6b6b"
                        right_bar "#333333"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 121
                        background "#ffffff"

                    frame:
                        xsize 4
                        ysize 36
                        xoffset 244
                        background "#ffffff"

    # Sprite display
    $ sheep_costume_suffix = {"marriage_material": "SPC1", "ein_sheeple": "SPC2"}.get(sheep_costume)
    if show_care_heart["sheep"]:
        add ("images/Maps/Stables/%s_heart.png" % sheep_costume_suffix if sheep_costume_suffix else "images/Maps/Stables/SP_heart.png") at fit_sprite
        timer 1.0 action Function(reset_care_heart, "sheep")
    else:
        add ("images/Sprites/Sheep/%s.png" % sheep_costume_suffix if sheep_costume_suffix else "images/Sprites/Sheep/sp_1.png") at fit_sprite

        if active_care_tool != None and animal_hovered["sheep"]:
            add ("images/Maps/Stables/%s_hover.png" % sheep_costume_suffix if sheep_costume_suffix else "images/Maps/Stables/SP_hover.png") at fit_sprite

        button:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 600
            background None
            hovered Function(set_animal_hovered, "sheep", True)
            unhovered Function(set_animal_hovered, "sheep", False)
            action If(active_care_tool != None,
                true=Function(do_care_task, "sheep", active_care_tool),
                false=NullAction())

screen character_select():
    add "images/Backgrounds/UI/Char_Select.png"

    text "Choose Your Character":
        xalign 0.455
        yalign 0.05
        color "#ffffff"
        size 55
        underline True

    hbox:
        xalign 0.5
        yalign 0.55
        spacing 40

        # Malik - Gorilla
        fixed:
            xsize 480
            ysize 700

            add "images/Sprites/MC/mc_gorilla.png" xalign 0.0 yalign 0.5 zoom 0.686 xoffset -200 yoffset 60

            button:
                xsize 480
                ysize 400
                xalign 0.05
                yalign 0.6
                xoffset -125
                background "#00000090"
                hover_background "#ffffff30"
                action Return("Malik")

            vbox:
                xsize 480
                xalign 0.5
                yalign 0.75
                xoffset -100
                yoffset -60
                spacing 16

                text "Malik" xalign 0.5 color "#ffffff" size 40
                text "Animal: Gorilla" xalign 0.5 color "#ffdd00" size 24
                text "Penis Size: Girthy" xalign 0.5 color "#ffdd00" size 24

                frame:
                    xsize 250
                    xalign 0.5

                    text "Loves bananas and femboys." color "#aaaaaa" size 18 xalign 0.5

                frame:
                    xsize 440
                    xalign 0.5
                    
                    text "Special Ability: ???" color "#aaaaaa" size 18 xalign 0.5

        # Duke - Bulldog
        fixed:
            xsize 480
            ysize 700

            add "images/Sprites/MC/mc_bear.png" xalign 0.0 yalign 0.5 zoom 0.648 xoffset -40 yoffset 90

            button:
                xsize 480
                ysize 400
                xalign 0.05
                yalign 0.6
                xoffset -5
                yoffset 65
                background "#00000090"
                hover_background "#00000090"
                sensitive False
                action NullAction()

            vbox:
                xsize 480
                xalign 0.5
                yalign 0.6
                spacing 16

                text "King" xalign 0.5 color "#ffffff" size 40
                text "Animal: Polar Bear" xalign 0.5 color "#ffdd00" size 24
                text "Penis Size: Proportional" xalign 0.5 color "#ffdd00" size 24

                frame:
                    xsize 250
                    xalign 0.5

                    text "Coming soon..." color "#aaaaaa" size 18 xalign 0.5

                frame:
                    xsize 440
                    xalign 0.5
                    
                    text "Special Ability: ???" color "#aaaaaa" size 18 xalign 0.5

        # Thunder - Horse
        fixed:
            xsize 480
            ysize 700

            add "images/Sprites/MC/mc_horse.png" xalign 0.85 yalign 0.5 zoom 0.696 xoffset 210 yoffset 60

            button:
                xsize 480
                ysize 400
                xalign 0.05
                yalign 0.6
                xoffset 160
                background "#00000090"
                hover_background "#00000090"
                sensitive False
                action NullAction()

            vbox:
                xsize 480
                xalign 0.5
                yalign 0.75
                xoffset 150
                yoffset -100
                spacing 16

                text "Thunder" xalign 0.5 color "#ffffff" size 40
                text "Animal: Horse" xalign 0.5 color "#ffdd00" size 24
                text "Penis Type: Long" xalign 0.5 color "#ffdd00" size 24

                frame:
                    xsize 250
                    xalign 0.5

                    text "Coming soon..." color "#aaaaaa" size 18 xalign 0.5

                frame:
                    xsize 440
                    xalign 0.5
                    
                    text "Special Ability: ???" color "#aaaaaa" size 18 xalign 0.5

screen day_counter(day):
    zorder 200
    add Movie(play="images/Maps/MC/sleep.webm", loop=False)       # <-- video inside the screen
    text "Day [day]":
        xalign 0.5
        yalign 0.5
        color "#ff0000"
        size 80
        
## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 1.0
            yalign 0.0

            textbutton _("Save") action ShowMenu('save')
            
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("Help") action ShowMenu("help")

        if renpy.variant("pc"):

            ## The quit button is banned on iOS and unnecessary on Android and
            ## Web.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    add gui.main_menu_background

    ## This empty frame darkens the main menu.
    frame:
        style "main_menu_frame"

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    imagebutton:
        idle "images/Icons/picon_idle.png"
        hover "images/Icons/picon_hover.png"
        at Transform(zoom=0.45)
        xalign 0.0
        yalign 1.0
        xoffset 0
        yoffset -30
        action OpenURL("https://www.patreon.com/PluckyPlatypus")

    imagebutton:
        idle "images/Icons/ticon_idle.png"
        hover "images/Icons/ticon_hover.png"
        at Transform(zoom=0.578)
        xalign 0.0
        yalign 1.0
        xoffset 117
        yoffset -4
        action OpenURL("https://x.com/P1ucky_P1atypus")

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")

            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:

                    label _("Text Speed")

                    bar value Preference("text speed")

                    label _("Auto-Forward Time")

                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_voice:
                        label _("Voice Volume")

                        hbox:
                            bar value Preference("voice volume")

                            if config.sample_voice:
                                textbutton _("Test") action Play("voice", config.sample_voice)

                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide, B/Right Button")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900
