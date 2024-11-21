import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, time, random, csv, project
pygame.init()
sound = pygame.mixer.Sound(r'sounds\medium_fight.mp3')
win_sound = pygame.mixer.Sound(r'sounds\winner.mp3')
lose_sound = pygame.mixer.Sound(r'sounds\death.mp3')
hero_attack = pygame.mixer.Sound(r'sounds\hero_attack.mp3')
monster_attack = pygame.mixer.Sound(r'sounds\monster_bite.mp3')

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

    enemies = ["long cat", "mutated rat", "mutated dog", "wild, flesh-eating monster", "screaming, little freak", "odd badger", "odd elk", "long stoat", "Ana", "Syuuran"]
    idx = random.randrange(len(enemies))
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
        description = "This is the description for the long cat!"
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
        description = "This is the description for the mutated rat!"
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
        description = "This is the description for the mutated dog!"
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
        description = "This is the description for the WFEM!"
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
        description = "This is the description for the screaming, little freak!"
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        # appearance scares player and their guard is down. health is lowered and strength is lowered too.
        strength = float(5)
        health = float(100)
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
        description = "This is the description for the odd badger!"
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
        description = "This is the description for the odd elk!"
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
        description = "This is the description for the long stoat!"
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
    
    anim_print(f"{the_or_no.capitalize()}{enemies[idx]} in front of you prepares to attack!")
    anim_print("You've been hit!")
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
    anim_print(f"Your attack is {strength:.0f}.")
    anim_print(f"Your health is {new_health:.0f}!")
    anim_print("Get ready!")
    time.sleep(1)
    anim_print(f"{the_or_no.capitalize()}{enemies[idx]} prepares to attack!")
    anim_print(f"{the_or_no.capitalize()}{enemies[idx]} manages to hit you despite your attempt to avoid {her_him_it}!")
    new_health -= enemy_attack
    anim_print(f"Your health decreases by {enemy_attack} and your health is now {new_health}!")

    game_is_running = True
    while game_is_running:
        while enemy_health > 0:
            # add inventory option
            attack_or_dodge = anim_input("Type 'A' to attack, 'D' to dodge, or 'R' to run away: ").capitalize()
            chance = random.choice([True, False])
            if attack_or_dodge == "A":
                if chance == True:
                    game_is_running = True
                    anim_print("You go in to defend yourself against your attacker by striking a blow...")
                    time.sleep(2)
                    anim_print("But you lose your balance and you miss...")
                    monster_attack.play()
                    anim_print(f"{enemies[idx]} turns around and {enemy_desc} at you! {attack_type}")
                    new_health -= enemy_attack
                    anim_print(f"Your health is now {new_health}")
                if chance == False:
                    game_is_running = True
                    anim_print("You go in to defend yourself against your attacker by striking a blow...")
                    time.sleep(2)
                    anim_print(f"And you hit {the_or_no}{enemies[idx]} successfully!")
                    hero_attack.play()
                    enemy_health -= strength
                    anim_print(f"{enemies[idx]}'s health is {enemy_health}")
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
                        anim_print(f"{enemies[idx]} feels bad and cries.")
                        sound.stop()
                        time.sleep(2)
                        anim_print("You died...")
                        time.sleep(4)
                        anim_print("Overriding program...")
                        time.sleep(2)
                        anim_print("Resetting...")
                        time.sleep(1)
                        new_health = 100
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
                        new_health = 100
                        game_is_running = True
                        break
            elif attack_or_dodge == "D":
                if chance == True:
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
                if chance >= 10:
                    game_is_running = True
                    anim_print(f"You attempt to run away from {the_or_no}{enemies[idx]}...")
                    time.sleep(2)
                    anim_print("But you trip and fall.")
                    anim_print(f"{the_or_no.capitalize()}{enemies[idx]} is able to strike you while you're down.")
                    anim_print("The attack hurts more than you think it should.")
                    anim_print("The attack was 2 times stronger.")
                    new_health -= (enemy_attack * 2)
                    anim_print(f"Your health is now {new_health}")
                    if new_health < 10:
                        if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                            sound.stop()
                            anim_print(f"{enemies[idx]} feels bad and cries.")
                            sound.stop()
                            time.sleep(2)
                            anim_print("You died...")
                            time.sleep(4)
                            anim_print("Overriding program...")
                            time.sleep(2)
                            anim_print("Resetting...")
                            time.sleep(1)
                            new_health = 100
                            game_is_running = True
                        else:
                            sound.stop()
                            anim_print("You died...")
                            time.sleep(4)
                            anim_print("Overriding program...")
                            time.sleep(2)
                            anim_print("Resetting...")
                            time.sleep(1)
                            new_health = 100
                            game_is_running = True
                            break
                elif chance > 10:
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
                    attack_or_dodge = False
                    break
            else:
                monster_attack.play()
                anim_print("You've been hit! What are you doing?")
                anim_print("I mean...",delay=0.005)
                anim_print(f"You froze, unable to act and {the_or_no}{enemies[idx]} hits you!")
                new_health -= (enemy_attack * 2.5)
                anim_print(f"{the_or_no}{enemies[idx]}'s attack was 2.5 times stronger!")
                anim_print(f"Your health is {new_health}!")
                time.sleep(1)
                if new_health <= 0:
                    if enemies[idx] == "Ana" or enemies[idx] == "Syuuran":
                        sound.stop()
                        anim_print(f"{enemies[idx]} feels bad and cries.")
                        sound.stop()
                        time.sleep(2)
                        anim_print("You died...")
                        time.sleep(4)
                        anim_print("Overriding program...")
                        time.sleep(2)
                        anim_print("Resetting...")
                        time.sleep(1)
                        new_health = 100
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
                        new_health = 100
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
