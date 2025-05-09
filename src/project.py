import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time, csv, pygame, random, random_fight, hard_random_enemy, first_fight
pygame.init()
trees_rustle = pygame.mixer.Sound(r'sounds\wind_trees.mp3')
breaking_wall = pygame.mixer.Sound(r'sounds\wall_break.mp3')
player_falls = pygame.mixer.Sound(r'sounds\character_hits_ground.mp3')
city_rain = pygame.mixer.Sound(r'sounds\rain_concrete.mp3')

def anim_print(UI_text, delay=0.052):
    for character in UI_text:
        print(character, end="", flush=True)
        time.sleep(delay)
    print()

def anim_input(prompt):
    for character in prompt:
        print(character, end="", flush=True)
        time.sleep(0.062)
    return input()

def opening_scene():
    time.sleep(.07)
    anim_print("Loading...", delay=0.135)
    time.sleep(1.5)
    anim_print("Running interactive program...", delay=0.135)
    time.sleep(1.5)
    filename = "project_inventory.csv"
    statistics = "stats.csv"

    wrong_username = True
    while wrong_username:
        username = anim_input("Input a name: ").capitalize()
        if username == "Ana" or username == "Syuuran":
            wrong_username = True
            anim_print("That name is in use.")
        elif username == "":
            anim_print("This input is no good...")
            time.sleep(1)
        else:
            wrong_username = False
    creating_stats = True
    while creating_stats:
        while True:
            adjective_01 = anim_input("Adjective 01: ".lower())
            if adjective_01 != "":
                break
            anim_print("This input is no good...")
            anim_print("Retry your input.")
            time.sleep(1)
        
        while True:
            adjective_02 = anim_input("Adjective 02: ".lower())
            if adjective_02 != "":
                break
            anim_print("This input is no good...")
            anim_print("Retry your input.")
            time.sleep(1)
        
        while True:
            ability = anim_input("What is a good skill to have? ")
            if ability != "":
                break
            anim_print("This input is no good...")
            anim_print("Retry your input.")
            time.sleep(1)
        
        while True:
            weakness = anim_input("In one word, what scares you? ")
            if weakness != "":
                break
            anim_print("This input is no good...")
            anim_print("Retry your input.")
            time.sleep(1)
        creating_stats = False

    strength = True
    while strength:
        try:
            anim_print(f"Pick a number between 1 and 10.")
            attack = float(anim_input("Choose wisely: "))
            if 1 <= attack <= 10:
                strength = False
            else:
                anim_print("This is not what was asked of you.")
                time.sleep(0.75)
        except ValueError:
            anim_print("Do you call that a number...?")
            time.sleep(1)
    with open(statistics, 'a', newline='') as file:
        new_stat = "your name"
        you = username
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_stat, you])
    with open(statistics, 'a', newline='') as file:
        new_stat = "your description"
        description = adjective_01, adjective_02
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_stat, description])
    with open(statistics, 'a', newline='') as file:
        new_stat = "your ability"
        player_ability = ability
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_stat, player_ability])
    with open(statistics, 'a', newline='') as file:
        new_stat = "your weakness"
        player_weakness = weakness
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_stat, player_weakness])
    with open(statistics, 'a', newline='') as file:
        new_stat = "your attack"
        kill_power = attack
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_stat, kill_power])
    with open(statistics, 'a', newline='') as file:
        new_stat = "your health"
        life = 100
        csv_writer = csv.writer(file)
        csv_writer.writerow([new_stat, life])

    anim_print("Loading...", delay=0.135)
    time.sleep(1.5)
    print()
    anim_print("Welcome...", delay=0.14)
    anim_print("You feel... odd.")
    time.sleep(1)
    anim_print("Who are you? Do you know anymore?")
    time.sleep(1)
    anim_print("Your choices have consequences.")
    time.sleep(0.5)
    anim_print("So choose wisely...")
    time.sleep(1)
    print()

    anim_print("Character: ANA")
    time.sleep(1)
    anim_print("Description: Ana is happy and kinda brave. There's not much else to say.")
    time.sleep(1)
    anim_print("Health: 100")
    anim_print("Attack: 6")
    anim_print("Special Ability: Observation")
    anim_print("Weakness: Spiders")
    time.sleep(1.5)
    print()

    anim_print("Character: SYUURAN")
    time.sleep(1)
    anim_print("Description: Syuuran is scared and kinda alone. There's not much else to say.")
    time.sleep(1)
    anim_print("Health: 100")
    anim_print("Attack: 4")
    anim_print("Special Ability: Persuasion")
    anim_print("Weakness: Mice")
    time.sleep(1.5)
    print()

    anim_print(f"Character: {username.title()}")
    time.sleep(1)
    anim_print(f"Description: {username.title()} is {adjective_01.lower()} and kinda {adjective_02.lower()}. There's not much else to say.")
    time.sleep(1)
    anim_print("Health: 100")
    anim_print(f"Attack: {attack:.0f}")
    anim_print(f"Special Ability: {ability.title()}")
    anim_print(f"Weakness: {weakness.title()}")
    time.sleep(2)
    print()
    correct_choice = False
    while not correct_choice:
            anim_print("Who are you?")
            character_choice = anim_input("Choose wisely: ").capitalize()
            if character_choice == username.capitalize():
                correct_choice = True
            elif character_choice == "Syuuran" or character_choice == "Ana":
                correct_choice = False
                anim_print("Sorry! This choice is not available for the demo! Look for updates in the future!")
            else:
                correct_choice = False
                anim_print("This is not what was asked of you.")

    if character_choice == username:
        health = 100
        attack = 6
        ana_special_ability = "observation"
        ana_weakness = "spiders"
        anim_print("Okay...")
        time.sleep(1)
        anim_print("Creating scenario...", delay=0.135)
        time.sleep(1.5)
        anim_print("Importing sounds...",delay=0.135)
        time.sleep(2)
        anim_print("Loading...", delay=0.135)
        time.sleep(2)
        print()
        trees_rustle.play(loops=-1)
        trees_rustle.set_volume(0.125)
        anim_print("You open your tired eyes and look around the room.")
        anim_print("The room you're in resembles a huge metal box, but time and nature started eating away at it.")
        anim_print("Now, the large bolts that kept the room in one piece are starting to rust.")
        anim_print("And the metal plating that used to be the walls are warped and falling apart.")
        anim_print("Sunlight seeps through the cracks and gaps in the walls, and a strong smell of rain overwhelms your senses.")
        anim_print("You can hear the faint squeak of mice in the distance along with the rustling of trees.")
        anim_print("Despite there being a metal table in the room with a metal chair, you are lying on the cold, wet floor.")
        anim_print("Your clothes smell like mildew and moss now.")
        anim_print("What do you do? Leave or look around?")
        response = True
        while response:
            leave_or_look = anim_input("Leave or look: ").capitalize()
            if leave_or_look == "Look":
                leave_or_look = False
                anim_print("You look at your surroundings.")
                anim_print("You look at the table and chair in front of you.")
                anim_print("You can't really remember anything about yourself which makes you feel uneasy.")
                anim_print("But you have a faint memory of standing on a chair once.")
                anim_print("You slipped and fell.")
                anim_print("You look around the room a little more.")
                time.sleep(1)
                anim_print("You notice moss is slowly but surely inching its way along the walls.")
                anim_print("In time, the walls will inevitably be covered in it.")
                time.sleep(.75)
                anim_print("You see that fresh and rotting leaves adorn the floor of the metal room closest to the broken wall.")
                anim_print("Leaves must have fallen into the room from outside.")
                time.sleep(.75)
                anim_print("You look across the room.")
                time.sleep(.10)
                anim_print("There is a door...")
                anim_print("Maybe you'll be able to leave. And hopefully find a way home.")
                anim_print("Maybe by time you leave, you'll remember where home is.")
                time.sleep(1)
                anim_print("Your legs feel numb as you stand, and you stumble your way towards the door.")
                anim_print("Once closer, you find that the handle of the door is completely missing, and the door is cracked open slightly.")
                anim_print("You slip your fingers into the crack between the wall and the door...")
                time.sleep(2)
                anim_print("...but the door is too heavy to open.")
                anim_print("Maybe there is something in the room that can help you.")
                break
            if leave_or_look == "Leave":
                leave_or_look = False
                anim_print("You decide to try and find a way out of the metal box and you notice a door across the room.")
                anim_print("Your legs feel numb as you stand, and you stumble your way towards the door.")
                anim_print("Once closer, you find that the door is cracked open slightly.")
                anim_print("You slip your fingers into the crack between the wall and the door...")
                time.sleep(2)
                anim_print("...but the door is too heavy to open.")
                anim_print("Maybe you should look around for something to help you.")
                break
            else:
                leave_or_look = True
        anim_print("Looking around the room, you notice several places to investigate.")
        anim_print("Where do you look? The pile of leaves, under the table, or the hole in the wall?")
        seen_inputs = set()
        all_choices = {"leaves", "table", "wall"}
        looking = True
        while looking:
            if seen_inputs == all_choices:
                looking = False
                elevated_surface = False
                break
            to_look = anim_input("You look at the 'leaves', 'table', or 'wall': ").lower()
            if to_look in seen_inputs:
                looking = True
                anim_print("You already looked there. Look somewhere else.")
            else:
                seen_inputs.add(to_look)
                if to_look == "leaves":
                    looking = True
                    anim_print("As your legs start to feel better, you make your way towards the pile of leaves.")
                    anim_print("You reach down to move the leaves around and see if you find something.")
                    anim_print("As your hands are in the wet, mushy pile of leaves, you find a crowbar.")
                    anim_print("It is covered in rust.")
                    anim_print("A rusty crowbar was added to your inventory.")
                    with open(filename, 'a', newline='') as file:
                        new_item = "rusty crowbar"
                        attack = 8
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, attack])
                    if seen_inputs != all_choices:
                        anim_print("Maybe there's something else here.")
                elif to_look == "table":
                    looking = True
                    anim_print("You walk back over to the table you woke up next to.")
                    anim_print("When you crouch down to look under the table...")
                    anim_print("You see nothing but scratches on the floor from the table legs along with greenish coloured water stains.")
                    anim_print("When you get up, you hit your head on the table.")
                    anim_print("You found nothing but a headache.")
                    time.sleep(1)
                    anim_print("A headache was added to your inventory.")
                    with open(filename, 'a', newline='') as file:
                        new_item = "headache"
                        attack = 15
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, attack])
                    anim_print("As you stand there thinking about your headache, you hear something fall to the floor.")
                    anim_print("You look under the table again and see a strange, metal key on the floor.")
                    anim_print("It must have been taped to the underside of the table.")
                    anim_print("A strange, metal key was added to your inventory.")
                    with open(filename, 'a', newline='') as file:
                        new_item = "strange, metal key"
                        attack = 3
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, attack])
                    if seen_inputs != all_choices:
                        anim_print("Maybe there's something else here.")
                elif to_look == "wall":
                    looking = True
                    anim_print("You go towards the wall where the light from the outside world is shining through.")
                    trees_rustle.set_volume(0.225)
                    anim_print("The smell of rain is stronger closer to the wall, " + 
                    "and you stand on the leaves that had fallen through the hole in the wall.")
                    anim_print("They uncomfortably crunch and squish underneath your feet.")
                    anim_print("You don't hear any rain though. Just the rustling of trees from the wind.")
                    anim_print("It must have rained recently. You should really get out of there before it starts to rain again.")
                    anim_print("Now that you're so close to the wall, you notice a window near the ceiling.")
                    anim_print("You think that maybe you can get out. If only you can reach the window.")
                    anim_print("Maybe there is something in the room that you can use to reach the window.")
                    elevated_surface = True
                    while elevated_surface:
                        grab_item = anim_input("You have an idea to grab something to stand on and you grab the... ").lower()
                        if grab_item == "table":
                            anim_print("You go over to the table to see if you can grab it and drag it to the wall.")
                            anim_print("But once you reach the table and try moving it, you quickly find that the table is way too heavy to move.")
                            anim_print("You look down and see that it's bolted to the floor...")
                            time.sleep(1)
                            anim_print("Maybe something that's next to the table can help you reach the window.")
                            time.sleep(1)
                        elif grab_item == "chair":
                            elevated_surface = False
                            anim_print("You grab the chair and set it on the floor underneath where the window is.")
                            anim_print("You put one foot on the chair and then the other and carefully climb up.")
                            anim_print("You almost fall due to the floor being slippery.")
                            anim_print("Once higher up, you find that there are thick, metal bars along the window.")
                            anim_print("They have yet to be claimed by rust, so they are unlikely to break.")
                            anim_print("But the walls themselves are cracking and you might be able to break off some of the bars from the wall and escape.")
                            anim_print("You grab one of the slick bars and pull.")
                            time.sleep(1.5)
                            breaking_wall.play()
                            anim_print("The wall cracks a bit.")
                            time.sleep(1.5)
                            breaking_wall.play()
                            anim_print("You pull at the bar again.")
                            time.sleep(1.5)
                            breaking_wall.play()
                            anim_print("And again...", delay=0.135)
                            time.sleep(1.5)
                            breaking_wall.play()
                            anim_print("You pull at the bar a final time and the chair slides across the floor.")
                            time.sleep(1.5)
                            player_falls.play()
                            trees_rustle.set_volume(0)
                            anim_print("You fall...",delay=0.25)
                            time.sleep(2)
                            trees_rustle.set_volume(0.125)
                            anim_print("When you open your eyes, you look around.")
                            anim_print("It's a little darker outside. You must have been knocked out for a while.")
                            anim_print("When you try to get up, your foot hits something.")
                            anim_print("There is a metal bar lying on the floor at your feet along with pieces of the wall.")
                            anim_print("A metal bar was added to your inventory.")
                            with open(filename, 'a', newline='') as file:
                                new_item = "thick, metal bar"
                                attack = 12
                                csv_writer = csv.writer(file)
                                csv_writer.writerow([new_item, attack])
                            time.sleep(1)
                            anim_print("You think its best to use the bar to open the door rather than climb on the chair and fall again.")
                            anim_print("You don't want to get hurt...")
                            time.sleep(1)
                            anim_print("Oh.")
                            time.sleep(1)
                            anim_print("The chair is broken anyway.")
                            anim_print("You didn't notice that the legs of the chair were rusty.")
                            time.sleep(1)
                            if seen_inputs != all_choices:
                                anim_print("Maybe there's something else here.")
                        else:
                            elevated_surface = True
                            anim_print("You don't know if that will work.")
                else:
                    anim_print("That is not what was asked.")
                    time.sleep(1)
        anim_print("After you've looked around the room, you go back over to the door.")
        anim_print("You've found some things that could help you open the door.")
        anim_print("To view your inventory, press E. You can only view your inventory when prompted.")
        anim_print("Type anything else to close prompt.")
        inventory = True
        while inventory:
            print()
            view_inventory = anim_input("View your inventory? ").capitalize()
            print()
            if view_inventory == "E":
                inventory = True
                with open(filename, 'r') as collected_items:
                    choice = csv.reader(collected_items)
                    for row in choice:
                        new_item, attack = row
                        print(f"{new_item.title()}: {attack} damage")
            else:
                inventory = False
                anim_print("Verywell then...")
                time.sleep(1)
        anim_print("What can help you pry open the door?")
        opening_door = True
        while opening_door:
            inventory = True
            with open(filename, 'r') as collected_items:
                reader = csv.reader(collected_items)
                items = list(reader)
                nonexistent_item = True
                while nonexistent_item:
                    item_to_remove = anim_input("What are you going to use? ").strip().capitalize()
                    item_exists = any(row[0].capitalize() == item_to_remove for row in items)
                    if item_exists:
                        nonexistent_item = False
                        items = [row for row in items if row[0].capitalize() != item_to_remove]
                        with open(filename, 'w', newline='') as collected_items:
                            writer = csv.writer(collected_items)
                            writer.writerows(items)
                    else:
                        nonexistent_item = True
                        anim_print(f"{item_to_remove} is not in your inventory.")
                        print()
                if item_to_remove == "Rusty crowbar".capitalize():
                    opening_door = True
                    anim_print("You try to use the rusty crowbar to pry open the door.")
                    anim_print("But due to its significant amount of rust...")
                    anim_print("It breaks.")
                elif item_to_remove == "thick, metal bar".capitalize():
                    opening_door = False
                    anim_print("You try to use the thick, metal bar to pry open the door.")
                    anim_print("And despite your limited strength, the bar was strong enough to pry open the door just enough for you to slip through without the bar breaking.")
                    anim_print("Unfortunately the bar is bent.")
                    time.sleep(1)
                    with open(filename, 'a', newline='') as file:
                        new_item = "bent, metal bar"
                        attack = 9
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, attack])
                elif item_to_remove != "Thick, metal bar" and item_to_remove != "Rusty crowbar":
                    opening_door = True
                    anim_print(f"You try to use the {item_to_remove} to pry open the door.")
                    anim_print("It does not work.")
                    with open(filename, 'a', newline='') as file:
                        new_item = item_to_remove
                        attack = 2
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, attack])
                    anim_print(f"Your {item_to_remove} is now damaged, and will be weaker if used as a weapon.")
        anim_print("Finally, with the door wedged open, you can leave the room.")
        time.sleep(1)
        print()
        anim_print("The door was too heavy to open all the way, so you have to carefully squeeze out of the room.")
        anim_print("The cold metal of the wall wipes against your face as the edge of the door presses into your back.")
        anim_print("Once you finally are free of the door's grasp, you feel a sharp sting in your shoulder.")
        anim_print("You look down at your shoulder and find that it's cut.")
        anim_print("Blood from your shoulder drips down your arm and onto the concrete ground.")
        anim_print("Concrete was not something you were expecting to find under your feet.")
        anim_print("You were expecting the welcoming dirt of the earth.")
        anim_print("But as you look around, you find that you're nowhere near the ground.")
        anim_print("And it's starting to rain.")
        trees_rustle.stop()
        city_rain.play(-1)
        city_rain.set_volume(.5)
        time.sleep(1)
        anim_print("You look around and see that you're in an outdoor, concrete hallway of a sort.")
        anim_print("There is a cracked concrete wall that protects anyone from falling over the edge.")
        anim_print("And after you walk over and look over the edge, you see nothing but the tops of trees.")
        anim_print("The trees are tall enough to where you can touch the tips of them if you reach out.")
        anim_print("You can't see the ground, and assume that it's a long way down.")
        anim_print("It's best to avoid looking over the edge for too long. You don't want to fall.")
        time.sleep(.5)
        anim_print("You back up a bit and continue to look around.")
        anim_print("You look back at the room you just left and notice that the outside of the door has something written on it.")
        anim_print("You can't tell what language it is.")
        time.sleep(.5)
        anim_print("You start to look around again...")
        anim_print("But not long after escaping your prison, the distant squeaks that you heard from inside the room quickly grow louder.")
        anim_print("In the distance, you see a large figure.")
        anim_print("The closer it gets, the more you can make out what it is.")
        anim_print("Those squeaks weren't from mice!")
        anim_print("It's a huge, mutated rat!")
        anim_print("Surprised, you are unable to avoid it!")
        anim_print("It must have been attracted by the smell of your blood!")
        time.sleep(1)
        city_rain.stop()
        anim_print("Loading...", delay=0.135)
        first_fight.easy_fight()
        city_rain.play(loops=-1)
        city_rain.set_volume(.5)
        anim_print("You were able to defend yourself from the rat, and it drops dead.")
        anim_print("You are able to retrieve clean bandages from it.")
        time.sleep(2)
        anim_print("What an odd thing to find on a rat...")
        time.sleep(1.25)
        anim_print("Clean bandages were added to your inventory.")
        with open(filename, 'a', newline='') as file:
            new_item = "clean bandages"
            attack = 0
            csv_writer = csv.writer(file)
            csv_writer.writerow([new_item, attack])
        anim_print("Congradulations on your first victory!")
        anim_print("You can now view your statistics when you view your inventory.")
        anim_print("To keep things simple, it will still be refered to as 'inventory'.")
        anim_print("Would you like to view your inventory before you continue your journey?")
        inventory = True
        while inventory:
            print()
            view_inventory = anim_input("View your inventory (E)? ").capitalize()
            print()
            if view_inventory == "E":
                with open(statistics, 'r') as file:
                    anim_print("YOUR STATISTICS")
                    time.sleep(1)
                    choice = csv.reader(file)
                    stats = {}
                    for row in choice:
                        new_stat, kill_power = row
                        stats[new_stat] = kill_power
                    for key in ["your name", "your description", "your ability", "your weakness"]:
                        if key in stats:
                            if key == "your description":
                                words = stats[key].strip("()").replace("'", "").split(", ")
                                print(f"{key.title()}: You are {words[0]} and kinda {words[1]}. There is not much else to say.")
                            else:
                                print(f"{key.title()}: {stats[key].capitalize()}")
                            time.sleep(1)
                    if "your health" in stats:
                        print(f"Your Health: {stats['your health'].capitalize()}")
                        time.sleep(1)
                    if "your attack" in stats:
                        print(f"Your Attack: {stats['your attack'].capitalize()}")
                        time.sleep(1)
                with open(filename, 'r') as collected_items:
                    print()
                    anim_print("YOUR INVENTORY")
                    choice = csv.reader(collected_items)
                    for row in choice:
                        new_item, attack = row
                        print(f"{new_item.title()}: {attack} damage")
                        time.sleep(1)
            else:
                inventory = False
                anim_print("Verywell then...")
                time.sleep(1)
        anim_print("Your arm still aches after the attack and you decide to use the bandage that you just got from the rat.")
        time.sleep(1)
        item_to_remove = "clean bandages"
        with open(filename, 'r') as collected_items:
            reader = csv.reader(collected_items)
            items = list(reader)
            items = [row for row in items if row[0].capitalize() != item_to_remove]
        with open(filename, 'w', newline='') as collected_items:
            writer = csv.writer(collected_items)
            writer.writerows(items)
        anim_print("The bandages were removed from your inventory.")
        time.sleep(1)
        anim_print("It's best if you get out of this area.")
        anim_print("You make your way down the hallway of the building you just came from.")
        anim_print("The smell of rain overwhelms your senses.")
        anim_print("You hope that you'll get used to it soon.")
        anim_print("As you reach the end of the hallway, you see two separate metal doors.")
        anim_print("The left door looks like it leads to the rest of the complex.")
        anim_print("The right door might lead to the stairs.")
        anim_print("Which one do you choose?")
        choose_door = True
        while choose_door:
            door = anim_input("Left or right?: ").lower()
            if door == "left":
                choose_door = True
                anim_print("You reach your hand out to open the door on the left...")
                anim_print("But its locked...")
                anim_print("You think to yourself 'Maybe I can unlock this after the game is completed...'")
                anim_print("Whatever that means...")
                # when you write this part, import the scene as a custom [NAME_HERE].py file.
                # the imported file MUST end with the character at the left and right door.
                # the character automatically leaves out the right door after exploring everywhere.
                time.sleep(1)
            elif door == "right":
                choose_door = False
                anim_print("You reach your hand out to open the door on the right...")
                anim_print("And you were right.")
                anim_print("Behind the door is a stairwell.")
                time.sleep(1)
            else:
                choose_door = True
                anim_print("What?", delay=0.1)
                time.sleep(.5)
        anim_print("You slowly make your way down the concrete stairwell.")
        anim_print("The metal railing feels smooth and cold against your skin as you take step after step towards freedom.")
        anim_print("You feel as if you've walked twenty flights to reach the bottom, but you finally make it to the bottom.")
        anim_print("Once at ground level, you take in your surroundings.")
        anim_print("You are surrounded by a huge, beautiful forest with a winding, muddy path directly ahead.")
        anim_print("The combination of wind and rain brings forth a beautiful melody that sways through the trees.")
        time.sleep(1)
        anim_print("To your left, there are steep, sharp rocks that line the edge of what you think could be mountains.")
        anim_print("And to your right, there is a dense forest. In the far distance, you think that you can see a cliff face.")
        time.sleep(1)
        anim_print("You turn around and look at the building that you just escaped from.")
        anim_print("It's concrete and metal form is carefully merged with the cliffside.")
        anim_print("As you scan the face of the building, you can't even see the room you were in because the trees block your view.")
        time.sleep(1)
        anim_print("As the grass gently rubs against your bare ankles, and the rain soaks your socks...")
        anim_print("You think to yourself that you should keep moving. You shouldn't stay in the rain for too long.")
        anim_print("You don't want to get sick.")
        time.sleep(1)
        anim_print("Knowing that you are almost entirely surrounded by walls, whether manmade or otherwise...")
        time.sleep(1)
        anim_print("There is no where to go but forward.")
        time.sleep(4)
        print()
        anim_print("CHAPTER ONE - CITY OF SEONA (demo version)",delay=0.1)
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("finish the prologue")]
        for item in items_to_add:
            if item not in inventory:
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
            else:
                print()
        time.sleep(2)
        anim_print("You look ahead of you at the trail.")
        anim_print("This is the only way to go.")
        anim_print("All trails lead to somewhere safe, right?")
        anim_print("If you go down this trail, maybe you can find some help.")
        anim_print("Maybe someone can help you find home.")
        anim_print("You continue your journey, unfettered by the rain, and you head down the trail up ahead.")
        anim_print("The mud sucks at your shoes, threatening to pull them off.")
        anim_print("But you still continue walking.")
        time.sleep(1)
        anim_print("After about an hour or so of walking, you begin to get tired.")
        anim_print("You start to think of whether this trail actually leads somewhere or not.")
        anim_print("You consider turning around and going back to that steril building you woke up in.")
        anim_print("At least it was much drier.")
        anim_print("As soon as those doubts of continuing on started popping in your head, you see something in the distance.")
        anim_print("A wooden trail sign.")
        time.sleep(1)
        anim_print("Excited to see something other than trees, you rush up to the sign.")
        anim_print("You don't care that one of your shoes came off in the mud.")
        anim_print("At least this is hope that you can find out if you're going in the right direction!")
        anim_print("As you walk up to the sign, you notice that the path in front of your forks two ways.")
        anim_print("The path to the left rises while the other falls.")
        time.sleep(1)
        anim_print("The sign is shaped like an arrow with two points going in opposite directions.")
        anim_print("The Left Sign: 'The Seona Misty Trails'")
        time.sleep(1)
        anim_print("The Right Sign: 'City of Seona'")
        time.sleep(1)
        anim_print("Following the left sign means that you'll head deeper into the mountains...")
        anim_print("That might be dangerous.")
        anim_print("No one knows where you are.")
        time.sleep(1)
        anim_print("Following the right sign means that you'll eventually end up in a town called Seona.")
        anim_print("The town is only 2 miles away.")
        time.sleep(1)
        anim_print("Which way are you going to go?")
        left_or_right = True
        while left_or_right:
            trail_choice = anim_input("You choose to go to the... ").lower()
            if trail_choice == "left":
                left_or_right = True
                anim_print("Sorry! This choice is not available for the demo! Look for updates in the future!")
                time.sleep(1)
                # when updating the demo, custom import this scene as a .py file.
            elif trail_choice == "right":
                anim_print("You decide to take the right path and go towards the city of Seona.")
                anim_print("But first, you go back to retrieve your other shoe from the mud.")
                anim_print("Now that you have both of your shoes, you continue on your journey!")
                left_or_right = False
                break
            else:
                left_or_right = True
                anim_print("That isn't a choice.")
                time.sleep(1)
        anim_print("Loading...",delay=0.135)
        time.sleep(2)
        anim_print("You continue down the trail, not knowing what lies ahead...")
        anim_print("But then you hear something rustling in the underbrush.")
        anim_print("You think that it could just be the wind and rain moving the trees, but you're not sure.")
        anim_print("Be careful.")
        time.sleep(1)
        anim_print("You have no idea what could be out here with you.")
        time.sleep(1)
        anim_print("Type 'M' to move forward.")
        walking_in_woods = True
        count = 0
        while walking_in_woods:
            move_forward = anim_input("Continue on (M)? ").upper()
            while count < 6:
                chance = random.randint(1, 100)
                if move_forward == 'M':
                    if chance <= 15 or chance >= 75 or count == 4:
                        anim_print("You hear the rustling of plants grow louder as something approaches you!")
                        time.sleep(1)
                        city_rain.stop()
                        random_fight.random_enemy()
                        city_rain.play()
                        anim_print("You were safely able to fend off your attacker!")
                        anim_print("You should hurry up and get off of this trail.")
                        anim_print("You're bound to be attacked again.")
                        time.sleep(1)
                        move_forward = False
                        break
                    else:
                        anim_print("You safely move forward along the trail.")
                        time.sleep(1)
                        count += 1
                        if count == 6:
                            anim_print("And as you reach the end of the trail, you see another sign written in huge, capital letters.")
                            anim_print("'WELCOME TO SEONA CITY'")
                            walking_in_woods = False
                            break
                        else:
                            anim_print("A sign that you just passed says that you've traveled a third of a mile.")
                            anim_print("You best hurry to the town.")
                            move_forward = False
                            break
                else:
                    anim_print("You stop to take in your surrounding instead of moving forward.")
                    anim_print("But you hear something rush up from behind you!")
                    anim_print("You have no time to react!")
                    random_fight.random_enemy()
                    time.sleep(1)
                    anim_print("You were safely able to fend off your attacker!")
                    anim_print("But in your despiration to get away...")
                    time.sleep(1)
                    anim_print("You ran a third of a mile in the wrong direction.")
                    time.sleep(1)
                    count -= 1
                    move_forward = False
                    break
        anim_print("The entrance to the city is not as welcoming as you thought it would be, though.")
        anim_print("The streets are cracked and broken up, and the building are in even worse condition.")
        anim_print("Weeds have long taken over any surface they could wrap themselves around.")
        anim_print("Mold spots the shop signs and any porous surface within its reach.")
        time.sleep(1)
        anim_print("Does anyone even live here anymore?")
        time.sleep(1)
        anim_print("You sure hope so, but it doesn't seem like it.")
        anim_print("You walk a couple of steps into town when you see another sign on the street corner.")
        anim_print("You cross the deteriorating street to look at the sign...")
        anim_print("...but upon further inspection, most of the words and pictures are eaten away by mold and time.")
        anim_print("The title of the sign reads: 'Downtown Seona Scramble'.")
        anim_print("This is a map of Seona's downtown area!")
        anim_print("There were dozens of places to visit here, but on the map, its reduced to only a few.")
        anim_print("Maybe if you use this map to look around the city, you can find out what happened here.")
        anim_print("And maybe you can find some help.")
        anim_print("Some of the places still marked on the map are the market, the middle school, the hospital, the playground, and Seona pond.")
        anim_print("Where should you go first?")
        seen_towns = set()
        all_choices = {"market", "school", "hospital", "playground", "pond"}
        explore = True
        while explore:
            if seen_towns == all_choices:
                explore = False
                deciding = False
                inventory = False
                count = False
                walking_in_woods = False
                exploring_floor_three = False
                break
            to_explore = anim_input("You decide to explore the market, school, hospital, playground, or pond: ").lower()
            if to_explore in seen_towns:
                explore = True
                anim_print("You already looked there. Look somewhere else.")
            else:
                seen_towns.add(to_explore)
                if to_explore == "market":
                    city_rain.stop()
                    anim_print("You decide to head towards the market.")
                    anim_print("According to the map, it's not too far from where you are now.")
                    anim_print("As you walk down the streets, you really get a chance to see how worn down the city is.")
                    anim_print("You are surprised that buildings are still standing.")
                    anim_print("The only thing that is the most recognizable are the glass skyscrapers in the distance.")
                    anim_print("But they are way too far away to reach.")
                    anim_print("You look down at the ground for a moment as you walk.")
                    anim_print("And you notice smudges, dirty papers are scattered all over the roads.")
                    anim_print("You can't make out what they say.")
                    time.sleep(1)
                    anim_print("You pass several buildings on your way to the market.")
                    ambushed = random.choice([True, False])
                    if ambushed == True:
                        anim_print("But you suddenly feel something run into you!")
                        anim_print("You turn and you see it!")
                        random_fight.random_enemy()
                        anim_print("Luckily you were able to get away with your life!")
                        anim_print("And you continue down the street, a little more aware of your surroundings, until you see the market.")
                    if ambushed == False:
                        anim_print("You pass an old laundromat, a cleaners, and even several building of what you think could have been restaurants.")
                        anim_print("But you safely make it to the market.")
                    anim_print("As you stand at the door of the market, you are reluctant to touch the door to go inside.")
                    anim_print("The door is covered in a gross, shiny slime.")
                    anim_print("You have no idea what it could be.")
                    anim_print("But you must continue on.")
                    anim_print("You place both of your hands on the door.")
                    anim_print("The sludge feels as if it seeps into your skin.")
                    anim_print("It feels even worse under your nails.")
                    anim_print("You give the door a good push and the hinges on the door give way.")
                    anim_print("The entire door falls to the ground with a thud.")
                    anim_print("You hope that that didn't attract any unwanted attention.")
                    time.sleep(1)
                    anim_print("You step inside of the market.")
                    anim_print("The muffled crunch of rotting boxes and packaging is heard from under your feet.")
                    anim_print("You look up at the knocked over and neglected shelves that you assume once held dry goods.")
                    anim_print("You look around the aisles and find a paper nustled in the shelving.")
                    anim_print("You pull the paper out from underneath some exploded, oozing cans of beans.")
                    anim_print("As you straighten the paper to read it, you recognize it from somewhere.")
                    anim_print("It looks like one of the papers that you saw lying in the street!")
                    anim_print("At least you're able to read this paper better despite being stained with food waste.")
                    time.sleep(1)
                    anim_print("It's a public service announcement...")
                    time.sleep(1)
                    anim_print("The city was evacuated...")
                    time.sleep(1)
                    anim_print("You can't quite make out the date, but this notice was issued sometime in August.")
                    time.sleep(1)
                    anim_print("You don't remember hearing anything about an evacuation.")
                    time.sleep(1)
                    anim_print("You don't remember much at all...")
                    time.sleep(3)
                    anim_print("You shove the paper into your pocket.")
                    time.sleep(1)
                    anim_print("Maybe it'll be useful later even if you can't read half of it...")
                    time.sleep(1)
                    anim_print("A PSA flier was added to your inventory.")
                    with open(filename, 'a', newline='') as file:
                        new_item = "public service announcement"
                        attack = 1
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, attack])
                    time.sleep(1)
                    anim_print("You continue to look around the market.")
                    anim_print("There has to be something else here.")
                    anim_print("You round the corner, steping over overgrown trees and plant life.")
                    anim_print("But you hear something rustling around in the meat section of the market.")
                    anim_print("Should you leave or investigate?")
                    anim_print("If you leave, you can't come back.")
                    deciding = True
                    while deciding:
                        leave_or_stay = anim_input("You decide you 'leave' or 'investigate': ").lower()
                        if leave_or_stay == "leave":
                            anim_print("You don't want to take your chances and you decide to leave.")
                            anim_print("You quietly turn around and head in the other direction.")
                            anim_print("You don't want to risk being attacked for a helpful item that might not even be in the other room.")
                            anim_print("Once you sneak out of the aisle, you find something blocking your way.")
                            random_fight.random_enemy()
                            anim_print("You successfully were able to fend off your attacker!")
                            anim_print("It's best to not stay here. Some other monsters could be attracted by the sound of the fight.")
                            anim_print("Once you leave the market, you find yourself outside.")
                            anim_print("Where should you go next?")
                            deciding = False
                            break
                        if leave_or_stay == "investigate":
                            anim_print("You decide to be brave and investigate the source of the mysterious sound.")
                            anim_print("You pick up a large stick that you find lying on the floor, and you grasp it tightly in your hands.")
                            anim_print("You're nervous about what you might find waiting for you around the corner.")
                            anim_print("Nevertheless, you pause before bursting around the corner.")
                            anim_print("You swing as hard as you can towards the source of the sound!")
                            anim_print("But you only ended up hitting a couple of small rats that were sitting on the shelves, looking for food.")
                            anim_print("Regular rats weren't what you were expecting...")
                            anim_print("But you're happy it wasn't anything worse...")
                            time.sleep(1)
                            anim_print("You look around the room you're in to see if anything can be salvaged.")
                            anim_print("And you're in luck!")
                            anim_print("Across the room, you see a butchers knife sitting on the counter.")
                            anim_print("You walk over to the knife and grab it.")
                            anim_print("It's pretty old, but it can still be great as a weapon if you get attacked again.")
                            anim_print("A butcher's knife was added to your inventory.")
                            with open(filename, 'a', newline='') as file:
                                new_item = "butcher's knife"
                                attack = 35
                                csv_writer = csv.writer(file)
                                csv_writer.writerow([new_item, attack])
                            time.sleep(1)
                            anim_print("You spend some more time looking around the market, but there isn't much else that could be useful to you.")
                            anim_print("You turn to leave the store when something blocks your way.")
                            anim_print("Maybe now is your chance to test out that new knife of yours.")
                            random_fight.random_enemy()
                            anim_print("You successfully were able to fend off your attacker!")
                            anim_print("It's best to not stay here. Some other monsters could be attracted by the sound of the fight.")
                            anim_print("Once you leave the market, you find yourself outside.")
                            anim_print("Where should you go next?")
                            deciding == False
                            break
                        else:
                            anim_print("This is not what was asked of you.")
                            time.sleep(1)
                            deciding == True
                elif to_explore == "school":
                    city_rain.stop()
                    anim_print("You decide to head towards the middle school.")
                    anim_print("According to the map, it's not too far from where you are now.")
                    anim_print("As you walk down the streets towards the school, you think back on some of your memories.")
                    anim_print("You can't remember much.")
                    anim_print("You don't even remember whether you've been to school or not.")
                    anim_print("All you know is that you have to find a way home.")
                    anim_print("That is your guiding intuition.")
                    time.sleep(1)
                    anim_print("You pass several buildings on your way to the school.")
                    ambushed = random.choice([True, False])
                    if ambushed == True:
                        anim_print("But you suddenly feel something run into you!")
                        anim_print("You turn and you see it!")
                        random_fight.random_enemy()
                        anim_print("Luckily you were able to get away with your life!")
                        anim_print("And you continue down the street, a little more aware of your surroundings, until you see the market.")
                    if ambushed == False:
                        anim_print("You pass an diner, a several, and a couple of delapitated apartments.")
                        anim_print("But you safely make it to the school.")
                    anim_print("You stand outside of the school, wondering what could await you inside.")
                    anim_print("You walk down the school's front courtyard to reach the doors.")
                    time.sleep(1)
                    anim_print("The doors are already open when you get to them.")
                    time.sleep(1)
                    anim_print("Be careful.")
                    time.sleep(1)
                    anim_print("You step inside of the school and you are immediately overwelmed by the smell of mold.")
                    anim_print("The hallways are relatively empty aside from the occasional debris.")
                    anim_print("And the school looks better on the inside than you thought that it would.")
                    anim_print("You just can't get over the smell of mold.")
                    anim_print("You know that you don't want to stay here too long.")
                    time.sleep(1)
                    anim_print("You walk down the hallways expecting to see other people around, but it's eerily silent.")
                    anim_print("Too silent.")
                    anim_print("As you continue walking, you pass a classroom with an open door.")
                    ambushed = random.choice([True, False])
                    if ambushed == True:
                        anim_print("And something jumps out at you!")
                        random_fight.random_enemy()
                        anim_print("Luckily you were able to get away with your life!")
                        anim_print("Maybe you shouldn't just poke your head into classrooms like that.")
                        time.sleep(1)
                    if ambushed == False:
                        anim_print("You peek inside but see no one there.")
                        anim_print("You decide to walk inside the classroom, and you notice that there are some bags lying around the room.")
                        anim_print("You look through the bags, hoping that no one would mind since they're all obviously gone...")
                        anim_print("And you find a tape recorder.")
                        anim_print("It is worn and dirty looking, but maybe it'll still work.")
                        anim_print("There is nothing inside.")
                        anim_print("A tape recorder was added to your inventory.")
                        with open(filename, 'a', newline='') as file:
                            new_item = "tape recorder"
                            attack = 1
                            csv_writer = csv.writer(file)
                            csv_writer.writerow([new_item, attack])
                        time.sleep(1)
                        anim_print("Maybe you can find an important tape for it.")
                        time.sleep(1)
                    anim_print("You continue down the hallways until you reach the cafeteria.")
                    anim_print("You would have taken a different turn, but most of the hallways were blocked off by broken trees or stacked up desks.")
                    anim_print("You don't want to think about why people stacked those desks like they did.")
                    anim_print("You walk into the cafeteria.")
                    ambushed = random.choice([True, False])
                    if ambushed == True:
                        anim_print("And you hear something!")
                        time.sleep(1)
                        random_fight.random_enemy()
                        anim_print("Luckily you were able to get away with your life!")
                        time.sleep(1)
                    if ambushed == False:
                        anim_print("And you hear something!")
                        time.sleep(1)
                        anim_print("Oh.")
                        time.sleep(1)
                        anim_print("It was just a bird.")
                        anim_print("A very noisy bird...")
                        time.sleep(1)
                    anim_print("You continue into the cafeteria, pushing the door open a little bit more with your body.")
                    anim_print("And you see that the whole room is a complete mess.")
                    anim_print("From a glance, you see that there is nothing of value that you can get here.")
                    anim_print("So, you turn back and leave the cafeteria.")
                    anim_print("You never forgot about the mold smell.")
                    anim_print("In fact it's even gotten worse.")
                    anim_print("Should you leave?")
                    anim_print("If you choose to leave, you can't come back.")
                    deciding = True
                    while deciding:
                        leave_or_stay = anim_input("You decide you 'leave' or 'investigate': ").lower()
                        if leave_or_stay == "leave":
                            anim_print("You don't want to get a serious headache from the smell...")
                            anim_print("So, you turn around and go back the way you came.")
                            anim_print("On the way back down the hallway, you notice something that you missed.")
                            time.sleep(1)
                            anim_print("A paper cutter blade was added to your inventory.")
                            with open(filename, 'a', newline='') as file:
                                new_item = "paper cutter blade"
                                attack = 12
                                csv_writer = csv.writer(file)
                                csv_writer.writerow([new_item, attack])
                            time.sleep(1)
                            anim_print("You finally reach the front doors of the school, but when you turn to leave the school...")
                            anim_print("...something blocks your way.")
                            random_fight.random_enemy()
                            anim_print("You're lucky to still be alive!")
                            anim_print("You should hurry up and leave.")
                            time.sleep(1)
                            anim_print("Once outside where the smell of mold is noticeably less, you take a deep breath of fresh air.")
                            time.sleep(1)
                            anim_print("Where should you go next?")
                            deciding = False
                            break
                        if leave_or_stay == "investigate":
                            anim_print("You decide to tough it out.")
                            anim_print("Maybe you'll find something good in here that can really help you.")
                            time.sleep(1)
                            anim_print("You walk down the hallway of the school, taking a different turn when you reach a block in the path...")
                            anim_print("You feel like you were in that school all day, but you were able to get two things!")
                            time.sleep(1)
                            anim_print("A pair of scissors were added to your inventory.")
                            with open(filename, 'a', newline='') as file:
                                new_item = "pair of scissors"
                                attack = 8
                                csv_writer = csv.writer(file)
                                csv_writer.writerow([new_item, attack])
                            time.sleep(1)
                            anim_print("A yard stick was added to your inventory.")
                            with open(filename, 'a', newline='') as file:
                                new_item = "yard stick"
                                attack = 3
                                csv_writer = csv.writer(file)
                                csv_writer.writerow([new_item, attack])
                            time.sleep(1)
                            anim_print("You'd spend some more time looking around the school, but there isn't much else that could be useful to you.")
                            anim_print("You turn to leave the school when something blocks your way.")
                            random_fight.random_enemy()
                            anim_print("As you fought your attacker, you ended up running somewhere behind the school!")
                            anim_print("There is a dense, wooded area behind the school.")
                            anim_print("While you're here, you decide to look around.")
                            anim_print("Press 'M' to explore the woods.")
                            anim_print("Press 'G' to give up.")
                            walking_in_woods = True
                            count = 0
                            while walking_in_woods:
                                move_forward = anim_input("Explore the woods (M)? Give up (G)? ").upper()
                                while count < 5:
                                    chance = random.randint(1, 100)
                                    if move_forward == 'M':
                                        if chance <= 25 or chance >= 85:
                                            anim_print("You hear something come up from behind!")
                                            time.sleep(1)
                                            random_fight.random_enemy()
                                            anim_print("You were safely able to fend off your attacker!")
                                            anim_print("Maybe exploring back here wasn't the best idea.")
                                            time.sleep(1)
                                            move_forward = False
                                            break
                                        else:
                                            anim_print("You continue forward.")
                                            time.sleep(1)
                                            count += 1
                                            if count == 5:
                                                anim_print("You made it to the end of the visible, beaten path.")
                                                anim_print("You look around but see nothing of interest.")
                                                anim_print("You're about to turn around when you hear something up ahead.")
                                                anim_print("Instinctively, you pick up a rock and throw it.")
                                                anim_print("You hear it hit something, and you can hear a loud, metallic CLASH!")
                                                anim_print("You go over to where you heard the rock hit metal...")
                                                anim_print("And you are surprised at what you find.")
                                                time.sleep(2)
                                                anim_print("A bear trap was added to your inventory.")
                                                with open(filename, 'a', newline='') as file:
                                                    new_item = "bear trap"
                                                    attack = 60
                                                    csv_writer = csv.writer(file)
                                                    csv_writer.writerow([new_item, attack])
                                                time.sleep(1)
                                                anim_print("When you decide to use it, you'll automatically arm it.")
                                                time.sleep(1)
                                                anim_print("You decide that you're done exploring the back of the school and you head back to the main road.")
                                                time.sleep(1)
                                                anim_print("Where should you look next?")
                                                walking_in_woods = False
                                                break
                                            else:
                                                anim_print("The school gets further behind you...")
                                                time.sleep(1)
                                                move_forward = False
                                                break
                                    if move_forward == 'G':
                                        anim_print("You don't want to get hurt looking back here.")
                                        anim_print("So you just decide to go back to the main road.")
                                        time.sleep(1)
                                        anim_print("Where should you look next?")
                                        move_forward = False
                                        break
                                    else:
                                        anim_print("You stop to take in your surrounding instead of moving forward.")
                                        anim_print("But you hear something rush up from behind you!")
                                        anim_print("You have no time to react!")
                                        random_fight.random_enemy()
                                        time.sleep(1)
                                        anim_print("You were safely able to fend off your attacker!")
                                        anim_print("But in your despiration to get away...")
                                        time.sleep(1)
                                        anim_print("You ran a third of a mile in the wrong direction.")
                                        time.sleep(1)
                                        count -= 1
                                        move_forward = False
                                        break
                            deciding == False
                            break
                        else:
                            print("This is not what was asked of you.")
                            time.sleep(1)
                            deciding == True
                elif to_explore == "hospital":
                    city_rain.stop()
                    anim_print("You decide to go to the hospital.")
                    anim_print("If you're attacked, there's surely something there that can help you feel better.")
                    anim_print("As you walk towards the hosital, you see an enemy in the distance.")
                    anim_print("It looks like this route has a lot of enemies...")
                    anim_print("Be careful.")
                    time.sleep(1)
                    anim_print("Press 'M' to walk towards the hospital.")
                    walking_in_woods = True
                    count = 0
                    while walking_in_woods:
                        move_forward = anim_input("Walk towards the hospital (M)? ").upper()
                        while count < 6:
                            chance = random.randint(1, 100)
                            if move_forward == 'M':
                                if chance <= 40 or count == 3:
                                    anim_print("Despite seeing enemies up ahead, you hear something come up from behind you!")
                                    time.sleep(1)
                                    random_fight.random_enemy()
                                    anim_print("You were safely able to get away with your life!")
                                    anim_print("Whatever is in the hospital better be worth it.")
                                    time.sleep(1)
                                    move_forward = False
                                    break
                                else:
                                    anim_print("You carefully sneak past another enemy.")
                                    anim_print("That could have been a close call.")
                                    time.sleep(1)
                                    count += 1
                                    if count == 6:
                                        anim_print("You finally make it to the hospital and quickly go inside before something attacks you.")
                                        walking_in_woods = False
                                        break
                                    else:
                                        move_forward = False
                                        break
                            else:
                                anim_print("You weren't paying close enough attention to where you were going and you're attacked!")
                                random_fight.random_enemy()
                                time.sleep(1)
                                anim_print("You were safely able to fend off your attacker!")
                                anim_print("But you ended up going the wrong way.")
                                time.sleep(1)
                                count -= 1
                                move_forward = False
                                break
                    anim_print("You quickly pry open the sliding doors.")
                    anim_print("You have to fight off some monsters to get inside, but you're able to get in.")
                    anim_print("You hold the doors closed as you drag a nearby chair over to block the monsters from getting inside the main lobby.")
                    anim_print("You should be safe for now.")
                    anim_print("But you don't want to stay too long.")
                    anim_print("There were a whole bunch of floors to the hospial, but now most of the higher ones are decaying and weathered.")
                    anim_print("You look around the bottom floor and find some places to go.")
                    seen_hospital = set()
                    all_choices = {"gift shop", "restrooms", "stairway"}
                    explore = True
                    while explore:
                        if seen_hospital == all_choices:
                            explore = False
                            break
                        to_explore = anim_input("You decide to go to the gift shop, restrooms, or stairway: ").lower()
                        if to_explore in seen_hospital:
                            explore = True
                            anim_print("You already looked there. Look somewhere else.")
                        else:
                            seen_hospital.add(to_explore)
                            if to_explore == "gift shop":
                                anim_print("A gift shop is bound to have something useful.")
                                anim_print("You follow the signs until you get to the gift shop.")
                                anim_print("The door to the gift shop is still locked and you couldn't kick it down when you tried.")
                                anim_print("Luckily, you see a display window, and decide to break it and climb in through there.")
                                time.sleep(1)
                                anim_print("Once inside the gift shop, you can get a good look around.")
                                anim_print("The gift shop seems untouched by the elements outside, and everything looks rather new.")
                                anim_print("With the exception of the layers of dust over everything.")
                                anim_print("You grab what you can and you leave.")
                                time.sleep(1)
                                anim_print("A med kit was added to your inventory.")
                                with open('health_inventory.csv', 'a', newline='') as file:
                                    new_item = "med kit"
                                    attack = 15
                                    csv_writer = csv.writer(file)
                                    csv_writer.writerow([new_item, attack])
                                time.sleep(1)
                                anim_print("A bottle of rubbing alcohol was added to your inventory.")
                                with open('health_inventory.csv', 'a', newline='') as file:
                                    new_item = "rubbing alcohol"
                                    attack = 10
                                    csv_writer = csv.writer(file)
                                    csv_writer.writerow([new_item, attack])
                                time.sleep(1)
                                anim_print("Clean bandages were added to your inventory.")
                                with open('health_inventory.csv', 'a', newline='') as file:
                                    new_item = "clean bandages"
                                    attack = 5
                                    csv_writer = csv.writer(file)
                                    csv_writer.writerow([new_item, attack])
                                time.sleep(1)
                                anim_print("You think you've gotten enough from the gift shop and you leave through the display window.")
                                anim_print("Where should you go next?")
                            elif to_explore == "restrooms":
                                anim_print("You go to the restrooms.")
                                anim_print("You're not exactly sure what you might find in there.")
                                anim_print("But maybe you'll find something useful.")
                                anim_print("You go into the restroom and find that it's really dark.")
                                # Secret 2 will be in this restroom.
                                # If you get a flashlight and shine it in the restroom, you can find the secret item.
                                anim_print("Just enough light from the open door shines into the room to where you can see your reflection.")
                                anim_print(f"You look {adjective_01} and kinda {adjective_02} as usual.")
                                time.sleep(1)
                                anim_print("While you're in here, you decide to take a short break.")
                                time.sleep(1)
                                inventory = True
                                while inventory:
                                    print()
                                    view_inventory = anim_input("View your inventory (E)? ").capitalize()
                                    print()
                                    if view_inventory == "E":
                                        with open(statistics, 'r') as file:
                                            anim_print("YOUR STATISTICS")
                                            time.sleep(1)
                                            choice = csv.reader(file)
                                            stats = {}
                                            for row in choice:
                                                new_stat, kill_power = row
                                                stats[new_stat] = kill_power
                                            for key in ["your name", "your description", "your ability", "your weakness"]:
                                                if key in stats:
                                                    if key == "your description":
                                                        words = stats[key].strip("()").replace("'", "").split(", ")
                                                        print(f"{key.title()}: You are {words[0]} and kinda {words[1]}. There is not much else to say.")
                                                    else:
                                                        print(f"{key.title()}: {stats[key].capitalize()}")
                                                    time.sleep(1)
                                            if "your health" in stats:
                                                print(f"Your Health: {stats['your health'].capitalize()}")
                                                time.sleep(1)
                                            if "your attack" in stats:
                                                print(f"Your Attack: {stats['your attack'].capitalize()}")
                                                time.sleep(1)
                                        with open(filename, 'r') as collected_items:
                                            print()
                                            anim_print("YOUR INVENTORY")
                                            choice = csv.reader(collected_items)
                                            for row in choice:
                                                new_item, attack = row
                                            for key in new_item:
                                                if key == "public service announcement":
                                                    new_item, attack = row
                                                    print(f"{new_item.title()}: The PSA reads...\nResidents of Seona City - This is a public service announcement.\nPlease evacuate the city immediately due to an unknown [illegible].\nThis notice is put into effect as of August [illegible].\n{attack} damage.")
                                                else:
                                                    print(f"{new_item.title()}: {attack} damage")
                                            time.sleep(1)
                                        with open('health_inventory.csv') as collected_health:
                                            print()
                                            anim_print("YOUR HEALTH ITEMS")
                                            choice = csv.reader(collected_health)
                                            for row in choice:
                                                new_item, healing = row
                                                print(f"{new_item.title()}: {healing} healing")
                                        print()
                                    else:
                                        inventory = False
                                        anim_print("Verywell then...")
                                        time.sleep(1)
                                anim_print("After self reflecting, you decide to leave the bathroom.")
                                anim_print("Where should you go next?")
                                time.sleep(1)
                            elif to_explore == "stairway":
                                anim_print("You follow the signs posted in the hallway until you reach the stairwell.")
                                anim_print("You shove open the door with great force.")
                                anim_print("It was hard to open due to the weeds and tree roots blocking the way.")
                                anim_print("Once you're inside of the stairwell, you look up.")
                                anim_print("There are at least 20 flights of stairs until you reach the top floor of the hospital.")
                                anim_print("Luckily you aren't going that far.")
                                time.sleep(1)
                                anim_print("You go up the stairs until you find yourself on floor two.")
                                anim_print("Once you leave the stairs and step foot on to the second floor, you hear a thud from down the hallway.")
                                anim_print("You prepare for a fight.")
                                time.sleep(1)
                                anim_print("But nothing happens.")
                                time.sleep(1)
                                anim_print("Do you investigate the sound, or do you leave?")
                                leave_or_stay = anim_input("You decide to... ").lower()
                                if leave_or_stay == "leave":
                                    anim_print("You don't want to risk your life to see what could be down the hallway.")
                                    anim_print("So, you decide to go back to the stairwell and up to floor three.")
                                if leave_or_stay == "investigate":
                                    anim_print("You decide to go down the hallway and find out where the source of the sound came from.")
                                    anim_print("Suddenly you are attacked!")
                                    anim_print("There are three enemies waiting for you in the hallway!")
                                    random_fight.random_enemy()
                                    anim_print("You're still alive!")
                                    anim_print("But there are two enemies left!")
                                    random_fight.random_enemy()
                                    anim_print("You're still alive!")
                                    anim_print("But there is one enemy left!")
                                    anim_print("You can do it!")
                                    random_fight.random_enemy()
                                    anim_print("You were able to stay alive!")
                                    anim_print("Right after your fight, you hear something fall in the other room.")
                                    anim_print("After surviving three attacks, you feel that you can do anything.")
                                    anim_print("You go into the other room, and to your surprise...")
                                    time.sleep(1)
                                    anim_print("You see another person!")
                                    anim_print("She is sitting on the dirty patient bed, holding her arm.")
                                    anim_print("Blood from her arm trickles down and stains her clothing.")
                                    anim_print("She must have been attacked!")
                                    time.sleep(1)
                                    anim_print("You quickly go over to her and try to talk to her.")
                                    anim_print("You ask her what happened to everyone.")
                                    anim_print("You ask her why everything looks like its falling apart.")
                                    anim_print("You ask her where she came from.")
                                    anim_print("You ask her why she's still here.")
                                    anim_print("But you stop your line of questioning, because she just stares at you puzzled.")
                                    anim_print("The woman pauses before she speaks with a hoarse voice.")
                                    anim_print("The woman says 'Kokodei hai kot'e zso'.")
                                    anim_print("But you don't know what she tells you.")
                                    anim_print("You don't recognize the language either.")
                                    anim_print("You look around the room for something to tie around the woman's arm.")
                                    anim_print("Maybe if you can help her out, she'll help you in return.")
                                    anim_print("You eventually find some bandages and tie them around her arm.")
                                    anim_print("The woman says 'Neuhaussomo fhtu'ho zso'.")
                                    anim_print("You don't know what she means.")
                                    anim_print("Everytime the woman speaks, she coughs a lot.")
                                    anim_print("You expect that she won't be saying much.")
                                    anim_print("You try your best to ask the woman for help, and you motion her to follow you.")
                                    anim_print("You hope that she understands.")
                                    time.sleep(1)
                                    anim_print("The young woman has joined your team!")
                                    anim_print("In fights, she can now help you!")
                                    with open(filename, 'a', newline='') as file:
                                        new_item = "unknown woman"
                                        attack = 40
                                        csv_writer = csv.writer(file)
                                        csv_writer.writerow([new_item, attack])
                                        inventory = []
                                    with open('achievements.csv', 'r') as file:
                                        reader = csv.reader(file)
                                        for row in reader:
                                            inventory.append(row[0])
                                    items_to_add = [("find another survivor")]
                                    for item in items_to_add:
                                        if item not in inventory:
                                            inventory.append(item)
                                            with open('achievements.csv', 'a', newline='') as file1:
                                                writer1 = csv.writer(file1)
                                                writer1.writerow([item])
                                        else:
                                            time.sleep(1)
                                    anim_print("After finding the woman, you are excited to have someone else with you.")
                                    anim_print("Even if she couldn't understand you.")
                                    anim_print("After finding your new friend, you decide to continue on your journey.")
                                    anim_print("And you make your way to floor three.")
                                    anim_print("The woman follows behind you.")
                                break
                            else:
                                anim_print(f"You don't remember seeing {to_explore} on the bottom floor.")
                                time.sleep(1)
                    anim_print("As you make your way up to floor three, you think to yourself that this is the last floor that you'll visit.")
                    anim_print("You don't feel comfortable staying in one place for too long.")
                    anim_print("As you make it to the third floor, you see that the nature had already started reclaiming the floor.")
                    anim_print("Light pours into the room from the huge holes in the wall, and the wind blows leaves from trees onto the dirty, cracked tile floors.")
                    anim_print("At least the rain has all but calmed down outside.")
                    anim_print("This floor mainly has hospital rooms for patients.")
                    anim_print("You don't know what you'll find.")
                    anim_print("You go to the front desk and you look through the papers, hoping to find a layout of the floor.")
                    anim_print("And you see a paper map of the floor.")
                    anim_print("You were honestly surprised to find this.")
                    anim_print("These places look like some places you could visit.")
                    anim_print("Where should you go?")
                    anim_print("You're only going to visit three places.")
                    seen_three = set()
                    all_choices = {"301", "302", "303", "304", "storage"}
                    exploring_floor_three = True
                    count = 0
                    while exploring_floor_three:
                        enter_area = anim_input("You decide to visit '301', '302', '303', '304', or the 'storage': ").lower().strip()
                        while count < 3:
                            if enter_area in seen_three:
                                exploring_floor_three = True
                                anim_print("You already looked there. Look somewhere else.")
                            else:
                                seen_three.add(enter_area)
                                if enter_area == "301":
                                    anim_print("You walk into room 301 not knowing what to expect.")
                                    anim_print("And you find a normal room.")
                                    time.sleep(1)
                                    anim_print("Unfortunately, there's nothing of interest in this room.")
                                    anim_print("Maybe a different room had something of use.")
                                    time.sleep(1)
                                    count += 1
                                    enter_area = False
                                    break
                                elif enter_area == "302":
                                    anim_print("You walk into room 302 not knowing what to expect.")
                                    anim_print("And you find a normal room.")
                                    time.sleep(1)
                                    random_fight.random_enemy()
                                    anim_print("You must have missed that enemy being in the room!")
                                    anim_print("You missed it hiding behind the bed!")
                                    time.sleep(1)
                                    anim_print("At least your fight wasn't in vain and you find something of use in the room.")
                                    time.sleep(1)
                                    with open('health_inventory.csv', 'a', newline='') as file:
                                        new_item = "strong medicine"
                                        attack = 20
                                        csv_writer = csv.writer(file)
                                        csv_writer.writerow([new_item, attack])
                                    anim_print("Strong medicine was added to your inventory.")
                                    time.sleep(1)
                                    count += 1
                                    enter_area = False
                                    break
                                elif enter_area == "303":
                                    anim_print("You walk into room 303 not knowing what to expect.")
                                    anim_print("And the room is a mess.")
                                    anim_print("The walls are scratched up and the carpets are in ruin.")
                                    anim_print("Something's in here.")
                                    random_fight.random_enemy()
                                    anim_print("There's a second one!")
                                    random_fight.random_enemy()
                                    time.sleep(1)
                                    anim_print("At least your fight wasn't in vain and you find something of use in the room.")
                                    time.sleep(1)
                                    with open('project_inventory.csv', 'a', newline='') as file1, open('health_inventory.csv', 'a', newline='') as file2:
                                        health_item = "mysterious pills"
                                        health_attack = 25
                                        attack_item = "mysterious pills"
                                        attack_attack = 100
                                        writer1 = csv.writer(file1)
                                        writer2 = csv.writer(file2)
                                        writer1.writerow([attack_item, attack_attack])
                                        writer2.writerow([health_item, health_attack])
                                    anim_print("Two bottles of mysterious pills were added to your inventory.")
                                    time.sleep(1)
                                    anim_print("You're... worried to use these on yourself...")
                                    time.sleep(1)
                                    anim_print("Maybe you'll test them on your enemy first...")
                                    count += 1
                                    enter_area = False
                                    break
                                elif enter_area == "304":
                                    anim_print("You walk into room 304 not knowing what to expect.")
                                    anim_print("And you find a normal room.")
                                    time.sleep(1)
                                    anim_print("Unfortunately, there's nothing of interest in this room.")
                                    anim_print("Maybe a different room had something of use.")
                                    time.sleep(1)
                                    count += 1
                                    enter_area = False
                                    break
                                elif enter_area == "storage":
                                    anim_print("You walk into the storage room, not knowing what to expect.")
                                    anim_print("And you find a whole bunch of stuff thrown in the room.")
                                    anim_print("Among cleaning supplies, you find spare medical supplies sloppily placed in the closet.")
                                    anim_print("Even with the building itself being in decay, you don't understand why the storage room is such a mess.")
                                    anim_print("Someone must have thrown these things in here in a rush.")
                                    time.sleep(1)
                                    anim_print("You dig through the storage room and the items thrown about...")
                                    anim_print("...and you find a duffle bag.")
                                    anim_print("It's filled with empty boxes.")
                                    anim_print("Wait. One of these boxes has something in it.")
                                    time.sleep(1)
                                    with open(filename, 'a', newline='') as file:
                                        new_item = "box of unused syringes"
                                        attack = 22
                                        csv_writer = csv.writer(file)
                                        csv_writer.writerow([new_item, attack])
                                    anim_print("A box of unused syringes was added to your inventory.")
                                    time.sleep(1)
                                    count += 1
                                    enter_area = False
                                    break
                                else:
                                    anim_print("That isn't on the map.")
                                    move_forward = False
                                    break
                        if count == 3:
                            anim_print("You've in three different places on this floor, but you think that it's about time to leave.")
                            anim_print("The sun is starting to set.")
                            anim_print("You walk back down to the bottom floor of the hospital and you're happy that the monsters that were outside are gone now.")
                            anim_print("You leave out of the front door of the hospital.")
                            time.sleep(1)
                            anim_print("And you aren't ambushed.")
                            time.sleep(1)
                            exploring_floor_three = False
                            break
                        elif count < 3:
                            anim_print("Where should I go next?")
                            enter_area = False
                            break
                elif to_explore == "playground":
                    anim_print("You decide to go to the playground.")
                    anim_print("As you walk to the playground, you don't expect to find much.")
                    anim_print("On the way to the playground, you are surprised that there was nothing there to attack you.")
                    anim_print("When you reach the playground, you even more surprised that it's completely empty.")
                    anim_print("It's entirely quiet.")
                    anim_print("Too quiet...")
                    time.sleep(1)
                    anim_print("Be careful.")
                    time.sleep(1)
                    anim_print("You go over to the overgrown, grassy field connected to the playground.")
                    anim_print("Little gnats start to swarm around you the closer you get.")
                    anim_print("You swat at them to try and keep them away from your eyes.")
                    anim_print("Something bad is here.")
                    anim_print("You just have a feeling.")
                    time.sleep(1)
                    anim_print("You see two different places to go.")
                    anim_print("The swings.")
                    anim_print("Or the playset.")
                    swing_playset = anim_input("You go to the 'swings' or the 'playset': ").lower().strip()
                    if swing_playset == "swings":
                        anim_print("You walk over to the creaking swingset.")
                        anim_print("The swings are slowly swaying back and forth as if someone just got off of them moments before.")
                        anim_print("Just being in the area makes you feel a little sick.")
                        time.sleep(1)
                        anim_print("Upon closer inspection of the swings.")
                        anim_print("You notice thick, oily hair stuck to it.")
                        anim_print("That hair is surely not human.")
                        anim_print("Despite your instincts telling you to leave, you continue to look around the area.")
                        anim_print("Decay eats away and the plants in the area.")
                        anim_print("This place is unusually eerie.")
                        time.sleep(1)
                        anim_print("Suddenly...")
                        hard_random_enemy.hard_random_enemy()
                        anim_print("You're still alive and you try to run.")
                        time.sleep(1)
                        anim_print("But...")
                        hard_random_enemy.hard_random_enemy()
                        anim_print("You're still alive and you run away as fast as you can from the area.")
                        anim_print("You don't look behind you.")
                        anim_print("Maybe next time you'll listen to your instincts.")
                        time.sleep(1)
                    if swing_playset == "playset":
                        anim_print("You decide to go over to the playset.")
                        anim_print("The metal is slick with water from the rain.")
                        anim_print("And you almost fall as you're walking over the rubber foundation that the playset is built on.")
                        anim_print("You're not sure of what kid would want to be here.")
                        anim_print("This place is creepy.")
                        anim_print("But at least visiting here wasn't in vain.")
                        anim_print("You found... something...")
                        time.sleep(1)
                        with open(filename, 'a', newline='') as file:
                            new_item = "stuffed animal"
                            attack = 8
                            csv_writer = csv.writer(file)
                            csv_writer.writerow([new_item, attack])
                        anim_print("A stained stuffed animal was added to your inventory.")
                        anim_print("You think it was a bear.")
                        time.sleep(1)
                    else:
                        anim_print("You decide to just leave. You don't want to risk getting hurt.")
                        time.sleep(1)
                elif to_explore == "pond":
                    anim_print("You figure that you'll investigate the pond first.")
                    anim_print("The map says that it's one of furthest places to travel to...")
                    anim_print("But you have nothing to lose.")
                    anim_print("Once you finally reach the pond, you find that its filthy.")
                    anim_print("Not only is the pond overgrown with moss and mold...")
                    anim_print("But there is a surprising amound of trash around too.")
                    anim_print("The people that used to live here must have thought that this was some kind of landfill.")
                    anim_print("You go towards the murky pond, and as you stand over it, you find that you can't even see your reflection in the water.")
                    anim_print("You regret coming here.")
                    anim_print("There's nothing of interest...")
                    time.sleep(1)
                else:
                    anim_print(f"You don't remember seeing {to_explore} on the map.")
                    time.sleep(1)

        anim_print("You finish exploring everywhere that you saw on the map.")
        anim_print("You think about what your next move should be when you hear a human scream from down the street.")
        anim_print("You run towards the scream to see if you can help, when you see it!")
        anim_print("You don't know what to think of it!")
        time.sleep(2)
        anim_print("Thank you for playing the demo of 'Mystery of Seona!")
        anim_print("Come back in the future for the completed game!")
        anim_print("There will probably be an update in the future!")
        time.sleep(1)
        anim_print("These are your achievements!")
        time.sleep(1)
        with open(filename, 'r') as collected_items:
            print()
            anim_print("YOUR ACHIEVEMENTS!")
            time.sleep(1)
            choice = csv.reader(collected_items)
            for row in choice:
                new_item, attack = row
                print(f"{new_item.title()}: {attack} damage")
                time.sleep(1)
        response = anim_input("Type something to quit: ")
        if response == response:
            anim_print("Deleting files...",delay=0.135)
            time.sleep(1)
            anim_print("Loading...",delay=0.135)
            with open('achievements.csv', 'w', newline='') as file:
                pass
            with open('health_inventory.csv', 'w', newline='') as file:
                pass
            with open('project_inventory.csv', 'w', newline='') as file:
                pass
            with open('secret_items.csv', 'w', newline='') as file:
                pass
            with open('stats.csv', 'w', newline='') as file:
                pass


        # after exploring everywhere, you are ambushed by a miniboss, the user's weakness, who has a human hostage; the mega mutation.
        # there are two endings for the miniboss fight. if miniboss kills hostage, hostage can't tell you important info.
            # if you kill miniboss before hostage dies, you get important info.
            # important info is a keycard to unlock a secret base in the woods. that is where secret is revealed and you fight the final boss.
            # you can use your special skill as a weapon. attack power is *10 of your attack. you can only use it once per round.
            # when boss dies once, boss has a phase two.
            # you get a lot of items to use against the boss, AND healing items too.
            # phase 1: Boss health is 400, attack 25.
            # phase 2: Boss health is 600, attack 40.


        # To clear ALL of the contents of a CSV file at once, type the following...
        # "with open('FILENAME.csv', 'w', newline='') as file:
        # pass"
        # inventory clears and stats clear when you finish the game so you can play again without having to clear your inventory manually.

    if character_choice == "Syuuran":
        health = 100
        attack = 4
        syuuran_special_ability = "persuasion"
        syuuran_weakness = "mice"
        anim_print("Interesting...")
        time.sleep(1)
        anim_print("Creating scenario...", delay=0.135)
        time.sleep(2)
        anim_print("Loading...", delay=0.135)
        print()
        # Syuuran finds himself in the middle of the woods at night.

    if character_choice == "Ana":
        health = 100
        player_attack = attack
        ana_special_ability = "observation"
        ana_weakness = "mice"
        anim_print("I see...")
        time.sleep(1)
        anim_print("Creating scenario...", delay=0.135)
        time.sleep(2)
        anim_print("Loading...", delay=0.135)
        print()
        # ana finds a knife as her weapon in the story.

if __name__ == "__main__":
    opening_scene()
