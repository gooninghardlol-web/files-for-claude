################################################################################
## Tutorial
##
## Self-contained first-time walkthrough. Penny (me_1) guides the player
## through Farm -> Market -> Fields -> Stables -> Pudding's care loop.
## Every other file only needed two touches to support this: script.rpy's
## label start: calls `tutorial_start` instead of `call screen Farm_map`,
## and screens.rpy gates the specific buttons used below with `sensitive`
## checks and appends step-advance calls to their existing actions.
##
## tutorial_overlay is registered as an overlay screen (same mechanism as
## quick_menu in screens.rpy), so it always draws on top of whatever map
## screen is currently shown without needing a `use` statement added to
## each map screen individually.
################################################################################

default tutorial_active = False
default tutorial_step = "farm_intro"

define DEBUG_SKIP_TUTORIAL = False  # <-- set back to False to re-enable the tutorial

transform tutorial_portrait:
    zoom 0.22

define audio.complete = "audio/complete.wav"

init python:
    config.overlay_screens.append("tutorial_overlay")
    renpy.music.register_channel("tutorial_sfx", mixer="sfx", loop=False)  # <-- separate from "sound" so it doesn't cut off the seed/water sfx firing on the same click

    TUTORIAL_TEXT = {
        "farm_intro":        "Welcome to your new farm! Let's go see if we can get some seeds\nso we can start planting for the season. Head over to the Market.",
        "market_intro":      "This is Harriet's Market. Here you can buy any farm goods you might need.\nHarriet will also buy your crops for cold hard cash to keep your farm churning.",
        "market_seeds":      "Here, take these — five wheat seeds to get you started.",
        "market_return":     "Alright, let's head back to the farm.\nClick the {color=#4caf50}farm icon{/color} in the top left of the screen to go home.",
        "farm_to_fields":    "Now let's get you planting. Click on the Fields.",
        "fields_pick_tool":  "Grab your seed bag from the tool rack.",
        "fields_pick_seed":  "Pick the wheat seeds — that's what we've got.",
        "fields_plant":      "Now plant all 5 wheat seeds — just click a plot for each one.",
        "fields_pick_water": "Good. Now grab the watering can.",
        "fields_water_plot": "Water each of those 5 plots to help them grow.",
        "fields_die_info":   "Water every plot daily — miss a day and the crop dies,\nso don't slack off.",
        "fields_pick_scythe": "See that corn up in the corner, fully grown?\nLet's harvest it — grab the scythe.",
        "fields_harvest_click": "Now click that corn to harvest it.",
        "fields_harvest_done": "Nice! Take a look up top — we've got one corn now.",
        "fields_pick_hoe":    "That other plot's got a dead plant on it.\nLet's clear it out — grab the hoe.",
        "fields_hoe_click":   "Click that plot to clear it.",
        "fields_hoe_done":    "Good as new. Let's head back to the farm.",
        "fields_return":     "Click the {color=#4caf50}farm icon{/color} in the top left of the screen to head home.",
        "farm_to_stables":   "Now let's go check on the animals. Click on the Stables.",
        "stables_info":      "The animals in the stables and farmhouse need your care.",
        "stables_info_2":    "Any care you show boosts their affection — but skip a day\nand it dips a little, so stay consistent.",
        "stables_info_3":    "One thing though: once affection hits 33%, 66%, or 100%,\nit'll never drop below that mark again.",
        "stables_pg_door":   "Let's start with Pudding. Click on the door with the pig icon.",
        "pg_intro":          "This is the animal care screen for Pudding's stable.\nHere you can take care of Pudding and show them how much you care for them.",
        "pg_wash_tool":      "Grab the wash bucket.",
        "pg_wash_click":     "Now click on Pudding to wash him.",
        "pg_brush_tool":     "See that heart? He liked that. Now try the brush.",
        "pg_brush_click":    "Click on Pudding to brush him.",
        "pg_feed_tool":      "Nice! Now let's feed him —\nfeeding boosts affection more than washing or brushing.",
        "pg_feed_click":     "Click on Pudding to feed him.",
        "stables_return":    "Great work with Pudding! Click the {color=#4caf50}farm icon{/color} in the top left of the screen to head home.",
        "farm_to_house":     "Now let's get you settled in. Click on the farmhouse.",
        "house_intro":       "Other animals live here too, but your bedroom's the door on the right.",
        "house_pick_room":   "Go ahead and click your bedroom to head inside.",
        "mc_bed_click":      "That's your bed. Clicking it ends the day and starts a new one\n— go ahead and give it a try.",
        "tutorial_done":     "You've got the hang of it now. The rest of the farm's yours — good luck!",
    }

    ## step -> next step for "narration" beats, where progress is a "Got it"
    ## click rather than a real game action. Value None ends the tutorial.
    TUTORIAL_NARRATION = {
        "market_intro":        "market_seeds",
        "market_seeds":        "market_return",
        "fields_die_info":     "fields_pick_scythe",
        "fields_harvest_done": "fields_pick_hoe",
        "fields_hoe_done":     "fields_return",
        "stables_info":        "stables_info_2",
        "stables_info_2":      "stables_info_3",
        "stables_info_3":      "stables_pg_door",
        "pg_intro":            "pg_wash_tool",
        "house_intro":         "house_pick_room",
        "tutorial_done":       None,
    }

    ## Two plots in the fields are pre-staged for the harvest/hoe steps below.
    TUTORIAL_CORN_PLOT = 8   # upper-right area: fully grown corn, ready to harvest
    TUTORIAL_DEAD_PLOT = 9   # upper-right area: dead plant, ready to be cleared

    def tutorial_target(step):
        ## True if this element is the one thing the player should click right now.
        return (not store.tutorial_active) or (store.tutorial_step == step)

    def tutorial_target_any(*steps):
        return (not store.tutorial_active) or (store.tutorial_step in steps)

    def tutorial_locked_out():
        ## For buttons that are never part of the tutorial script.
        return not store.tutorial_active

    def tutorial_advance_if(current_step, next_step):
        if store.tutorial_active and store.tutorial_step == current_step:
            store.tutorial_step = next_step

    def grant_tutorial_seeds():
        store.player_inventory["wheat_seed"] += 5

    def tutorial_go_home():
        if store.tutorial_step == "market_return":
            store.tutorial_step = "farm_to_fields"
        elif store.tutorial_step == "fields_return":
            store.tutorial_step = "farm_to_stables"
        elif store.tutorial_step == "stables_return":
            store.tutorial_step = "farm_to_house"

    def tutorial_setup_fields():
        if not (store.tutorial_active and store.tutorial_step == "farm_to_fields"):
            return
        corn_plot = store.farm_plots[TUTORIAL_CORN_PLOT]
        corn_plot["state"] = "max"
        corn_plot["crop"] = "corn"
        dead_plot = store.farm_plots[TUTORIAL_DEAD_PLOT]
        dead_plot["state"] = "dead"
        dead_plot["crop"] = None

    def tutorial_plot_sensitive(i):
        ## Keeps the player from planting/watering the two staged plots, and
        ## from touching any plot but the intended one during harvest/hoe.
        if not store.tutorial_active:
            return True
        step = store.tutorial_step
        if step in ("fields_plant", "fields_water_plot"):
            return i not in (TUTORIAL_CORN_PLOT, TUTORIAL_DEAD_PLOT)
        if step == "fields_harvest_click":
            return i == TUTORIAL_CORN_PLOT
        if step == "fields_hoe_click":
            return i == TUTORIAL_DEAD_PLOT
        return False

    def tutorial_count_wheat_planted():
        return sum(1 for p in store.farm_plots if p.get("crop") == "wheat")

    def tutorial_count_wheat_watered():
        return sum(1 for p in store.farm_plots
                    if p.get("crop") == "wheat" and p.get("water_day") == store.in_game_day)

    def tutorial_check_plot(i):
        step = store.tutorial_step
        if step == "fields_plant" and tutorial_count_wheat_planted() >= 5:
            renpy.sound.play(audio.complete, channel="tutorial_sfx")
            tutorial_advance_if("fields_plant", "fields_pick_water")
        elif step == "fields_water_plot" and tutorial_count_wheat_watered() >= 5:
            renpy.sound.play(audio.complete, channel="tutorial_sfx")
            tutorial_advance_if("fields_water_plot", "fields_die_info")
        elif step == "fields_harvest_click" and i == TUTORIAL_CORN_PLOT and store.farm_plots[i]["state"] == "dry":
            tutorial_advance_if("fields_harvest_click", "fields_harvest_done")
        elif step == "fields_hoe_click" and i == TUTORIAL_DEAD_PLOT and store.farm_plots[i]["state"] == "dry":
            tutorial_advance_if("fields_hoe_click", "fields_hoe_done")

    def tutorial_check_pig_care():
        care = store.animal_care["pig"]
        if care["washed"]:
            tutorial_advance_if("pg_wash_click", "pg_brush_tool")
        if care["brushed"]:
            if store.tutorial_active and store.tutorial_step == "pg_brush_click":
                store.player_inventory["corn"] += 1                  # <-- silently stocked for the feed step below
            tutorial_advance_if("pg_brush_click", "pg_feed_tool")
        if care["fed"]:
            tutorial_advance_if("pg_feed_click", "stables_return")

    def tutorial_narration_continue():
        if store.tutorial_step == "market_intro":
            grant_tutorial_seeds()
        next_step = TUTORIAL_NARRATION.get(store.tutorial_step)
        if next_step is None:
            store.tutorial_active = False
        else:
            store.tutorial_step = next_step
        renpy.restart_interaction()


screen tutorial_overlay():
    zorder 95

    if tutorial_active and tutorial_step in TUTORIAL_TEXT:
        $ tutorial_is_narration = tutorial_step in TUTORIAL_NARRATION

        mousearea:
            xpos 360
            xanchor 0.0
            yalign 0.98
            xsize 1260
            ysize 150
            hovered SetVariable("default_mouse", "default")
            unhovered Function(restore_tool_cursor)

        button:
            xpos 360
            xanchor 0.0
            yalign 0.98
            xsize 1260
            ysize 150
            background "#000000d0"
            hover_background ("#0000009a" if tutorial_is_narration else "#000000d0")
            action (Function(tutorial_narration_continue) if tutorial_is_narration else NullAction())

            hbox:
                xalign 0.5
                yalign 0.5
                spacing 24

                add "me_1" at tutorial_portrait yalign 1.0

                vbox:
                    xsize 950
                    yalign 0.5
                    spacing 6

                    text TUTORIAL_TEXT[tutorial_step]:
                        xsize 950
                        color "#ffffff"
                        size 24

                    if tutorial_is_narration:
                        text "(click to continue)":
                            color "#ffdd00"
                            size 16


label tutorial_start:
    play music audio.main_music
    if DEBUG_SKIP_TUTORIAL:
        call screen Farm_map
        return
    $ tutorial_active = True
    $ tutorial_step = "farm_intro"
    call screen Farm_map
    return
