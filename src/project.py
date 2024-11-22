import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time, csv, pygame
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
        else:
            wrong_username = False
    adjective_01 = anim_input("Adjective 01: ")
    adjective_02 = anim_input("Adjective 02: ")
    ability = anim_input("What is a good skill to have? ")
    weakness = anim_input("In one word, what scares you? ")
    strength = True
    while strength:
        try:
            anim_print(f"Pick a number between 1 and 10.")
            attack = float(anim_input("Choose wisely: "))
            if 1 <= attack <= 10:
                strength = False
            else:
                anim_print("This is not what I asked for.")
                time.sleep(0.75)
        except ValueError:
            anim_print("Do you call that a number...?")
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

    anim_print(f"Character: {username.upper()}")
    time.sleep(1)
    anim_print(f"Description: {username.title()} is {adjective_01} and kinda {adjective_02}. There's not much else to say.")
    time.sleep(1)
    anim_print("Health: 100")
    anim_print(f"Attack: {attack:.0f}")
    anim_print(f"Special Ability: {ability.capitalize()}")
    anim_print(f"Weakness: {weakness.capitalize()}")
    time.sleep(2)
    print()
    correct_choice = False
    while not correct_choice:
            anim_print("Who are you?")
            character_choice = anim_input("Choose wisely: ").capitalize()
            if character_choice == username.capitalize():
                correct_choice = True
            elif character_choice == "Syuuran" or "Ana":
                correct_choice = False
                anim_print("Sorry! This choice is not available for the demo! Look for updates in the future!")
            else:
                correct_choice = False
                anim_print("This is not what I asked for.")

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
                anim_print("You see that leaves adorn the floor of the metal room closest to the broken wall.")
                anim_print("Leaves must have fallen into the room from outside.")
                time.sleep(.75)
                anim_print("You look across the room.")
                time.sleep(.10)
                anim_print("There is a door...")
                anim_print("Maybe you'll be able to leave. And hopefully find a way home.")
                anim_print("Maybe by time you leave, you'll remember where home is.")
                time.sleep(1)
                anim_print("Your legs feel numb as you stand, and you stumble your way towards the door.")
                anim_print("Once closer, you find that the door is cracked open slightly.")
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
            to_look = anim_input("You look at the leaves, table, or wall: ").lower()
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
                    if seen_inputs == all_choices:
                        anim_print("Maybe there's something else here.")
                elif to_look == "table":
                    looking = True
                    anim_print("You walk back over to the table you woke up next to.")
                    anim_print("When you crouch down, to look under the table.")
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
                    if seen_inputs == all_choices:
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
                        grab_item = anim_input("You have an idea to grab something to stand on, and you grab the... ").lower()
                        if grab_item == "chair":
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
                            if seen_inputs == all_choices:
                                anim_print("Maybe there's something else here.")
                        else:
                            elevated_surface = True
                            anim_print("You don't know if that will work.")
            if seen_inputs == all_choices:
                looking = False
                break
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
        anim_print("What can help you open the door?")
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
                    print("It does not work.")
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
        city_rain.play(loops=-1)
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
        import first_fight
        first_fight
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
                inventory = True
                with open(statistics, 'r') as file:
                    anim_print("YOUR STATISTICS")
                    time.sleep(1)
                    choice = csv.reader(file)
                    for row in choice:
                        new_stat, kill_power = row
                        print(f"{new_stat.title()}: {kill_power}")
                        time.sleep(2)
                with open(filename, 'r') as collected_items:
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
        anim_print("The bandage was removed from your inventory.")
        time.sleep(1)
        anim_print("It's best if you get out of this area.")
        anim_print("You make your way down the hallway of the building you just came from.")
        anim_print("The smell of rain overwhelms your senses.")
        anim_print("You hope that you'll get used to it soon.")
        anim_print("As you reach the end of the hallway, you see two sepparate metal doors.")
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
                time.sleep(1)
            elif door == "right":
                choose_door = False
                anim_print("")
            else:
                choose_door = True
                anim_print("What?", delay=0.1)
                time.sleep(.5)

        # go to abandoned towns.
        # you find a map of the whole area.
        seen_towns = set()
        all_choices = {"market", "school", "hospital", "playground", "pond"}
        explore = True
        while explore:
            to_explore = anim_input("You decide to explore the market, school, hospital, playground, or pond: ").lower()
            if to_explore in seen_towns:
                looking = True
                anim_print("You already looked there. Look somewhere else.")
            else:
                seen_towns.add(to_explore)
                if to_explore == "market":
                    explore = True
                    city_rain.stop()
                    anim_print("")
                elif to_explore == "school":
                    explore = True
                    city_rain.stop()
                    anim_print("")
                elif to_explore == "hospital":
                    explore = True
                    city_rain.stop()
                    anim_print("")
                elif to_explore == "playground":
                    explore = True
                    anim_print("")
                elif to_explore == "pond":
                    explore = True
                    anim_print("")
                elif seen_towns == all_choices:
                    break
        anim_print("")


        anim_print("")
        # Explore the nearby town and its abandoned buildings.
        # Town name: Seona
            # produce market
            # school + woods behind the school
            # hospital
            # playground
            # murky pond
        # Final fight is spider queen.
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
