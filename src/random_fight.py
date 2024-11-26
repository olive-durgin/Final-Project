import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, time, random, csv, project
pygame.init()
sound = pygame.mixer.Sound(r'sounds\medium_fight.mp3')
win_sound = pygame.mixer.Sound(r'sounds\winner.mp3')
lose_sound = pygame.mixer.Sound(r'sounds\death.mp3')
hero_attack = pygame.mixer.Sound(r'sounds\hero_attack.mp3')
monster_attack = pygame.mixer.Sound(r'sounds\monster_bite.mp3')
filename = "project_inventory.csv"
statistics = "stats.csv"

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

def random_enemy():

    enemies = ["Ana"] * 1 + ["Syuuran"] * 1 + ["screaming, little freak"] * 5 + ["wild, flesh-eating monster"] * 5 +["long cat", "mutated rat", "mutated dog", "odd badger", "odd elk", "long stoat"] * 88
    selected_enemy = random.choice(enemies)
    idx = enemies.index(selected_enemy)

    if enemies[idx] != "Ana" and enemies[idx] != "Syuuran":
        the_or_no = "the "
        her_him_it = "it"
        she_he_it = "it"
        herself_himself_itself = "itself"
    else:
        the_or_no = ""
    if enemies[idx] == "long cat":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "At first, you couldn't tell what was off about it, but then you realized..."\
        "\nIt is unusually long!\nAs it moves, its spine bends awkwardly, and it looks as if its in pain!"
        attack_type = "\nThe long cat's crooked teeth sinks into your skin and you scream."
        initial_enemy_health = float(18)
        enemy_health = initial_enemy_health
        enemy_attack = float(6)
        enemy_desc = "pounces"
        a_or_an = " a"
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("meet long cat")]
        for item in items_to_add:
            if item not in inventory:
                see_or_not = "This is something you've never seen before!"
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
                time.sleep(2)
            else:
                see_or_not = f"{the_or_no.capitalize()}{enemies[idx]} looks familiar! You've seen {her_him_it} before!"
    if enemies[idx] == "mutated rat":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "Like the first rat that ambushed you when you left that metal room, this one looks no different."\
        "\nBoth were rather disfigured.\nBoth were nearly as big as you were!"
        attack_type = "\nAs the rat bites into the part of you that's closest to its mouth, you try to kick it off, but it won't let go!\nWhen it finally gets off of you, a chunk of your arm goes with it!"
        initial_enemy_health = float(15)
        enemy_health = initial_enemy_health
        enemy_attack = float(10)
        enemy_desc = "snaps"
        a_or_an = " a"
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("meet mutated rat")]
        for item in items_to_add:
            if item not in inventory:
                see_or_not = "This is something you've never seen before!"
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
                time.sleep(2)
            else:
                see_or_not = f"{the_or_no.capitalize()}{enemies[idx]} looks familiar! You've seen {her_him_it} before!"
    if enemies[idx] == "mutated dog":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "As it runs towards you at full speed, you feel fear rush over you like a wave!"\
        "\nIt's awkward, broken run is accompanied by it's wheezing bark.\nYou have no time to react!"
        attack_type = "\nThe mutated dog's bite was much stronger than its bark, \nand its teeth and long, uncut claws digs into your skin!"
        initial_enemy_health = float(20)
        enemy_health = initial_enemy_health
        enemy_attack = float(15)
        enemy_desc = "lunges"
        a_or_an = " a"
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("meet mutated dog")]
        for item in items_to_add:
            if item not in inventory:
                see_or_not = "This is something you've never seen before!"
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
                time.sleep(2)
            else:
                see_or_not = f"{the_or_no.capitalize()}{enemies[idx]} looks familiar! You've seen {her_him_it} before!"
    if enemies[idx] == "wild, flesh-eating monster":
        if "wild, flesh-eating monster" == "wild, flesh-eating monster":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "It was hard to comprehend what was coming towards you at first, but as it got closer, you wish it didn't."\
        "\nIts twelve pair of backwards, twisted limbs thrusted the thing closer and closer to you."\
        "\nIf you weren't mistaken, it smiled at you.\nOr maybe that's just how its decaying face looks.\n"\
        "You have no idea what it is.\nOr what it was...\nYou don't want to know...\nSomething about it is terribly wrong..."
        attack_type = "\nIt grabs you using its many hands, and it attempts to bite off your face."\
        "Luckily for you, it missed.\nBut it still managed to hurt you when it grabbed you roughly."
        initial_enemy_health = float(50)
        enemy_health = initial_enemy_health
        enemy_attack = float(12)
        enemy_desc = "thrusts"
        a_or_an = " a"
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("meet wild, flesh-eating monster")]
        for item in items_to_add:
            if item not in inventory:
                see_or_not = "This is something you've never seen before!"
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
                time.sleep(2)
            else:
                see_or_not = f"{the_or_no.capitalize()}{enemies[idx]} looks familiar! You've seen {her_him_it} before!"
    if enemies[idx] == "screaming, little freak":
        if "wild, flesh-eating monster" == "wild, flesh-eating monster":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "You suddenly feel a chill as you see it...\nYou want to look away but you can't take your eyes off of it..."\
        "It's shrill scream hurts your ears...\nIt's uncanny, yellow-toothed smile unsettles you..."\
        "It moves like it doesn't belong here.\nIt's gross, oily, black hair sticks to its face and gets stuck between its teeth."\
        "Does it resemble a horse?\nA donkey?\nIt's something very wrong...\nIt terrifies you...\nYour health is set to half."\
        "\nYour attack is a quarter of what it should be..."
        strength = strength/4
        new_health = new_health/2        
        attack_type = "\nYou wish it didn't touch you but it did.\nIt's hot breath felt uncomfortable on your skin."\
        "\nIt overstayed its welcome when it bit you with its square, blunt teeth.\nIt screams when you kick it off of you."
        initial_enemy_health = float(45)
        enemy_health = initial_enemy_health
        enemy_attack = float(20)
        enemy_desc = "runs"
        a_or_an = " a"
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("meet screaming, little freak")]
        for item in items_to_add:
            if item not in inventory:
                see_or_not = "This is something you've never seen before!"
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
                time.sleep(2)
            else:
                see_or_not = f"{the_or_no.capitalize()}{enemies[idx]} looks familiar! You've seen {her_him_it} before!"
    if enemies[idx] == "odd badger":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "It would almost be a normal badger if somethng wasn't off about it.\nYou can't tell what it is."\
        "Maybe its the odd badger's extra head."
        attack_type = "\nWith it's long, dirty nails, it thrashes at you and breaks your skin!"
        initial_enemy_health = float(12)
        enemy_health = initial_enemy_health
        enemy_attack = float(6)
        enemy_desc = "thrashes"
        a_or_an = " an"
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("meet odd badger")]
        for item in items_to_add:
            if item not in inventory:
                see_or_not = "This is something you've never seen before!"
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
                time.sleep(2)
            else:
                see_or_not = f"{the_or_no.capitalize()}{enemies[idx]} looks familiar! You've seen {her_him_it} before!"
    if enemies[idx] == "odd elk":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "The thing approaching you is rather strange!\nWait a minute...\nIt's running at you a little too fast!"\
        "You only got a glimpse of it before it was right on top of you."\
        "It smells like mold and wet hair."
        attack_type = "\nThe odd elk throws its antlers around, hoping to hit you.\nUnfortunately it succeeds and the odd elk hurts you!"\
        "You're just happy that you didn't break a bone!"
        initial_enemy_health = float(50)
        enemy_health = initial_enemy_health
        enemy_attack = float(20)
        enemy_desc = "charges"
        a_or_an = " an"
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("meet odd elk")]
        for item in items_to_add:
            if item not in inventory:
                see_or_not = "This is something you've never seen before!"
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
                time.sleep(2)
            else:
                see_or_not = f"{the_or_no.capitalize()}{enemies[idx]} looks familiar! You've seen {her_him_it} before!"
    if enemies[idx] == "long stoat":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "Rather, you've been ambushed by an abnormally long stoat!\nIt would be a normal stoat if it weren't double the length!"
        attack_type = "\nIt's little blunt teeth nick at your skin!"
        initial_enemy_health = float(9)
        enemy_health = initial_enemy_health
        enemy_attack = float(3)
        enemy_desc = "rushes"
        a_or_an = " a"
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("meet long stoat")]
        for item in items_to_add:
            if item not in inventory:
                see_or_not = "This is something you've never seen before!"
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
                time.sleep(2)
            else:
                see_or_not = f"{the_or_no.capitalize()}{enemies[idx]} looks familiar! You've seen {her_him_it} before!"
    if enemies[idx] == "Ana":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        initial_enemy_health = float(100)
        enemy_health = initial_enemy_health
        enemy_attack = float(6)
        enemy_desc = "swings"
        a_or_an = ""
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("meet Ana")]
        for item in items_to_add:
            if item not in inventory:
                see_or_not = "This is something you've never seen before!"
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
                time.sleep(2)
            else:
                see_or_not = f"{she_he_it.capitalize()} looks familiar! Didn't you kill {her_him_it} before?"
    if enemies[idx] == "Syuuran":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        initial_enemy_health = float(100)
        enemy_health = initial_enemy_health
        enemy_attack = float(4)
        enemy_desc = "swings"
        a_or_an = ""
        inventory = []
        with open('achievements.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                inventory.append(row[0])
        items_to_add = [("meet Ana")]
        for item in items_to_add:
            if item not in inventory:
                see_or_not = "This is something you've never seen before!"
                inventory.append(item)
                with open('achievements.csv', 'a', newline='') as file1:
                    writer1 = csv.writer(file1)
                    writer1.writerow([item])
                time.sleep(2)
            else:
                see_or_not = f"{she_he_it.capitalize()} looks familiar! Didn't you kill {her_him_it} before?"
    with open('stats.csv', 'r') as file:
        choice = csv.reader(file)
        for row in choice:
            if row[0] == "your attack":
                new_stat, kill_power = row
                strength = float(kill_power)
            elif row[0] == "your health":
                new_stat, life = row
                new_health = float(life)
            elif row[0] == "initial health":
                new_stat, new_life = row
                initial_health = float(new_life)
    anim_print(f"You've been ambushed by{a_or_an} {enemies[idx]}!")
    if enemies[idx] == "Ana":
        anim_print("ERROR...")
        time.sleep(1)
        anim_print("Unknown files detected.")
        time.sleep(2)
        anim_print("Deleting unknown files...", delay=0.135)
        time.sleep(1)
        anim_print("Unable to fix error.")
        time.sleep(1)
        anim_print("Rebooting...", delay=0.135)
        time.sleep(1)
        anim_print("...", delay=0.135)
        time.sleep(2)
        anim_print("ERROR...")
        time.sleep(4)
        anim_print(f"You've been ambushed by{a_or_an} {enemies[idx]}!")
        time.sleep(1)
        anim_print("Some say she's happy and kinda brave.")
        time.sleep(1)
        anim_print("Who says this, exactly?")
        time.sleep(2)
        attack_type = "\nWith her knife loosely grasped in her shaking hands, Ana tries to stab you."\
        "\nThe knife cuts a deep gash in your skin.\nShe feels bad for hurting you."
        enemy_desc = "swings"
        a_or_an = ""
    if enemies[idx] == "Syuuran":
        anim_print("ERROR...")
        time.sleep(1)
        anim_print("Unknown files detected.")
        time.sleep(2)
        anim_print("Deleting unknown files...", delay=0.135)
        time.sleep(1)
        anim_print("Unable to fix error.")
        time.sleep(1)
        anim_print("Rebooting...", delay=0.135)
        time.sleep(1)
        anim_print("...", delay=0.135)
        time.sleep(2)
        anim_print("ERROR...")
        time.sleep(4)
        anim_print(f"You've been ambushed by{a_or_an} {enemies[idx]}!")
        time.sleep(1)
        anim_print("Some say he's scared and kinda alone.")
        time.sleep(1)
        anim_print("Who says this, exactly?")
        time.sleep(2)
        attack_type = "With an old frying pan in his hands, Syuuran takes a swing at you."\
        "You've never thought of a frying pan as being a weapon...\nIt still hurts..."
        enemy_desc = "swings"
        a_or_an = ""
    if enemies[idx] != "Ana" and enemies[idx] != "Syuuran":
        anim_print(description)
    if enemies[idx] == "Ana":
        she_he_it = "she"
        her_him_it = "her"
        herself_himself_itself = "herself"
    elif enemies[idx] == "Syuuran":
        she_he_it = "he"
        her_him_it = "him"
        herself_himself_itself = "himself"
    anim_print(see_or_not)

    inventory = []
    with open('stats.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            inventory.append(row[0])
    items_to_add = [("initial health", new_health)]
    for item, attack in items_to_add:
        if item not in inventory:
            time.sleep(2)
            anim_print(f"{the_or_no.capitalize()}{enemies[idx]} prepares to attack!")
            anim_print("Since you weren't expecting an ambush, you've been hit!")
            monster_attack.play()
            new_health -= enemy_attack
            anim_print(f"Your health decreases by {enemy_attack}!")
            anim_print(f"Your health dropped to {new_health}!")
            if new_health <= 0:
                if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                    sound.stop()
                    anim_print(f"{enemies[idx].capitalize()} feels bad for killing you so soon...")
                    sound.stop()
                    time.sleep(2)
                    anim_print("You died already...")
                    time.sleep(4)
                    anim_print("Overriding program...")
                    time.sleep(2)
                    anim_print("Resetting...")
                    time.sleep(2)
                    anim_print("Updating health to 100...")
                    time.sleep(1)
                    anim_print("Continuing code where it left off...")
                    time.sleep(1)
                    with open(statistics, 'r') as file:
                        reader = csv.reader(file)
                        items = list(reader)
                        item_to_remove = "your health".strip().capitalize()
                        items = [row for row in items if row[0].capitalize() != item_to_remove]
                    with open(statistics, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(items)
                    with open(statistics, 'a', newline='') as file:
                        new_item = "your health"
                        health = 100.0
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, health])
                        new_health = 100
                    with open(statistics, 'r') as file:
                        reader = csv.reader(file)
                        items = list(reader)
                        item_to_remove = "initial health".strip().capitalize()
                        items = [row for row in items if row[0].capitalize() != item_to_remove]
                    with open(statistics, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(items)
                    with open(statistics, 'a', newline='') as file:
                        new_item = "initial health"
                        health = 100.0
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, health])
                        new_health = 100
                else:
                    sound.stop()
                    time.sleep(2)
                    anim_print("You died already...")
                    time.sleep(4)
                    anim_print("Overriding program...")
                    time.sleep(2)
                    anim_print("Resetting...")
                    time.sleep(2)
                    anim_print("Updating health to 100...")
                    time.sleep(1)
                    anim_print("Continuing code where it left off...")
                    time.sleep(1)
                    with open(statistics, 'r') as file:
                        reader = csv.reader(file)
                        items = list(reader)
                        item_to_remove = "your health".strip().capitalize()
                        items = [row for row in items if row[0].capitalize() != item_to_remove]
                    with open(statistics, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(items)
                    with open(statistics, 'a', newline='') as file:
                        new_item = "your health"
                        health = 100.0
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, health])
                        new_health = 100
                    with open(statistics, 'r') as file:
                        reader = csv.reader(file)
                        items = list(reader)
                        item_to_remove = "initial health".strip().capitalize()
                        items = [row for row in items if row[0].capitalize() != item_to_remove]
                    with open(statistics, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(items)
                    with open(statistics, 'a', newline='') as file:
                        new_item = "initial health"
                        health = 100.0
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, health])
                        new_health = 100
            anim_print("Now is your chance!")
            anim_print("You remember what to do, right?")
            anim_print(f"Show that {enemies[idx]} what you got before {she_he_it} gets a chance to attack again!")
            anim_print("Be strategic about this, because sometimes, the enemy can be smarter than they look.")
            anim_print("Take your time and think about your next move though.")
            anim_print("Feel free to use your inventory.")
            anim_print("Just make sure your attacks and dodges don't miss.")
            time.sleep(1)
            anim_print("They might.")
            time.sleep(1)
            anim_print("Remember...")
            anim_print(f"Your attack is {strength:.0f}.")
            anim_print(f"Your health is {new_health:.0f}!")
            anim_print("If you die, these are the stats that will be used.")
            time.sleep(1)
            anim_print("Get ready!")
            time.sleep(1)
            inventory.append(item)
            with open('stats.csv', 'a', newline='') as file1:
                writer1 = csv.writer(file1)
                writer1.writerow([item, attack])
            anim_print("Something's changed...")
            time.sleep(2)
        else:
            anim_print(f"{the_or_no.capitalize()}{enemies[idx]} prepares to attack!")
            anim_print("Since you weren't expecting an ambush, you've been hit!")
            monster_attack.play()
            new_health -= enemy_attack
            anim_print(f"Your health decreases by {enemy_attack}!")
            anim_print(f"Your health dropped to {new_health}!")
            if new_health <= 0:
                if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                    sound.stop()
                    anim_print(f"{enemies[idx].capitalize()} feels bad for killing you so soon...")
                    sound.stop()
                    time.sleep(2)
                    anim_print("You died already...")
                    time.sleep(4)
                    anim_print("Overriding program...")
                    time.sleep(2)
                    anim_print("Resetting...")
                    time.sleep(2)
                    anim_print("Updating health to 100...")
                    time.sleep(1)
                    anim_print("Continuing code where it left off...")
                    time.sleep(1)
                    with open(statistics, 'r') as file:
                        reader = csv.reader(file)
                        items = list(reader)
                        item_to_remove = "your health".strip().capitalize()
                        items = [row for row in items if row[0].capitalize() != item_to_remove]
                    with open(statistics, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(items)
                    with open(statistics, 'a', newline='') as file:
                        new_item = "your health"
                        health = 100.0
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, health])
                        new_health = 100

                    with open(statistics, 'r') as file:
                        reader = csv.reader(file)
                        items = list(reader)
                        item_to_remove = "initial health".strip().capitalize()
                        items = [row for row in items if row[0].capitalize() != item_to_remove]
                    with open(statistics, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(items)
                    with open(statistics, 'a', newline='') as file:
                        new_item = "initial health"
                        health = 100
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, health])
                        new_health = 100
                else:
                    sound.stop()
                    time.sleep(2)
                    anim_print("You died already...")
                    time.sleep(4)
                    anim_print("Overriding program...")
                    time.sleep(2)
                    anim_print("Resetting...")
                    time.sleep(2)
                    anim_print("Updating health to 100...")
                    time.sleep(1)
                    anim_print("Continuing code where it left off...")
                    time.sleep(1)
                    with open(statistics, 'r') as file:
                        reader = csv.reader(file)
                        items = list(reader)
                        item_to_remove = "your health".strip().capitalize()
                        items = [row for row in items if row[0].capitalize() != item_to_remove]
                    with open(statistics, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(items)
                    with open(statistics, 'a', newline='') as file:
                        new_item = "your health"
                        health = 100.0
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, health])
                        new_health = 100
                    with open(statistics, 'r') as file:
                        reader = csv.reader(file)
                        items = list(reader)
                        item_to_remove = "initial health".strip().capitalize()
                        items = [row for row in items if row[0].capitalize() != item_to_remove]
                    with open(statistics, 'w', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerows(items)
                    with open(statistics, 'a', newline='') as file:
                        new_item = "initial health"
                        health = 100.0
                        csv_writer = csv.writer(file)
                        csv_writer.writerow([new_item, health])
                        new_health = 100
            anim_print("Now is your chance!")
            anim_print("You remember what to do, right?")
            anim_print(f"Show that {enemies[idx]} what you got before {she_he_it} gets a chance to attack again!")
            time.sleep(1)
            anim_print("Get ready!")
            time.sleep(1)
    data = []
    with open('stats.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_stat, life = row
            if row[0] == "your health":
                row[1] = str(new_health)
            data.append(row)
    with open('stats.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    hint_list = [f"\nThe enemy's health is {enemy_health}.\nThe enemy's attack is {enemy_attack}",
                 "There is a 5% chance of getting a really dangerous enemy",
                 "You have a 20% chance of running away successfully",
                 "Type 'no secret is truly a secret' when you are asked to attack, dodge, run, or check your inventory",
                 "There is a 10% chance of your item failing."]
    last_input = None
    secret_hint = False
    game_is_running = True
    while game_is_running:
        if not secret_hint:
            hint_chance = random.randint(1,1000)
            if hint_chance == 117:
                hint_yes_or_no = anim_input("Do you want a hint? Yes or no: ").capitalize()
                if hint_yes_or_no == "Yes":
                    hint = random.choice(hint_list)
                    anim_print(f"Secret Hint: {hint}.")
                    time.sleep(1)
                    secret_hint = True
                elif hint_yes_or_no == "No":
                    anim_print("Okay then.")
                    secret_hint = True
                else:
                    anim_print("Incorrect input...")
                    secret_hint = True  
            else:
                secret_hint = False
        data = []
        with open('stats.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == "your health":
                    initial_health = float(row[1])
                    row[1] = new_health
                data.append(row)
        with open('stats.csv', 'w', newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        attack_or_dodge = anim_input("Type 'A' to attack, 'D' to dodge, 'R' to run away, or 'E' to access your inventory: ").capitalize()
        if attack_or_dodge == "E" and last_input == "E":
            anim_print("You can't access your inventory 2 times in a row.")
        else:
            last_input = attack_or_dodge
        chance = random.choice([True, False])
        if attack_or_dodge == "A":
            if chance == True:
                game_is_running = True
                anim_print("You go in to defend yourself against your attacker by striking a blow...")
                time.sleep(2)
                anim_print("But you lose your balance and you miss...")
                if enemies[idx] != "Ana" and enemies[idx] != "Syuuran":
                    monster_attack.play()
                    anim_print(f"{the_or_no.capitalize()}{enemies[idx].capitalize()} turns around and {enemy_desc} at you! {attack_type}")
                    new_health -= enemy_attack
                    anim_print(f"Your health is now {new_health}")
                else:
                    enemy_attack_chance = random.choice([True,False])
                    if enemy_attack_chance == True:
                        game_is_running = True
                        anim_print(f"{enemies[idx].capitalize()} goes in for the attack.")
                        time.sleep(2)
                        anim_print(f"But {enemies[idx]} misses!")
                        anim_print("You got lucky.")
                    elif enemy_attack_chance == False:
                        game_is_running = True
                        anim_print(f"{enemies[idx].capitalize()} goes in for the attack.")
                        time.sleep(2)
                        anim_print(f"And {enemies[idx]} hits you!")
                        new_health -= enemy_attack
                        anim_print(f"Your health is now {new_health}!")
            if chance == False:
                game_is_running = True
                anim_print("You go in to defend yourself against your attacker by striking a blow...")
                time.sleep(2)
                anim_print(f"And you hit {the_or_no}{enemies[idx]} successfully!")
                hero_attack.play()
                enemy_health -= strength
                anim_print(f"{the_or_no.capitalize()}{enemies[idx].capitalize()}'s health is {enemy_health}")
            if enemy_health <= 0:
                if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                    sound.stop()
                    anim_print(f"You killed {enemies[idx]}...")
                    time.sleep(2)
                    anim_print(f"You have a feeling that you might see {her_him_it} again.")
                    win_sound.set_volume(2)
                    win_sound.play()
                    anim_print("YOU WIN!")
                    game_is_running = False
                    break
                else:
                    game_is_running = False
                    sound.stop()
                    win_sound.set_volume(2)
                    win_sound.play()
                    anim_print("YOU WIN!")
                    break
            if new_health <= 0:
                if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                    sound.stop()
                    anim_print(f"{enemies[idx].capitalize()} feels bad and cries.")
                    sound.stop()
                    time.sleep(2)
                    anim_print("You died...")
                    time.sleep(4)
                    anim_print("Overriding program...")
                    time.sleep(2)
                    anim_print("Resetting...")
                    time.sleep(1)
                    data = []
                    with open('stats.csv', 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            data.append(row)
                            if row[0] == "initial health":
                                initial_health = float(row[1])
                    for row in data:
                        if row[0] == "your health":
                            row[1] = str(initial_health)
                    with open('stats.csv', 'w', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(data)
                    new_health = initial_health
                    enemy_health = initial_enemy_health
                    game_is_running = True
                    sound.play(-1)
                else:
                    sound.stop()
                    anim_print("You died...")
                    time.sleep(4)
                    anim_print("Overriding program...")
                    time.sleep(2)
                    anim_print("Resetting...")
                    time.sleep(1)
                    data = []
                    with open('stats.csv', 'r') as file:
                        reader = csv.reader(file)
                        for row in reader:
                            data.append(row)
                            if row[0] == "initial health":
                                initial_health = float(row[1])
                    for row in data:
                        if row[0] == "your health":
                            row[1] = str(initial_health)
                    with open('stats.csv', 'w', newline="") as file:
                        writer = csv.writer(file)
                        writer.writerows(data)
                    new_health = initial_health
                    enemy_health = initial_enemy_health
                    game_is_running = True
                    sound.play(-1)
        elif attack_or_dodge == "D":
            if chance == True:
                if enemies[idx] != "Ana" and enemies[idx] != "Syuuran":
                    game_is_running = True
                    anim_print(f"{the_or_no.capitalize()}{enemies[idx]} {enemy_desc} at you with the intention to kill!")
                    time.sleep(2)
                    anim_print("But you trip and fall.")
                    time.sleep(1)
                    anim_print(f"{the_or_no.capitalize()}{enemies[idx]} is able to strike you while you're down.")
                    monster_attack.play()
                    anim_print("The attack hurts more than you think it should.")
                    new_health -= (enemy_attack * 1.5)
                    anim_print("The attack was 1.5 times stronger.")
                    anim_print(f"Your health is now {new_health}")
                else:
                    enemy_attack_chance = random.choice([True,False])
                    if enemy_attack_chance == True:
                        game_is_running = True
                        anim_print(f"{the_or_no.capitalize()}{enemies[idx]} {enemy_desc} at you with the intention to kill!")
                        time.sleep(2)
                        anim_print("But you trip and fall.")
                        time.sleep(2)
                        anim_print(f"Luckily for you, {enemies[idx]} misses!")
                        anim_print("You got lucky.")
                    elif enemy_attack_chance == False:
                        game_is_running = True
                        anim_print(f"{the_or_no}{enemies[idx]} {enemy_desc} at you with the intention to kill!")
                        time.sleep(2)
                        anim_print("But you trip and fall.")
                        time.sleep(2)
                        anim_print(f"And {enemies[idx]} hits you!")
                        new_health -= enemy_attack
                        anim_print(f"Your health is now {new_health}!")
            if chance == False:
                game_is_running = True
                anim_print(f"{the_or_no.capitalize()}{enemies[idx]} {enemy_desc} at you with the intention to kill!")
                time.sleep(2)
                anim_print(f"But you successfully dodged {the_or_no}{enemies[idx]}'s attack!")
                anim_print(f"{the_or_no.capitalize()}{enemies[idx]} falls to the ground after missing," +
                            f" and you're are able to attack while {the_or_no}{enemies[idx]} picks {herself_himself_itself} up off the ground!")
                hero_attack.play()
                enemy_health -= strength
                anim_print(f"{the_or_no.capitalize()}{enemies[idx]}'s health is now {enemy_health}!")
            if enemy_health <= 0:
                if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                    sound.stop()
                    anim_print(f"You killed {enemies[idx]}...")
                    time.sleep(2)
                    anim_print(f"You have a feeling that you might see {her_him_it} again.")
                    win_sound.set_volume(2)
                    win_sound.play()
                    anim_print("YOU WIN!")
                    game_is_running = False
                    break
                else:
                    game_is_running = False
                    sound.stop()
                    win_sound.set_volume(2)
                    win_sound.play()
                    anim_print("YOU WIN!")
                    break
        elif attack_or_dodge == "R":
            chance = random.randint(1, 100)
            if chance >= 20:
                if enemies[idx] != "Ana" and enemies[idx] != "Syuuran":
                    game_is_running = True
                    anim_print(f"You attempt to run away from {the_or_no}{enemies[idx]}...")
                    time.sleep(2)
                    anim_print("But you trip and fall.")
                    anim_print(f"{the_or_no.capitalize()}{enemies[idx]} is able to strike you while you're down.")
                    anim_print("The attack hurts more than you think it should.")
                    anim_print("The attack was 2 times stronger.")
                    new_health -= (enemy_attack * 2)
                    anim_print(f"Your health is now {new_health}")
                else:
                    enemy_attack_chance = random.choice([True,False])
                    if enemy_attack_chance == True:
                        game_is_running = True
                        anim_print(f"You attempt to run away from {the_or_no}{enemies[idx]}...")
                        time.sleep(2)
                        anim_print("But you trip and fall.")
                        time.sleep(2)
                        anim_print(f"{the_or_no.capitalize()}{enemies[idx]} tries to strike you while you're down.")
                        time.sleep(2)
                        anim_print(f"But {enemies[idx]} misses!")
                        anim_print("You quickly get up to avoid another attack!")
                        anim_print("You got lucky.")
                        game_is_running = True
                        break
                    elif enemy_attack_chance == False:
                        anim_print(f"You attempt to run away from {the_or_no}{enemies[idx]}...")
                        time.sleep(2)
                        anim_print("But you trip and fall.")
                        time.sleep(2)
                        anim_print(f"{the_or_no.capitalize()}{enemies[idx]} tries to strike you while you're down.")
                        time.sleep(2)
                        anim_print(f"And {enemies[idx]} succeeds!")
                        anim_print("The attack hurts more than you think it should.")
                        anim_print("The attack was 2 times stronger.")
                        new_health -= (enemy_attack * 2)
                        anim_print(f"Your health is now {new_health}")
                        game_is_running = True
                        break
                if new_health <= 0:
                    if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                        sound.stop()
                        anim_print(f"{enemies[idx].capitalize()} feels bad and cries.")
                        sound.stop()
                        time.sleep(2)
                        anim_print("You died...")
                        time.sleep(4)
                        anim_print("Overriding program...")
                        time.sleep(2)
                        anim_print("Resetting...")
                        time.sleep(1)
                        new_health = initial_health
                        data = []
                        with open('stats.csv', 'r') as file:
                            reader = csv.reader(file)
                            for row in reader:
                                data.append(row)
                                if row[0] == "initial health":
                                    initial_health = float(row[1])
                        for row in data:
                            if row[0] == "your health":
                                row[1] = str(initial_health)
                        with open('stats.csv', 'w', newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(data)
                        new_health = initial_health
                        enemy_health = initial_enemy_health
                        game_is_running = True
                        sound.play(-1)
                        break
                    else:
                        sound.stop()
                        anim_print("You died...")
                        time.sleep(4)
                        anim_print("Overriding program...")
                        time.sleep(2)
                        anim_print("Resetting...")
                        time.sleep(1)
                        data = []
                        with open('stats.csv', 'r') as file:
                            reader = csv.reader(file)
                            for row in reader:
                                data.append(row)
                                if row[0] == "initial health":
                                    initial_health = float(row[1])
                        for row in data:
                            if row[0] == "your health":
                                row[1] = str(initial_health)
                        with open('stats.csv', 'w', newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(data)
                        new_health = initial_health
                        enemy_health = initial_enemy_health
                        game_is_running = True
                        sound.play(-1)
            else:
                anim_print(f"You attempt to run away from {the_or_no}{enemies[idx]}...")
                time.sleep(2)
                anim_print(f"And you feel as if you're light as air as you run!")
                anim_print(f"You're not sure if {the_or_no}{enemies[idx]} chased after you. You were too scared to look behind you.")
                anim_print("But you think you made it somewhere safe!")
                sound.stop()
                time.sleep(2)
                win_sound.set_volume(2)
                win_sound.play()
                anim_print("You successfully ran away!")
                time.sleep(3)
                game_is_running = False
                break
        elif attack_or_dodge == "E":
            inventory_empty = True
            with open(filename, 'r') as collected_items:
                choice = csv.reader(collected_items)
                for row in choice:
                    inventory_empty = False
                    new_item, attack = row
            if inventory_empty:
                anim_print("There is nothing in your inventory.")
                time.sleep(1)
                anim_print("These are your statistics.")
                time.sleep(1)
                print()
                with open(statistics, 'r') as file:
                    anim_print("YOUR STATISTICS")
                    time.sleep(1)
                    choice = csv.reader(file)
                    for row in choice:
                        new_stat, kill_power = row
                        if new_stat == "your description":
                            words = kill_power.strip("()").replace("'", "").split(", ")
                            print(f"{new_stat.title()}: You are {words[0]} and kinda {words[1]}. There is not much else to say.")
                        elif new_stat != "initial health":
                            print(f"{new_stat.title()}: {kill_power.capitalize()}")
                        time.sleep(1)
                print()
            else:
                print()
                with open(statistics, 'r') as file:
                    anim_print("YOUR STATISTICS")
                    time.sleep(1)
                    choice = csv.reader(file)
                    for row in choice:
                        new_stat, kill_power = row
                        if new_stat == "your description":
                            words = kill_power.strip("()").replace("'", "").split(", ")
                            print(f"{new_stat.title()}: You are {words[0]} and kinda {words[1]}. There is not much else to say.")
                        elif new_stat != "initial health":
                            print(f"{new_stat.title()}: {kill_power.capitalize()}")
                        time.sleep(1)
                with open(filename, 'r') as collected_items:
                    print()
                    anim_print("YOUR INVENTORY")
                    choice = csv.reader(collected_items)
                    for row in choice:
                        new_item, attack = row
                        print(f"{new_item.title()}: {attack} damage")
                        time.sleep(1)
                print()
                inventory_yes_or_no = True
                while inventory_yes_or_no:
                    anim_print(f"Do you want to use something against {the_or_no}{enemies[idx]}?")
                    yes_no = anim_input("'Y' for yes or 'N' for no: ").upper()
                    if yes_no == "Y":
                        anim_print("Select something to use against your enemy.")
                        item_as_weapon = True
                        while item_as_weapon:
                            item_as_weapon = True
                            with open('project_inventory.csv', 'r') as collected_items:
                                reader = csv.reader(collected_items)
                                items = list(reader)
                                nonexistent_item = True
                                while nonexistent_item:
                                    item_to_remove = anim_input("Choose an item to use: ").strip().capitalize()
                                    item_exists = any(row[0].capitalize() == item_to_remove for row in items)
                                    if item_exists:
                                        nonexistent_item = False
                                        for row in items:
                                            if row[0].capitalize() == item_to_remove.capitalize():
                                                item_attack = row[1]
                                                
                                                item_fails = True
                                                item_chance = random.randint(1,100)
                                                while item_fails:
                                                    if item_chance >= 10:
                                                        enemy_health -= float(item_attack)
                                                        anim_print(f"You hit {the_or_no}{enemies[idx]} as hard as you can with your {item_to_remove.lower()}!")
                                                        anim_print(f"The enemy's health is now {enemy_health}!")
                                                        attack_or_dodge = True
                                                        break
                                                    else:
                                                        anim_print(f"You use your {item_as_weapon} to try and hit {the_or_no}{enemies[idx]} as hard as you can!")
                                                        anim_print("But you miss your target, and your item is lost.")
                                                        anim_print(f"You no longer have {item_as_weapon}.")
                                                        break
                                        items = [row for row in items if row[0].capitalize() != item_to_remove]
                                        with open('project_inventory.csv', 'w', newline='') as collected_items:
                                            writer = csv.writer(collected_items)
                                            writer.writerows(items)
                                    else:
                                        nonexistent_item = True
                                        anim_print(f"{item_to_remove.capitalize()} is not in your inventory.")
                                        print()
                            break
                        if enemy_health <= 0:
                            if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                                sound.stop()
                                anim_print(f"You killed {enemies[idx]}...")
                                time.sleep(2)
                                anim_print(f"You have a feeling that you might see {her_him_it} again.")
                                win_sound.set_volume(2)
                                win_sound.play()
                                anim_print("YOU WIN!")
                                game_is_running = False
                                break
                            else:
                                game_is_running = False
                                sound.stop()
                                win_sound.set_volume(2)
                                win_sound.play()
                                anim_print("YOU WIN!")
                                break
                        break
                    if yes_no == "N":
                        anim_print("Very well.")
                        time.sleep(1)
                        print()
                        attack_or_dodge = True
                        break
                    else:
                        anim_print("That's not what I asked.")
                        time.sleep(1)
                        attack_or_dodge = True
        elif attack_or_dodge == "No secret is truly a secret":
            inventory = []
            with open('project_inventory.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    inventory.append(row[0])
            items_to_add = [("ultimate sword", 1000)]
            for item, attack in items_to_add:
                if item not in inventory:
                    time.sleep(2)
                    anim_print("Where did you hear that...?", delay=0.182)
                    time.sleep(4)
                    inventory.append(item)
                    with open('project_inventory.csv', 'a', newline='') as file1, open('secret_items.csv', 'a', newline='') as file2:
                        writer1 = csv.writer(file1)
                        writer2 = csv.writer(file2)
                        writer1.writerow([item, attack])
                        writer2.writerow([item, attack])
                    anim_print("Something's changed...")
                    time.sleep(2)
                else:
                    monster_attack.play()
                    anim_print("You've been hit! What are you doing?")
                    anim_print("I mean...",delay=0.005)
                    anim_print(f"You froze, unable to act, and {the_or_no}{enemies[idx]} hits you!")
                    new_health -= (enemy_attack * 2.5)
                    anim_print(f"{the_or_no.capitalize()}{enemies[idx]}'s attack was 2.5 times stronger!")
                    anim_print(f"Your health is {new_health}!")
                    time.sleep(1)
                    if new_health <= 0:
                        if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                            sound.stop()
                            anim_print(f"{enemies[idx].capitalize()} feels bad and cries.")
                            sound.stop()
                            time.sleep(2)
                            anim_print("You died...")
                            time.sleep(4)
                            anim_print("Overriding program...")
                            time.sleep(2)
                            anim_print("Resetting...")
                            time.sleep(1)
                            data = []
                            with open('stats.csv', 'r') as file:
                                reader = csv.reader(file)
                                for row in reader:
                                    data.append(row)
                                    if row[0] == "initial health":
                                        initial_health = float(row[1])
                            for row in data:
                                if row[0] == "your health":
                                    row[1] = str(initial_health)
                            with open('stats.csv', 'w', newline="") as file:
                                writer = csv.writer(file)
                                writer.writerows(data)
                            new_health = initial_health
                            enemy_health = initial_enemy_health
                            game_is_running = True
                            sound.play(-1)
                        else:
                            sound.stop()
                            anim_print("You died...")
                            time.sleep(4)
                            anim_print("Overriding program...")
                            time.sleep(2)
                            anim_print("Resetting...")
                            time.sleep(1)
                            data = []
                            with open('stats.csv', 'r') as file:
                                reader = csv.reader(file)
                                for row in reader:
                                    data.append(row)
                                    if row[0] == "initial health":
                                        initial_health = float(row[1])
                            for row in data:
                                if row[0] == "your health":
                                    row[1] = str(initial_health)
                            with open('stats.csv', 'w', newline="") as file:
                                writer = csv.writer(file)
                                writer.writerows(data)
                            new_health = initial_health
                            enemy_health = initial_enemy_health
                            game_is_running = True
                            sound.play(-1)
                    elif new_health > 0:
                        anim_print("Try not to make a mistake next time.")
                        time.sleep(1)
        else:
                monster_attack.play()
                anim_print("You've been hit! What are you doing?")
                anim_print("I mean...",delay=0.005)
                anim_print(f"You froze, unable to act, and {the_or_no}{enemies[idx]} hits you!")
                new_health -= (enemy_attack * 2.5)
                anim_print(f"{the_or_no.capitalize()}{enemies[idx]}'s attack was 2.5 times stronger!")
                anim_print(f"Your health is {new_health}!")
                time.sleep(1)
                if new_health <= 0:
                    if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                        sound.stop()
                        anim_print(f"{enemies[idx].capitalize()} feels bad and cries.")
                        sound.stop()
                        time.sleep(2)
                        anim_print("You died...")
                        time.sleep(4)
                        anim_print("Overriding program...")
                        time.sleep(2)
                        anim_print("Resetting...")
                        time.sleep(1)
                        data = []
                        with open('stats.csv', 'r') as file:
                            reader = csv.reader(file)
                            for row in reader:
                                data.append(row)
                                if row[0] == "initial health":
                                    initial_health = float(row[1])
                        for row in data:
                            if row[0] == "your health":
                                row[1] = str(initial_health)
                        with open('stats.csv', 'w', newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(data)
                        new_health = initial_health
                        enemy_health = initial_enemy_health
                        game_is_running = True
                        sound.play(-1)
                    else:
                        sound.stop()
                        anim_print("You died...")
                        time.sleep(4)
                        anim_print("Overriding program...")
                        time.sleep(2)
                        anim_print("Resetting...")
                        time.sleep(1)
                        data = []
                        with open('stats.csv', 'r') as file:
                            reader = csv.reader(file)
                            for row in reader:
                                data.append(row)
                                if row[0] == "initial health":
                                    initial_health = float(row[1])
                        for row in data:
                            if row[0] == "your health":
                                row[1] = str(initial_health)
                        with open('stats.csv', 'w', newline="") as file:
                            writer = csv.writer(file)
                            writer.writerows(data)
                        new_health = initial_health
                        enemy_health = initial_enemy_health
                        game_is_running = True
                        sound.play(-1)
                elif new_health > 0:
                    anim_print("Try not to make a mistake next time.")
                    time.sleep(1)
                    game_is_running = True

    data = []
    with open('stats.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_stat, life = row
            data.append(row)
            if row[0] == "your health":
                row[1] = str(new_health)
    with open('stats.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)
    
    data = []
    with open('stats.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_stat, life = row
            data.append(row)
            if row[0] == "initial health":
                row[1] = str(new_health)
    with open('stats.csv', 'w', newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)

    time.sleep(2)
    sound.stop()
    anim_print("Loading...", delay=0.135)
    time.sleep(3)

random_enemy()
