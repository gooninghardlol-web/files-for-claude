default player_character = None                                    # <-- tracks chosen character
default farm_plots = [{"state": "dry", "crop": None, "water_day": -1} for _ in range(30)]
default active_tool = None
default selected_seed = None
default in_game_day = 0
default harvest_flyers = []
default bio_character = "pig"
default scene_viewed = {
    "pig":   [False, False, False],
    "goat":  [False, False, False],
    "cow":   [False, False, False],
    "mouse": [False, False, False],
}
default counter_pulse = {"apple": False, "carrot": False, "wheat": False, "corn": False, "pumpkin": False}
default player_inventory = {"apple": 0, "carrot": 0, "wheat": 0, "corn": 0, "pumpkin": 0, "apple_seed": 0, "carrot_seed": 0, "wheat_seed": 0, "corn_seed": 0, "pumpkin_seed": 0, "fish": 0, "steak": 0, "cheese": 0, "beer": 0, "truffle": 0, "golden_truffle": 0, "piggy_icon": 0, "stars_stripes": 0, "g_o_a_t": 0, "high_noon": 0, "life_saver": 0, "macabre_bovine": 0, "stew_art_little": 0, "one_blind_mice": 0, "tractor": 0, "sprinkler": 0, "horse_pill": 0, "peg_is_sus": 0, "marriage_material": 0, "ein_sheeple": 0, "hoops_hopper": 0, "gala_glamour": 0, "bye_bye_clitty": 0, "katnip_kraver": 0, "sexual_dogma": 0, "best_in_show": 0, "ramen": 0, "golden_ramen": 0, "choco": 0, "golden_choco": 0, "cheesecake": 0, "golden_cheesecake": 0}  # <-- crop counts are harvested food; *_seed counts are separate, plantable-only
default current_map = None
default player_gold = 25
default market_tab = "buy"
default market_buy_category = "seeds"
default show_socialize = False  
default show_gift = False                                    # <-- new
default show_costume = False
default pig_costume = "default"
default horse_costume = "default"
default goat_costume = "default"
default cow_costume = "default"
default bunny_costume = "default"
default cat_costume = "default"
default dog_costume = "default"
default mouse_costume = "default"
default sheep_costume = "default"
default default_mouse = "default"                                  # <-- Ren'Py's built in cursor variable
default show_water_anim = False                                    # <-- for click animation
default show_care_heart = {                                         # <-- changed from single bool to dict
    "horse": False,
    "cow":   False,
    "pig":   False,
    "goat":  False,
    "mouse": False,
    "cat":   False,
    "dog":   False,
    "bunny": False,
    "sheep": False,
}
default animal_hovered = {
    "horse": False,
    "cow":   False,
    "pig":   False,
    "goat":  False,
    "mouse": False,
    "cat":   False,
    "dog":   False,
    "bunny": False,
    "sheep": False,
}
default market_buy = [
    {"id": "wheat_seed",   "label": "Wheat Seeds",   "price": 5,   "image": "images/Maps/Fields/wheat_seed.png",   "gives": "seeds", "crop": "wheat_seed",   "category": "seeds"},
    {"id": "corn_seed",    "label": "Corn Seeds",    "price": 15,  "image": "images/Maps/Fields/corn_seed.png",    "gives": "seeds", "crop": "corn_seed",    "category": "seeds"},
    {"id": "carrot_seed",  "label": "Carrot Seeds",  "price": 25,  "image": "images/Maps/Fields/carrot_seed.png",  "gives": "seeds", "crop": "carrot_seed",  "category": "seeds"},
    {"id": "pumpkin_seed", "label": "Pumpkin Seeds", "price": 50,  "image": "images/Maps/Fields/pumpkin_seed.png", "gives": "seeds", "crop": "pumpkin_seed", "category": "seeds"},
    {"id": "apple_seed",   "label": "Apple Seeds",   "price": 250, "image": "images/Maps/Fields/apple_seed.png",   "gives": "seeds", "crop": "apple_seed",   "category": "seeds"},
    {"id": "wheat",        "label": "Wheat",         "price": 20,  "image": "images/Maps/Fields/wheat_item.png",   "gives": "item",  "crop": "wheat",   "category": "food"},
    {"id": "corn",         "label": "Corn",          "price": 45,  "image": "images/Maps/Fields/corn_item.png",    "gives": "item",  "crop": "corn",    "category": "food"},
    {"id": "carrot",       "label": "Carrot",        "price": 70,  "image": "images/Maps/Fields/carrot_item.png",  "gives": "item",  "crop": "carrot",  "category": "food"},
    {"id": "pumpkin",      "label": "Pumpkin",       "price": 125, "image": "images/Maps/Fields/pumpkin_item.png", "gives": "item",  "crop": "pumpkin", "category": "food"},
    {"id": "apple",        "label": "Apple",         "price": 400, "image": "images/Maps/Fields/apple_item.png",   "gives": "item",  "crop": "apple",   "category": "food"},
    {"id": "fish",         "label": "Fish",          "price": 60,  "image": "images/Maps/Market/fish_item.png",    "gives": "item",  "crop": "fish",    "category": "food"},    # <-- new
    {"id": "steak",        "label": "Steak",         "price": 80,  "image": "images/Maps/Market/steak_item.png",   "gives": "item",  "crop": "steak",   "category": "food"},   # <-- new
    {"id": "cheese",       "label": "Cheese",        "price": 40,  "image": "images/Maps/Market/cheese_item.png",  "gives": "item",  "crop": "cheese",  "category": "food"},
    {"id": "beer",         "label": "Beer",          "price": 70,  "image": "images/Maps/Market/beer_item.png",    "gives": "item",  "crop": "beer",    "category": "food"},
    {"id": "truffle",        "label": "Truffle",        "price": 150, "image": "images/Maps/Market/truffle_item.png",        "gives": "item", "crop": "truffle",        "category": "food"},
    {"id": "golden_truffle", "label": "Golden Truffle", "price": 500, "image": "images/Maps/Market/golden_truffle_item.png", "gives": "item", "crop": "golden_truffle", "category": "food"},  # <-- new
    {"id": "ramen",             "label": "Ramen",             "price": 150, "image": "images/Maps/Market/ramen.png",             "gives": "item", "crop": "ramen",             "category": "food"},  # <-- new
    {"id": "golden_ramen",      "label": "Golden Ramen",      "price": 500, "image": "images/Maps/Market/golden_ramen.png",      "gives": "item", "crop": "golden_ramen",      "category": "food"},  # <-- new
    {"id": "choco",             "label": "Chocolate",         "price": 150, "image": "images/Maps/Market/choco.png",             "gives": "item", "crop": "choco",             "category": "food"},  # <-- new
    {"id": "golden_choco",      "label": "Golden Chocolate",  "price": 500, "image": "images/Maps/Market/golden_choco.png",      "gives": "item", "crop": "golden_choco",      "category": "food"},  # <-- new
    {"id": "cheesecake",        "label": "Cheesecake",        "price": 150, "image": "images/Maps/Market/cheesecake.png",        "gives": "item", "crop": "cheesecake",        "category": "food"},  # <-- new
    {"id": "golden_cheesecake", "label": "Golden Cheesecake", "price": 500, "image": "images/Maps/Market/golden_cheesecake.png", "gives": "item", "crop": "golden_cheesecake", "category": "food"},  # <-- new
    {"id": "piggy_icon",     "label": "Piggy Icon Costume", "price": 1000, "image": "images/Icons/PGC1.png",                "gives": "item", "crop": "piggy_icon",     "category": "costumes"},  # <-- new costume
    {"id": "stars_stripes",  "label": "Stars 'N' Stripes Costume", "price": 1000, "image": "images/Icons/PGC2.png",        "gives": "item", "crop": "stars_stripes",  "category": "costumes"},  # <-- new costume
    {"id": "g_o_a_t",        "label": "G.O.A.T Costume",           "price": 1000, "image": "images/Icons/GTC1.png",        "gives": "item", "crop": "g_o_a_t",        "category": "costumes"},  # <-- new costume
    {"id": "high_noon",      "label": "High Noon Costume",         "price": 1000, "image": "images/Icons/GTC2.png",        "gives": "item", "crop": "high_noon",      "category": "costumes"},  # <-- new costume
    {"id": "life_saver",     "label": "Life Saver Costume",        "price": 1000, "image": "images/Icons/CWC1.png",        "gives": "item", "crop": "life_saver",     "category": "costumes"},  # <-- new costume
    {"id": "macabre_bovine", "label": "Macabre Bovine Costume",    "price": 1000, "image": "images/Icons/CWC2.png",        "gives": "item", "crop": "macabre_bovine", "category": "costumes"},  # <-- new costume
    {"id": "stew_art_little", "label": "Stew Art Little Costume",  "price": 1000, "image": "images/Icons/MEC1.png",        "gives": "item", "crop": "stew_art_little", "category": "costumes"},  # <-- new costume
    {"id": "one_blind_mice",  "label": "One Blind Mice Costume",   "price": 1000, "image": "images/Icons/MEC2.png",        "gives": "item", "crop": "one_blind_mice",  "category": "costumes"},  # <-- new costume
    {"id": "horse_pill",        "label": "Horse Pill Costume",        "price": 1000, "image": "images/Icons/HEC1.png", "gives": "item", "crop": "horse_pill",        "category": "costumes"},  # <-- new costume
    {"id": "peg_is_sus",        "label": "Peg is Sus? Costume",       "price": 1000, "image": "images/Icons/HEC2.png", "gives": "item", "crop": "peg_is_sus",        "category": "costumes"},  # <-- new costume
    {"id": "marriage_material", "label": "Marriage Material Costume", "price": 1000, "image": "images/Icons/SPC1.png", "gives": "item", "crop": "marriage_material", "category": "costumes"},  # <-- new costume
    {"id": "ein_sheeple",       "label": "Ein Sheeple Costume",       "price": 1000, "image": "images/Icons/SPC2.png", "gives": "item", "crop": "ein_sheeple",       "category": "costumes"},  # <-- new costume
    {"id": "hoops_hopper",      "label": "Hoops Hopper Costume",      "price": 1000, "image": "images/Icons/BYC1.png", "gives": "item", "crop": "hoops_hopper",      "category": "costumes"},  # <-- new costume
    {"id": "gala_glamour",      "label": "Gala Glamour Costume",      "price": 1000, "image": "images/Icons/BYC2.png", "gives": "item", "crop": "gala_glamour",      "category": "costumes"},  # <-- new costume
    {"id": "bye_bye_clitty",    "label": "Bye Bye Clitty Costume",    "price": 1000, "image": "images/Icons/CTC1.png", "gives": "item", "crop": "bye_bye_clitty",    "category": "costumes"},  # <-- new costume
    {"id": "katnip_kraver",     "label": "Katnip Kraver Costume",     "price": 1000, "image": "images/Icons/CTC2.png", "gives": "item", "crop": "katnip_kraver",     "category": "costumes"},  # <-- new costume
    {"id": "sexual_dogma",      "label": "Sexual Dogma Costume",      "price": 1000, "image": "images/Icons/DGC1.png", "gives": "item", "crop": "sexual_dogma",      "category": "costumes"},  # <-- new costume
    {"id": "best_in_show",      "label": "Best in Show Costume",      "price": 1000, "image": "images/Icons/DGC2.png", "gives": "item", "crop": "best_in_show",      "category": "costumes"},  # <-- new costume
    {"id": "tractor",        "label": "Tractor (Harvest all crops at once.)", "price": 1000, "image": "images/Maps/Fields/tractor_idle.png", "gives": "item", "crop": "tractor", "category": "tools"},  # <-- new tool
    {"id": "sprinkler",      "label": "Sprinkler (Water all crops at once.)", "price": 1000, "image": "images/Maps/Fields/sprinkler_idle.png", "gives": "item", "crop": "sprinkler", "category": "tools"},  # <-- new tool
]
default market_sell = [
    {"id": "wheat",   "label": "Wheat",   "price": 10,  "image": "images/Maps/Fields/wheat_item.png"},
    {"id": "corn",    "label": "Corn",    "price": 30,  "image": "images/Maps/Fields/corn_item.png"},
    {"id": "carrot",  "label": "Carrot",  "price": 50,  "image": "images/Maps/Fields/carrot_item.png"},
    {"id": "pumpkin", "label": "Pumpkin", "price": 100, "image": "images/Maps/Fields/pumpkin_item.png"},
    {"id": "apple",   "label": "Apple",   "price": 350, "image": "images/Maps/Fields/apple_item.png"},
    {"id": "fish",    "label": "Fish",    "price": 60,  "image": "images/Maps/Market/fish_item.png"},    # <-- new
    {"id": "steak",   "label": "Steak",   "price": 80,  "image": "images/Maps/Market/steak_item.png"},  # <-- new
    {"id": "cheese",  "label": "Cheese",  "price": 40,  "image": "images/Maps/Market/cheese_item.png"}, # <-- new
]
default animal_care = {
    "horse": {"care": 0, "washed": False, "brushed": False, "fed": False},
    "cow":   {"care": 0, "washed": False, "brushed": False, "fed": False},
    "pig":   {"care": 0, "washed": False, "brushed": False, "fed": False},
    "goat":  {"care": 0, "washed": False, "brushed": False, "fed": False},
    "mouse": {"care": 0, "washed": False, "brushed": False, "fed": False},
    "cat":   {"care": 0, "washed": False, "brushed": False, "fed": False},
    "dog":   {"care": 0, "washed": False, "brushed": False, "fed": False},
    "bunny": {"care": 0, "washed": False, "brushed": False, "fed": False},
    "sheep": {"care": 0, "washed": False, "brushed": False, "fed": False},
}
default active_care_tool = None
default animal_gifted = {
    "horse":  {"truffle": False, "golden_truffle": False},
    "cow":    {"choco": False, "golden_choco": False},
    "pig":    {"truffle": False, "golden_truffle": False},
    "goat":   {"ramen": False, "golden_ramen": False},
    "mouse":  {"cheesecake": False, "golden_cheesecake": False},
    "cat":    {"truffle": False, "golden_truffle": False},
    "dog":    {"truffle": False, "golden_truffle": False},
    "bunny":  {"truffle": False, "golden_truffle": False},
    "sheep":  {"truffle": False, "golden_truffle": False},
}
init:
    transform tool_scale:
        zoom 1.4

    transform seed_greyed:
        matrixcolor SaturationMatrix(0.0)

    transform counter_pulse_transform:
        zoom 1.0
        linear 0.15 zoom 1.4
        linear 0.15 zoom 1.0

init python:
    import time

    BIO_ORDER = ["pig", "goat", "cow", "mouse"]

    BIO_IMAGES = {
        "pig":   "images/bio/PG_Bio.jpg",
        "goat":  "images/bio/GT_Bio.jpg",
        "cow":   "images/bio/CW_Bio.jpg",
        "mouse": "images/bio/ME_Bio.jpg",
    }

    BIO_NAMES = {
        "pig":   "Pudding",
        "goat":  "Daisy",
        "cow":   "Annabelle",
        "mouse": "Penny",
    }

    BIO_TITLES = {
        "pig":   "Pudding the Pig",
        "goat":  "Daisy the Goat",
        "cow":   "Annabelle the Cow",
        "mouse": "Penny the Mouse",
    }

    BIO_LIKES = {
        "pig":   "Mud baths, corn on the cob, and lazy afternoon naps in the sun.",
        "goat":  "Old books, quiet mornings, and anyone who takes the time to really notice her.",
        "cow":   "Fresh wildflowers, slow dancing, and a good scratch behind the ears.",
        "mouse": "Chewing on wheat stalks, tinkering with little gadgets, and sneaking extra cheese.",
    }

    SCENE_LABELS = {
        "pig":   ["Meet Pudding", "Panty Raid", "Dirty Talk"],
        "goat":  ["Attention Seeker", "In the Act", "Rave Rendezvous"],
        "cow":   ["Got Milk?", "Free Use", "Double Trouble"],
        "mouse": ["Wrecking Balls", "Gag Order", "Hanging Out"],
    }

    def bio_next():
        idx = BIO_ORDER.index(store.bio_character)
        store.bio_character = BIO_ORDER[(idx + 1) % len(BIO_ORDER)]

    def bio_prev():
        idx = BIO_ORDER.index(store.bio_character)
        store.bio_character = BIO_ORDER[(idx - 1) % len(BIO_ORDER)]

    def set_animal_hovered(animal, value):
        store.animal_hovered[animal] = value
        renpy.restart_interaction()

    def reset_care_heart(animal):                                   # <-- new, handles timer reset cleanly
        store.show_care_heart[animal] = False
        renpy.restart_interaction()

    def get_plot_image(index):
        plot = farm_plots[index]
        state = plot["state"]
        watered_today = plot.get("water_day", 0) == store.in_game_day

        if state == "dry":
            return "images/Maps/Fields/drysoil_idle.png"
        elif state in ("seed", "sprout", "medium", "max"):
            return "images/Maps/Fields/wetsoil_idle.png" if watered_today else "images/Maps/Fields/drysoil_idle.png"
        elif state == "dead":
            return "images/Maps/Fields/drysoil_idle.png"
        return "images/Maps/Fields/drysoil_idle.png"

    def get_plot_hover(index):
        plot = farm_plots[index]
        state = plot["state"]
        watered_today = plot.get("water_day", 0) == store.in_game_day

        if state == "dry":
            return "images/Maps/Fields/drysoil_hover.png"
        elif state in ("seed", "sprout", "medium", "max"):
            return "images/Maps/Fields/wetsoil_hover.png" if watered_today else "images/Maps/Fields/drysoil_hover.png"
        elif state == "dead":
            return "images/Maps/Fields/drysoil_hover.png"
        return "images/Maps/Fields/drysoil_hover.png"

    def get_plant_image(index):
        plot = farm_plots[index]
        crop = plot.get("crop")
        state = plot.get("state")

        if state in ("sprout", "medium", "max") and crop:
            return f"images/Maps/Fields/{crop}_{state}.png"
        elif state in ("seed",) and crop:
            return f"images/Maps/Fields/{crop}_seed.png"
        elif state == "dead":
            return "images/Maps/Fields/dead_plant.png"
        return None

    CARE_CHECKPOINTS = [0, 33, 66, 100]

    def get_care_floor(value):                                      # <-- checkpoints never lost once reached
        floor = 0
        for checkpoint in CARE_CHECKPOINTS:
            if value >= checkpoint:
                floor = checkpoint
        return floor

    def advance_day():
        store.in_game_day += 1

        growth_order = ["seed", "sprout", "medium", "max"]

        for plot in farm_plots:
            state = plot.get("state")

            if state not in ("seed", "sprout", "medium"):
                continue

            if plot.get("water_day", -1) < store.in_game_day - 1:
                if state == "seed":
                    plot["state"] = "dry"
                    plot["crop"] = None
                else:
                    plot["state"] = "dead"
                continue

            if state in growth_order:
                next_index = growth_order.index(state) + 1
                if next_index < len(growth_order):
                    plot["state"] = growth_order[next_index]

        for animal, data in store.animal_care.items():
            did_care = data["washed"] or data["brushed"] or data["fed"]
            if not did_care:
                data["care"] = max(get_care_floor(data["care"]), data["care"] - 5)
            data["washed"] = False
            data["brushed"] = False
            data["fed"] = False

        renpy.restart_interaction()

    CROP_COUNTER_ORDER = ["apple", "carrot", "wheat", "corn", "pumpkin"]

    def plot_screen_pos(index):
        col = index % 10
        row = index // 10
        grid_x = 0.2 * (1920 - (10 * 128 + 9 * 8))
        grid_y = 0.4 * (1080 - (3 * 256 + 2 * 8))
        cell_x = grid_x + col * (128 + 8)
        cell_y = grid_y + row * (256 + 8)
        return (int(cell_x + 64), int(cell_y + 190))

    def crop_counter_pos(crop):
        n = CROP_COUNTER_ORDER.index(crop)
        outer_x = 0.4 * (1920 - (709 + 32))
        outer_y = 0.02 * (1080 - (63 + 20))
        content_x = outer_x + 16
        content_y = outer_y + 10
        return (int(content_x + n * 145 + 31.5), int(content_y + 31.5))

    def spawn_harvest_flyer(crop, plot_index, delay=0.0):
        store.harvest_flyers.append({
            "crop": crop,
            "start": plot_screen_pos(plot_index),
            "end": crop_counter_pos(crop),
            "path": renpy.random.choice(["straight", "curve_left", "curve_right"]),
            "delay": delay,
            "duration": 0.6,
            "spawn_time": time.time(),
        })

    def flyer_position(flyer):
        elapsed = time.time() - flyer["spawn_time"] - flyer["delay"]
        sx, sy = flyer["start"]
        ex, ey = flyer["end"]
        if elapsed <= 0:
            return (sx, sy)
        t = min(1.0, elapsed / flyer["duration"])
        if flyer["path"] == "straight":
            return (int(sx + (ex - sx) * t), int(sy + (ey - sy) * t))
        side = 70 if flyer["path"] == "curve_right" else -70
        midx = (sx + ex) / 2 + side
        midy = (sy + ey) / 2 - 30
        if t < 0.5:
            t2 = t / 0.5
            return (int(sx + (midx - sx) * t2), int(sy + (midy - sy) * t2))
        else:
            t2 = (t - 0.5) / 0.5
            return (int(midx + (ex - midx) * t2), int(midy + (ey - midy) * t2))

    def tick_flyers():
        finished = [f for f in store.harvest_flyers if time.time() - f["spawn_time"] >= f["delay"] + f["duration"]]
        for f in finished:
            store.harvest_flyers.remove(f)
            store.player_inventory[f["crop"]] += 1
            store.counter_pulse[f["crop"]] = True
            renpy.sound.play(audio.click_2)
        renpy.restart_interaction()

    def flush_harvest_flyers():
        for f in store.harvest_flyers:
            store.player_inventory[f["crop"]] += 1
        store.harvest_flyers = []

    def reset_counter_pulse(crop):
        store.counter_pulse[crop] = False
        renpy.restart_interaction()

    def use_tool(index):
        plot = farm_plots[index]

        if active_tool == "water":
            if plot["state"] in ("seed", "sprout", "medium", "max"):
                plot["water_day"] = store.in_game_day
                store.show_water_anim = True
                store.default_mouse = "water_action"               # <-- swaps cursor to action image
                renpy.sound.play(audio.watering)

        elif active_tool == "seeds" and selected_seed:
            seed_key = selected_seed + "_seed"
            if plot["state"] == "dry" and store.player_inventory.get(seed_key, 0) > 0:
                plot["state"] = "seed"
                plot["crop"] = selected_seed
                store.player_inventory[seed_key] -= 1
                renpy.sound.play(audio.seed)

        elif active_tool == "hoe":
            was_dry = (plot["state"] == "dry")
            plot["state"] = "dry"
            plot["crop"] = None
            if not was_dry:
                renpy.sound.play(audio.hoe)

        elif active_tool == "scythe":
            if plot["state"] == "max":
                crop = plot["crop"]
                plot["state"] = "dry"
                plot["crop"] = None
                spawn_harvest_flyer(crop, index)
                renpy.sound.play(audio.harvest)

        renpy.restart_interaction()

    def use_sprinkler():
        watered_any = False
        for plot in farm_plots:
            if plot["state"] in ("seed", "sprout", "medium"):
                plot["water_day"] = store.in_game_day
                watered_any = True
        if watered_any:
            renpy.sound.play(audio.watering)
        renpy.restart_interaction()

    def use_tractor():
        harvested_any = False
        delay = 0.0
        for i, plot in enumerate(farm_plots):
            if plot["state"] == "max":
                crop = plot["crop"]
                plot["state"] = "dry"
                plot["crop"] = None
                spawn_harvest_flyer(crop, i, delay=delay)
                delay += 0.12
                harvested_any = True
        if harvested_any:
            renpy.sound.play(audio.harvest)
        renpy.restart_interaction()

    def go_to_map(target):
        if store.current_map:
            renpy.hide_screen(store.current_map)
        if target == "Farm_map":
            renpy.hide_screen("persistent_hud")
        else:
            renpy.show_screen("persistent_hud")
        renpy.show_screen(target)
        store.current_map = target

        track = audio.store_music if target in ("Market_map", "Fields_map") else audio.main_music
        if renpy.music.get_playing(channel="music") != track:
            renpy.music.play(track, channel="music")

    def buy_item(item):
        if store.player_gold >= item["price"]:
            store.player_gold -= item["price"]
            if item["gives"] == "seeds":
                store.player_inventory[item["crop"]] = min(99, store.player_inventory[item["crop"]] + 1)
            elif item["gives"] == "item":
                store.player_inventory[item["crop"]] += 1
            one_time_ids = ("truffle", "golden_truffle", "ramen", "golden_ramen", "choco", "golden_choco", "cheesecake", "golden_cheesecake")
            if item["category"] in ("costumes", "tools") or item["id"] in one_time_ids:
                renpy.sound.play(audio.money_2)
            else:
                renpy.sound.play(audio.money_1)
        renpy.restart_interaction()

    def sell_item(item):
        if store.player_inventory[item["id"]] > 0:
            store.player_inventory[item["id"]] -= 1
            store.player_gold += item["price"]
        renpy.restart_interaction()

    def do_care_task(animal, task):
        data = store.animal_care[animal]

        if task == "wash" and not data["washed"]:
            data["washed"] = True
            data["care"] = min(100, data["care"] + 1)
            store.show_care_heart[animal] = True
            renpy.sound.play(audio.wash)

        elif task == "brush" and not data["brushed"]:
            data["brushed"] = True
            data["care"] = min(100, data["care"] + 1)
            store.show_care_heart[animal] = True
            renpy.sound.play(audio.brush)

        elif task == "feed" and not data["fed"]:
            feed_items = {
                "horse": "apple",
                "pig":   "corn",
                "goat":  "pumpkin",
                "cow":   "wheat",
                "cat":   "fish",
                "dog":   "steak",
                "mouse": "cheese",
                "bunny": "carrot",
                "sheep": "beer",
            }
            food = feed_items.get(animal)
            if food and store.player_inventory.get(food, 0) > 0:
                store.player_inventory[food] -= 1
                data["fed"] = True
                data["care"] = min(100, data["care"] + 5)
                store.show_care_heart[animal] = True
                renpy.sound.play(audio.feed)

        store.active_care_tool = None
        store.animal_hovered[animal] = False                       # <-- reset hover after task completes
        renpy.restart_interaction()
        
    def do_gift_task(animal, item):
        if store.player_inventory.get(item, 0) > 0:
            store.player_inventory[item] -= 1
            store.animal_gifted[animal][item] = True
            store.show_care_heart[animal] = True
            renpy.sound.play(audio.money_2)
        store.animal_hovered[animal] = False
        store.show_gift = False
        renpy.restart_interaction()

    def restore_tool_cursor():
        tool_cursors = {
            "water":  "water",
            "seeds":  "seeds",
            "scythe": "scythe",
            "hoe":    "hoe",
        }
        store.default_mouse = tool_cursors.get(store.active_tool, "default")
        renpy.restart_interaction()

define mc = Character("player_character", dynamic=True, image="mc", who_color="#ff0000")
define pig = Character("Pudding the Pig", image="pig", who_color="#ff66b2")
define cow = Character("Annabelle the Cow", image="cow", who_color="#3399ff")
define mirabelle = Character("Mirabelle")
define horse = Character("Lady Moonbeam")
define sheep = Character("Dolly")
define goat = Character("Daisy the Goat", image="goat", who_color="#2dab11")
define dog = Character("Millie")
define cat = Character("Misty")
define mouse = Character("Penny the Mouse", image="mouse", who_color="#ff9933")
define bunny = Character("Roxy")
define malik = Character("Malik")
define king = Character("King")
define thunder = Character("Thunder")

image pg_1 = "images/sprites/Pig/pg_1.png"

image side pig = ConditionSwitch(
    "pig_costume == 'piggy_icon'", "images/Sprites/Pig/PGC1.png",
    "pig_costume == 'stars_stripes'", "images/Sprites/Pig/PGC2.png",
    "True", "images/Sprites/Pig/PGD1.png",
)

image side mc = ConditionSwitch(
    "player_character == 'Malik'", "images/Sprites/MC/mc_gorilla.png",
    "player_character == 'King'", "images/Sprites/MC/mc_bear.png",
    "player_character == 'Thunder'", "images/Sprites/MC/mc_horse.png",
    "True", "images/Sprites/MC/mc_gorilla.png",
)

image side goat = ConditionSwitch(
    "goat_costume == 'g_o_a_t'", "images/Sprites/Goat/GTC1.png",
    "goat_costume == 'high_noon'", "images/Sprites/Goat/GTC2.png",
    "True", Transform("images/Sprites/Goat/GTD1.png", xzoom=-1.0),
)

image side cow = ConditionSwitch(
    "cow_costume == 'life_saver'", "images/Sprites/Cow/CWC1.png",
    "cow_costume == 'macabre_bovine'", Transform("images/Sprites/Cow/CWC2.png", xzoom=-1.0),
    "True", "images/sprites/Cow/cw_1.png",
)

image side mouse = ConditionSwitch(
    "mouse_costume == 'stew_art_little'", "images/Sprites/Mouse/MEC1.png",
    "mouse_costume == 'one_blind_mice'", "images/Sprites/Mouse/MEC2.png",
    "True", "images/Sprites/Mouse/MED2.png",
)
image pg_2 = "images/sprites/Pig/pg_2.png"
image gt_1 = "images/sprites/Goat/gt_1.png"
image ct_1 = "images/sprites/Cat/ct_1.png"
image by_1 = "images/sprites/Bunny/by_1.png"
image me_1 = "images/sprites/Mouse/me_1.png"
image he_1 = "images/sprites/Horse/he_1.png"
image cw_1 = "images/sprites/Cow/cw_1.png"
image sp_1 = "images/sprites/Sheep/sp_1.png"
image dg_1 = "images/sprites/Dog/dg_1.png"

transform fit_sprite:
    zoom 0.71
    align (.5, 1.0)

transform fit_left:
    zoom 0.71
    align (.25, 1.0)

image bg Farm_1 = "images/Backgrounds/Farm/farm_1.5.png"
image bg Farm_2 = "images/Backgrounds/Farm/farm_2.png"
image bg House_1 = "images/Backgrounds/House/House_1.jpeg"
image bg Stables_1 = "images/Backgrounds/Stables/Stables_1.jpeg"
image bg Stables_2 = "images/Backgrounds/Stables/Stables_2.jpeg"
image bg HE_1 = "images/Backgrounds/Stables/HE_1.jpeg"
image bg CW_1 = "images/Backgrounds/Stables/Cow/CW_1.png"
image bg CW_2 = "images/Backgrounds/Stables/Cow/CW_2.png"
image bg CW_3 = "images/Backgrounds/Stables/Cow/CW_3.png"
image bg CW_4 = "images/Backgrounds/Stables/Cow/CW_4.jpg"
image bg CW_5 = "images/Backgrounds/Stables/Cow/CW_5.jpg"
image bg CW_6 = "images/Backgrounds/Stables/Cow/CW_6.png"
image bg CW_7 = "images/Backgrounds/Stables/Cow/CW_7.jpg"
image bg CW_8 = "images/Backgrounds/Stables/Cow/CW_8.jpg"
image bg CW_9 = "images/Backgrounds/Stables/Cow/CW_9.jpg"
image bg CW_10 = "images/Backgrounds/Stables/Cow/CW_10.jpg"
image bg CW_11 = "images/Backgrounds/Stables/Cow/CW_11.jpg"
image bg CW_12 = "images/Backgrounds/Stables/Cow/CW_12.jpg"
image bg CW_13 = "images/Backgrounds/Stables/Cow/CW_13.jpeg"
image bg CW_14 = "images/Backgrounds/Stables/Cow/CW_14.jpg"
image bg CW_15 = "images/Backgrounds/Stables/Cow/CW_15.png"
image bg CW_16 = "images/Backgrounds/Stables/Cow/CW_16.png"
image bg CW_17 = "images/Backgrounds/Stables/Cow/CW_17.jpg"
image bg CW_18 = "images/Backgrounds/Stables/Cow/CW_18.jpg"
image bg CW_19 = "images/Backgrounds/Stables/Cow/CW_19.jpg"
image bg CW_20 = "images/Backgrounds/Stables/Cow/CW_20.jpg"
image bg CW_21 = "images/Backgrounds/Stables/Cow/CW_21.jpg"
image bg CW_22 = "images/Backgrounds/Stables/Cow/CW_22.jpg"
image bg CW_23 = "images/Backgrounds/Stables/Cow/CW_23.jpg"
image bg CW_24 = "images/Backgrounds/Stables/Cow/CW_24.jpg"
image bg CW_25 = "images/Backgrounds/Stables/Cow/CW_25.jpg"
image bg CW_26 = "images/Backgrounds/Stables/Cow/CW_26.jpg"
image bg CW_27 = "images/Backgrounds/Stables/Cow/CW_27.jpg"
image bg CW_28 = "images/Backgrounds/Stables/Cow/CW_28.png"
image bg CW_29 = "images/Backgrounds/Stables/Cow/CW_29.jpg"
image bg CW_30 = "images/Backgrounds/Stables/Cow/CW_30.jpg"
image bg CW_31 = "images/Backgrounds/Stables/Cow/CW_31.jpg"
image bg CW_32 = "images/Backgrounds/Stables/Cow/CW_32.jpg"
image bg CW_33 = "images/Backgrounds/Stables/Cow/CW_33.jpg"
image bg CW_34 = "images/Backgrounds/Stables/Cow/CW_34.jpg"
image bg CW_35 = "images/Backgrounds/Stables/Cow/CW_35.jpg"
image bg CW_36 = "images/Backgrounds/Stables/Cow/CW_36.jpeg"
image bg CW_37 = "images/Backgrounds/Stables/Cow/CW_37.jpg"
image bg CW_38 = "images/Backgrounds/Stables/Cow/CW_38.jpeg"
image bg CW_39 = "images/Backgrounds/Stables/Cow/CW_39.jpg"
image bg GT_1 = "images/Backgrounds/Stables/GT_1.png"
image bg GT_2 = "images/Backgrounds/Stables/Goat/GT_2.jpeg"
image bg GT_3 = "images/Backgrounds/Stables/Goat/GT_3.jpeg"
image bg GT_4 = "images/Backgrounds/Stables/Goat/GT_4.jpeg"
image bg GT_5 = "images/Backgrounds/Stables/Goat/GT_5.png"
image bg GT_6 = "images/Backgrounds/Stables/Goat/GT_6.png"
image bg GT_7 = "images/Backgrounds/Stables/Goat/GT_7.png"
image bg GT_8 = "images/Backgrounds/Stables/Goat/GT_8.png"
image bg GT_9 = "images/Backgrounds/Stables/Goat/GT_9.png"
image bg GT_10 = "images/Backgrounds/Stables/Goat/GT_10.jpeg"
image bg GT_11 = "images/Backgrounds/Stables/Goat/GT_11.png"
image bg GT_12 = "images/Backgrounds/Stables/Goat/GT_12.jpeg"
image bg GT_13 = "images/Backgrounds/Stables/Goat/GT_13.jpeg"
image bg GT_14 = "images/Backgrounds/Stables/Goat/GT_14.jpeg"
image bg GT_15 = "images/Backgrounds/Stables/Goat/GT_15.jpeg"
image bg GT_16 = "images/Backgrounds/Stables/Goat/GT_16.jpeg"
image bg GT_17 = "images/Backgrounds/Stables/Goat/GT_17.jpeg"
image bg GT_18 = "images/Backgrounds/Stables/Goat/GT_18.jpeg"
image bg GT_19 = "images/Backgrounds/Stables/Goat/GT_19.jpeg"
image bg GT_20 = "images/Backgrounds/Stables/Goat/GT_20.jpeg"
image bg GT_21 = "images/Backgrounds/Stables/Goat/GT_21.png"
image bg GT_22 = "images/Backgrounds/Stables/Goat/GT_22.jpg"
image bg GT_23 = "images/Backgrounds/Stables/Goat/GT_23.jpg"
image bg GT_24 = "images/Backgrounds/Stables/Goat/GT_24.jpg"
image bg GT_25 = "images/Backgrounds/Stables/Goat/GT_25.jpg"
image bg GT_26 = "images/Backgrounds/Stables/Goat/GT_26.jpg"
image bg GT_27 = "images/Backgrounds/Stables/Goat/GT_27.png"
image bg GT_28 = "images/Backgrounds/Stables/Goat/GT_28.jpg"
image bg GT_29 = "images/Backgrounds/Stables/Goat/GT_29.jpg"
image bg GT_30 = "images/Backgrounds/Stables/Goat/GT_30.jpg"
image bg GT_31 = "images/Backgrounds/Stables/Goat/GT_31.jpg"
image bg GT_32 = "images/Backgrounds/Stables/Goat/GT_32.jpg"
image bg GT_33 = "images/Backgrounds/Stables/Goat/GT_33.jpg"
image bg GT_34 = "images/Backgrounds/Stables/Goat/GT_34.jpg"
image bg GT_35 = "images/Backgrounds/Stables/Goat/GT_35.png"
image bg GT_36 = "images/Backgrounds/Stables/Goat/GT_36.jpg"
image bg GT_37 = "images/Backgrounds/Stables/Goat/GT_37.jpg"
image bg GT_38 = "images/Backgrounds/Stables/Goat/GT_38.jpg"
image bg GT_39 = "images/Backgrounds/Stables/Goat/GT_39.jpg"
image bg GT_40 = "images/Backgrounds/Stables/Goat/GT_40.jpg"
image bg GT_41 = "images/Backgrounds/Stables/Goat/GT_41.jpg"
image bg GT_42 = "images/Backgrounds/Stables/Goat/GT_42.jpg"
image bg GT_43 = "images/Backgrounds/Stables/Goat/GT_43.png"
image bg GT_44 = "images/Backgrounds/Stables/Goat/GT_44.jpg"
image bg GT_45 = "images/Backgrounds/Stables/Goat/GT_45.jpg"
image bg GT_46 = "images/Backgrounds/Stables/Goat/GT_46.jpg"
image bg GT_47 = "images/Backgrounds/Stables/Goat/GT_47.jpg"
image bg GT_48 = "images/Backgrounds/Stables/Goat/GT_48.jpg"
image bg PG_1 = "images/Backgrounds/Stables/PG_1.jpeg"
image bg PG_2 = "images/Backgrounds/Stables/Pig/PG_2.jpeg"
image bg PG_3 = "images/Backgrounds/Stables/Pig/PG_3.png"
image bg PG_4 = "images/Backgrounds/Stables/Pig/PG_4.png"
image bg PG_5 = "images/Backgrounds/Stables/Pig/PG_5.jpeg"
image bg PG_6 = "images/Backgrounds/Stables/Pig/PG_6.jpeg"
image bg PG_7 = "images/Backgrounds/Stables/Pig/PG_7.jpeg"
image bg PG_9 = "images/Backgrounds/Stables/Pig/PG_9.jpeg"
image bg PG_10 = "images/Backgrounds/Stables/Pig/PG_10.png"
image bg PG_11 = "images/Backgrounds/Stables/Pig/PG_11.jpeg"
image bg PG_12 = "images/Backgrounds/Stables/Pig/PG_12.jpeg"
image bg PG_13 = "images/Backgrounds/Stables/Pig/PG_13.jpeg"
image bg PG_14 = "images/Backgrounds/Stables/Pig/PG_14.jpeg"
image bg PG_15 = "images/Backgrounds/Stables/Pig/PG_15.jpeg"
image bg PG_16 = "images/Backgrounds/Stables/Pig/PG_16.jpeg"
image bg PG_17 = "images/Backgrounds/Stables/Pig/PG_17.jpeg"
image bg PG_18 = "images/Backgrounds/Stables/Pig/PG_18.jpeg"
image bg PG_19 = "images/Backgrounds/Stables/Pig/PG_19.jpeg"
image bg PG_20 = "images/Backgrounds/Stables/Pig/PG_20.jpeg"
image bg PG_21 = "images/Backgrounds/Stables/Pig/PG_21.png"
image bg office = "images/Backgrounds/UI/Office.png"

label Farm_map:
    call screen Farm_map
    return
label FHhallway_map:
    call screen FHhallway_map
    return
label Stables_map:
    play music audio.main_music
    call screen Stables_map
    return
label Market_map:
    call screen Market_map
    return
label Fields_map:
    call screen Fields_map
    return
label MC_map:
    play music audio.main_music
    call screen MC_map
    return
label ME_map:
    call screen ME_map
    return
label CT_map:
    call screen CT_map
    return
label DG_map:
    call screen DG_map
    return
label PG_map:
    call screen PG_map
    return
label GT_map:
    call screen GT_map
    return
label CW_map:
    call screen CW_map
    return
label HE_map:
    call screen HE_map
    return
label BY_map:
    call screen BY_map
    return
label SP_map:
    call screen SP_map
    return


define audio.seed = "audio/seeds.wav"
define audio.watering = "audio/watering.wav"
define audio.harvest = "audio/harvest.wav"
define audio.hoe = "audio/hoe.wav"
define audio.rooster = "audio/rooster.wav"
define audio.main_music = "audio/main.wav"
define audio.store_music = "audio/store.wav"
define audio.sex_music = "audio/sex.wav"
define audio.click_1 = "audio/click_1.wav"
define audio.click_2 = "audio/click_2.wav"
define audio.door_open = "audio/door_open.wav"
define audio.door_close = "audio/door_close.wav"
define audio.money_1 = "audio/money_1.wav"
define audio.money_2 = "audio/money_2.wav"
define audio.wash = "audio/wash.wav"
define audio.brush = "audio/brush.wav"
define audio.feed = "audio/feed.wav"

label splashscreen:
    show screen splash_adult_warning
    pause 2.0
    hide screen splash_adult_warning with Dissolve(0.3)

    show screen splash_character_age
    pause 2.0
    hide screen splash_character_age with Dissolve(0.3)

    return

label sleep_transition:
    scene black
    hide screen MC_map
    hide screen persistent_hud
    $ advance_day()
    show screen day_counter(in_game_day)
    pause 2.0
    hide screen day_counter with Dissolve(0.3)
    scene black
    play sound audio.rooster                                       # <-- plays rooster
    show screen persistent_hud
    $ renpy.jump("MC_map")                                     # <-- use renpy.jump instead of jump                                       # <-- return instead of jump, clears call stack                         # <-- jumps back to MC_map label               

transform bg_stretch:
    size (1920, 1080)

transform button_scale:
    zoom 0.50

label start:
    $ renpy.block_rollback()
    if player_character is None:
        $ player_character = renpy.call_screen("character_select")  # <-- captures the Return() value

    
scene black with Dissolve (1.0) 
scene bg office
"The letter arrived on a gray morning, slipped halfway under the apartment door like it had been waiting for the right moment."
"You almost ignored it."
"Until you saw the return address."
"Your Uncle Henry’s name."
"You hadn’t seen him in years — not since childhood summers spent chasing chickens and getting lost in cornfields taller than you were."
"Hands slightly trembling, you opened it."
"If you’re reading this, the farm is yours now. She needs new hands. Strong ones. I hope you’ll give her the life she deserves."
#### Countryside road ####
play music audio.store_music
scene bg Farm_1 with Dissolve (1.0)  
"Three weeks later, everything you owned fit into the back of your truck."
"The gravel road to the farm crunched under your tires. The fields stretched wide and golden in the afternoon sun. A weathered farmhouse stood at the heart of it all, barn painted deep red, a tall grain silo beside it, fenced fields rolling toward a small lake glinting in the distance."
#### Farm Background ####
scene bg Farm_2
"It was bigger than you remembered."
"And quieter."
"You stepped out of the truck."
"That must be him."
"A voice called from the barn."
"You turned."
"A young woman wiped her hands on a cloth as she walked toward you. Sun-kissed skin, straw hat tilted back slightly, overalls rolled at the ankles. Confident stride. Easy smile."
show me_1 at fit_sprite
mouse "You must be Henry’s nephew."
mc "You nod. “That’s me."
"She offers to shake your hand."
mouse "Name’s Penny. I’ve been keeping things running since… well."
"You shake her hand. Her grip is firm."
mouse "Welcome to your farm."
"She gestured outward."
#### Insert Background of farm fields ####
mouse "We’ve got corn and wheat fields on the east side. Carrots closer to the creek — they like the softer soil. Oats grow well near the back pasture. Apple trees need pruning before harvest, and pumpkins…” she smirked, “pumpkins are stubborn but worth it."
"You follow her as she walks."
mouse "Tilling comes first. Soil’s gotta breathe before you plant. Water in the mornings, always. Too much and you’ll drown the roots."
"She pointed toward the barn."
#### Insert Background of farm animals or stables ####
mouse "Animals need tending twice daily. Cow’s gentle but picky with feed. Pig’ll eat near anything. Horse needs brushing and clean hooves. Sheep and goat are easy — just don’t let ’em test the fence."
"A small cat darted past your boots."
mouse "And that one runs the place,"
"A dog barked from the porch."
mouse "You feed them right, care for ’em right, they’ll take care of you."
"She stopped in front of the farmhouse steps and smiled again."
mouse "Big change from city life, huh?"
"You exhaled slowly."
mc "Yeah."
mc "Big change."

call tutorial_start from _call_tutorial_start

return
