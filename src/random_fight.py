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

    enemies = ["Ana"] * 1 + ["Syuuran"] * 1 + ["screaming, little freak"] * 5 + ["wild, flesh-eating monster"] * 5 + ["long cat", "mutated rat", "mutated dog", "odd badger", "odd elk", "long stoat"] * 88
    selected_enemy = random.choice(enemies)
    idx = enemies.index(selected_enemy)

    with open('stats.csv', 'r') as file:
        choice = csv.reader(file)
        for row in choice:
            if row[0] == "your attack":
                new_stat, kill_power = row
                strength = float(kill_power)
    with open('stats.csv', 'r') as file:
        choice = csv.reader(file)
        for row in choice:
            if row[0] == "your health":
                new_stat, life = row
                new_health = float(life)

    if enemies[idx] == "long cat":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "[This is the description for the long cat]!"
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        enemy_health = float(18)
        enemy_attack = float(6)
        enemy_desc = "pounces"
        a_or_an = " a"
    if enemies[idx] == "mutated rat":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "[This is the description for the mutated rat]!"
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        enemy_health = float(15)
        enemy_attack = float(10)
        enemy_desc = "snaps"
        a_or_an = " a"
    if enemies[idx] == "mutated dog":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "[This is the description for the mutated dog]!"
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        enemy_health = float(20)
        enemy_attack = float(15)
        enemy_desc = "lunges"
        a_or_an = " a"
    if enemies[idx] == "wild, flesh-eating monster":
        if "wild, flesh-eating monster" == "wild, flesh-eating monster":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "[This is the description for the WFEM]!"
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        enemy_health = float(30)
        enemy_attack = float(12)
        enemy_desc = "thrusts"
        a_or_an = " a"
    if enemies[idx] == "screaming, little freak":
        if "wild, flesh-eating monster" == "wild, flesh-eating monster":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "[This is the description for the screaming, little freak]!"
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        # appearance scares player and their guard is down. health is lowered and strength is lowered too.
        enemy_attack = float(5)
        enemy_health = float(100)
        enemy_health = float(45)
        enemy_attack = float(20)
        enemy_desc = "runs"
        a_or_an = " a"
    if enemies[idx] == "odd badger":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "[This is the description for the odd badger]!"
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        enemy_health = float(12)
        enemy_attack = float(6)
        enemy_desc = "thrashes"
        a_or_an = " an"
    if enemies[idx] == "odd elk":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "[This is the description for the odd elk]!"
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        # something about it is terribly wrong.
        enemy_health = float(50)
        enemy_attack = float(20)
        enemy_desc = "charges"
        a_or_an = " an"
    if enemies[idx] == "long stoat":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        description = "[This is the description for the long stoat]!"
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        enemy_health = float(9)
        enemy_attack = float(3)
        enemy_desc = "rushes"
        a_or_an = " a"
    if enemies[idx] == "Ana":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        enemy_health = float(100)
        enemy_attack = float(6)
        enemy_desc = "swings"
        a_or_an = ""
    if enemies[idx] == "Syuuran":
        if enemies[idx] == "wild, flesh-eating monster" or enemies[idx] == "screaming, little freak":
            eerie_sound = pygame.mixer.Sound(r'sounds\eerie_enemy.mp3')
            eerie_sound.play(-1)
        else:
            sound.play(-1)
        enemy_health = float(100)
        enemy_attack = float(4)
        enemy_desc = "swings"
        a_or_an = ""
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
        attack_type = "\nWith her knife loosely grasped in her shaking hands, Ana tries to stab you.\nThe knife cuts a deep gash in your skin.\nShe feels bad for hurting you."
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
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        enemy_desc = "swings"
        a_or_an = ""
    the_or_no = ""
    if enemies[idx] != "Ana" and enemies[idx] != "Syuuran":
        anim_print(description)
        if enemies[idx] != "Ana" and enemies[idx] != "Syuuran":
            the_or_no = "the "
        else:
            the_or_no = ""
    if enemies[idx] == "Ana":
        she_he_it = "she"
        her_him_it = "her"
        herself_himself_itself = "herself"
    elif enemies[idx] == "Syuuran":
        she_he_it = "he"
        her_him_it = "him"
        herself_himself_itself = "himself"
    else:
        she_he_it = "it"
        her_him_it = "it"
        herself_himself_itself = "itself"
    
    # anim_print("This is something you haven't seen before!")
    
    anim_print(f"{the_or_no.capitalize()}{enemies[idx]} prepares to attack!")
    anim_print("Since you weren't expecting an ambush, you've been hit!")
    monster_attack.play()
    new_health -= enemy_attack
    anim_print(f"Your health decreases by {enemy_attack}!")
    anim_print(f"Your health dropped to {new_health}!")
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
    
    hint_list = [f"\nThe enemy's health is {enemy_health}.\nThe enemy's attack is {enemy_attack}", "There is a 5% chance of getting a really dangerous enemy",
                 "You have a 20% chance of running away successfully", "Type 'no secret is truly a secret' when you are asked to attack, dodge, run, or check your inventory"]
    last_input = None
    secret_hint = False
    game_is_running = True
    while game_is_running:
        if not secret_hint:
            hint_chance = random.randint(1,1000)
            if hint_chance >= 10:
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
                break
        while enemy_health > 0:
            with open('stats.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    new_stat, life = row
                    data.append(row)
                    if row[0] == "your health":
                        initial_health = float(row[1])
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
                            anim_print(f"{enemies[idx].capitalize()} turns around and {enemy_desc} at you! {attack_type}")
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
                        anim_print(f"{enemies[idx].capitalize()}'s health is {enemy_health}")
                    if enemy_health <= 0:
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
                            new_health = initial_health
                            data = []
                            with open('stats.csv', 'r') as file:
                                reader = csv.reader(file)
                                for row in reader:
                                    if row[0] == "your health":
                                        row[1] = str(new_health)
                                    data.append(row)

                            with open('stats.csv', 'w', newline="") as file:
                                writer = csv.writer(file)
                                writer.writerows(data)
                            game_is_running = True
                            break
                        else:
                            sound.stop()
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
                                    if row[0] == "your health":
                                        row[1] = str(new_health)
                                    data.append(row)

                            with open('stats.csv', 'w', newline="") as file:
                                writer = csv.writer(file)
                                writer.writerows(data)
                            game_is_running = True
                            break
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
                        game_is_running = False
                        sound.stop()
                        win_sound.set_volume(2)
                        win_sound.play()
                        anim_print("YOU WIN!")
                        time.sleep(3)
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
                            elif enemy_attack_chance == False:
                                game_is_running = True
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
                                        if row[0] == "your health":
                                            row[1] = str(new_health)
                                        data.append(row)

                                with open('stats.csv', 'w', newline="") as file:
                                    writer = csv.writer(file)
                                    writer.writerows(data)
                                game_is_running = True
                            else:
                                sound.stop()
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
                                        if row[0] == "your health":
                                            row[1] = str(new_health)
                                        data.append(row)

                                with open('stats.csv', 'w', newline="") as file:
                                    writer = csv.writer(file)
                                    writer.writerows(data)
                                game_is_running = True
                                break
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
                    else:
                        print()
                        with open(statistics, 'r') as file:
                            anim_print("YOUR STATISTICS")
                            time.sleep(1)
                            choice = csv.reader(file)
                            for row in choice:
                                new_stat, kill_power = row
                                print(f"{new_stat.title()}: {kill_power}")
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
                                    game_is_running = False
                                    sound.stop()
                                    win_sound.set_volume(2)
                                    win_sound.play()
                                    anim_print("YOU WIN!")
                                    time.sleep(3)
                                    break
                                break
                            if yes_no == "N":
                                anim_print("Very well.")
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
                    time.sleep(2)
                    anim_print("Where did you hear that...?", delay=0.182)
                    time.sleep(4)
                    def add_to_inventory(item, attack):
                        if item not in inventory:
                            inventory.append(item)
                            with open('project_inventory.csv', 'a', newline='') as file1, open('secret_items.csv', 'a', newline='') as file2:
                                writer1 = csv.writer(file1)
                                writer2 = csv.writer(file2)
                                writer1.writerow([item, attack])
                                writer2.writerow([item, attack])
                            print(f"{item} added to inventory.")
                        else:
                            print("")
                    items_to_add = [("ultimate sword", 1000)]
                    for item, attack in items_to_add:
                        add_to_inventory(item, attack)
                    time.sleep(2)
                    anim_print("You got a new item.")
                    time.sleep(1)
                    anim_print("Check your inventory.")
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
                            new_health = initial_health
                            data = []
                            with open('stats.csv', 'r') as file:
                                reader = csv.reader(file)
                                for row in reader:
                                    if row[0] == "your health":
                                        row[1] = str(new_health)
                                    data.append(row)

                            with open('stats.csv', 'w', newline="") as file:
                                writer = csv.writer(file)
                                writer.writerows(data)
                            game_is_running = True
                            break
                        else:
                            sound.stop()
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
                                    if row[0] == "your health":
                                        row[1] = str(new_health)
                                    data.append(row)

                            with open('stats.csv', 'w', newline="") as file:
                                writer = csv.writer(file)
                                writer.writerows(data)
                            game_is_running = True
                            break
                    elif new_health > 0:
                        anim_print("Try not to make a mistake next time.")

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
    time.sleep(2)
    sound.stop()
    anim_print("Loading...", delay=0.135)
    time.sleep(3)

random_enemy()
