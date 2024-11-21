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
        anim_print("Deleting...", delay=0.135)
        time.sleep(1)
        anim_print("Unable to fix error.")
        time.sleep(1)
        anim_print("Rebooting...", delay=0.135)
        time.sleep(1)
        anim_print("...", delay=0.135)
        time.sleep(2)
        anim_print("ERROR...")
        time.sleep(4)
        anim_print("Some say she's happy and kinda brave.")
        time.sleep(1)
        anim_print("Who says this, exactly?")
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        enemy_desc = "swings"
        a_or_an = ""
    if enemies[idx] == "Syuuran":
        anim_print("ERROR...")
        time.sleep(1)
        anim_print("Unknown files detected.")
        time.sleep(2)
        anim_print("Deleting...", delay=0.135)
        time.sleep(1)
        anim_print("Unable to fix error.")
        time.sleep(1)
        anim_print("Rebooting...", delay=0.135)
        time.sleep(1)
        anim_print("...", delay=0.135)
        time.sleep(2)
        anim_print("ERROR...")
        time.sleep(4)
        anim_print("Who says this, exactly?")
        attack_type = "(ie. the [enemy]'s teeth sinks its into your skin and you scream.)"
        enemy_desc = "swings"
        a_or_an = ""
    if enemies[idx] != "Ana" and enemies[idx] != "Syuuran":
        anim_print(description)
    anim_print("This is something you haven't seen before!")
    # access inventory
    anim_print(f"The {enemies[idx]} in front of you prepares to attack!")
    monster_attack.play()
    new_health -= enemy_attack
    anim_print(f"Your health decreases by {enemy_attack}!")
    anim_print(f"Your health dropped to {new_health}!")
    anim_print("Now is your chance!")
    anim_print("You remember what to do, right?")
    anim_print(f"Show that {enemies[idx]} what you got before it gets a chance to attack again!")
    anim_print("Be strategic about this, because sometimes, the enemy can be smarter than it looks.")
    anim_print("And don't wait too long.")
    anim_print("Feel free to use your inventory.")
    anim_print("Just make sure your attacks and dodges don't miss.")
    time.sleep(1)
    anim_print("They might.")
    time.sleep(1)
    anim_print(f"Your attack is {strength:.0f}.")
    anim_print(f"Your health is {new_health:.0f}!")
    anim_print("Get ready!")
    time.sleep(1)
    anim_print(f"The {enemies[idx]} prepares to attack!")
    anim_print(f"The {enemies[idx]} moves slowly but still manages to hit you!")

    game_is_running = True
    while game_is_running:
        while enemy_health > 0:
            attack_or_dodge = anim_input("Type A to 'attack' or D to 'dodge': ").capitalize()
            if attack_or_dodge == "A":
                hero_attack.play()
                enemy_health -= strength
                anim_print(f"The {enemies[idx]}'s health is now {enemy_health}!")
                if enemy_health <= 0:
                    game_is_running = False
                    sound.stop()
                    win_sound.set_volume(2)
                    win_sound.play()
                    anim_print("YOU WIN!")
                    break
                anim_print(f"The {enemies[idx]} {enemy_desc} at you!")
                monster_attack.play()
                new_health -= enemy_attack
                anim_print(f"{attack_type}")
                anim_print(f"Your health is now {new_health}!")
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
                anim_print(f"The {enemies[idx]} {enemy_desc} at you with the intention to kill!")
                anim_print(f"But you successfully dodged the {enemies[idx]}'s attack!")
                anim_print(f"The {enemies[idx]} falls to the ground after missing," +
                           f" and you're are able to attack while the {enemies[idx]} picks itself up off the ground!")
                hero_attack.play()
                enemy_health -= strength
                anim_print(f"The {enemies[idx]}'s health is now {enemy_health}!")
                if enemy_health <= 0:
                    game_is_running = False
                    sound.stop()
                    win_sound.set_volume(2)
                    win_sound.play()
                    anim_print("YOU WIN!")
                    time.sleep(3)
                    break
                pass
            else:
                monster_attack.play()
                new_health -= enemy_attack
                anim_print("You've been hit! What are you doing?")
                anim_print(f"Your health is {new_health}!")
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