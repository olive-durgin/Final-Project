import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame, time, csv, project
pygame.init()

sound = pygame.mixer.Sound(r'sounds\easy_fight.mp3')
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

def easy_fight():

    sound.play(-1)
    sound.set_volume(3)
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

    anim_print("You've been ambushed by a mutated rat!")
    anim_print("The rules are simple.")
    anim_print("Try not to get hit.")
    anim_print("Right after the enemy attacks, you have a window of opportunity to fight back.")
    anim_print("Don't miss this chance.")
    anim_print("Be strategic about this, because sometimes, the enemy can be smarter than it looks.")
    anim_print("You shouldn't have any issues with this particular enemy though.")
    anim_print("Feel free to take your time.")
    anim_print("There is no consequence for waiting too long.")
    anim_print("You won't need your inventory for this fight either.")
    anim_print("And since this is your first fight, your attacks and dodges won't fail you.")
    anim_print("It won't be like that in the future though.")
    anim_print(f"Your attack is {strength:.0f}.")
    time.sleep(1)
    anim_print("I hope you chose wisely.")
    time.sleep(1)
    anim_print(f"Your health is {new_health:.0f}!")
    anim_print("Get ready!")
    time.sleep(1)
    anim_print("The grotesque rat in front of you boasts its sharp teeth!")
    anim_print("The rat moves slowly but still manages to hit you!")
    enemy_attack = 10
    enemy_health = 15
    monster_attack.play()
    new_health -= enemy_attack
    anim_print(f"Your health decreases by {enemy_attack}!")
    anim_print(f"Your health dropped to {new_health}!")
    anim_print("Now is your chance!")
    anim_print("Show that rat what you got before it gets a chance to attack again!")
    sound.stop()
    game_is_running = True
    while game_is_running:
        sound.play(-1)
        sound.set_volume(3)
        while enemy_health > 0:
            attack_or_dodge = anim_input("Type A to 'attack' or D to 'dodge': ").capitalize()
            if attack_or_dodge == "A":
                hero_attack.play()
                enemy_health -= strength
                anim_print(f"The rat's health is now {enemy_health}!")
                if enemy_health <= 0:
                    game_is_running = False
                    sound.stop()
                    win_sound.set_volume(2)              
                    win_sound.play()
                    anim_print("YOU WIN!")
                    break
                anim_print("The rat lunges at you!")
                monster_attack.play()
                new_health -= enemy_attack
                anim_print("It's teeth sinks into your skin, and you scream.")
                anim_print(f"Your health is now {new_health}!")
                if new_health <= 0:
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
                anim_print("The rat lunges at you with the intention to kill!")
                anim_print("But you successfully dodged the rat's attack!")
                anim_print("The rat falls to the ground after missing, and you're are able to attack while the rat picks itself up off the ground!")
                hero_attack.play()
                enemy_health -= strength
                anim_print(f"The rat's health is now {enemy_health}!")
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

easy_fight()
