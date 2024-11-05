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

def easy_fight(strength):
        sound.play(loops=-1)
        anim_print("You've been ambushed by a low-level enemy!")
        anim_print("The rules are simple.")
        anim_print("Try not to get hit.")
        anim_print("Right after the enemy attack, you have a window of opportunity to fight back.")
        anim_print("Don't miss this chance.")
        anim_print("Be strategic about this, because sometimes, the enemy can be smarter than it looks.")
        anim_print("You shouldn't have any issues with this particular enemy though.")
        anim_print("Feel free to take your time.")
        anim_print("You won't need an inventory for this fight either.")
        strength = 10
        health = float(100)
        enemy_attack = float(5)
        enemy_health = float(15)
        new_health = health - enemy_attack
        # access inventory
        while enemy_health > 0:
            anim_print("The enemy in front of you boasts sharp teeth!")
            anim_print("The enemy moves slowly but still manages to hit you!")
            new_health -= enemy_attack
            anim_print(f"Your health decreases by {enemy_attack}!")
            anim_print(f"Your health dropped to {new_health}!")
            anim_print("Now is your chance!")
            anim_print("Show that monster what you got before it gets a chance to attack again!")

            attack_or_dodge = input("Type A to 'attack' or D to 'dodge': ")
            attack_or_dodge = attack_or_dodge.capitalize()
            if attack_or_dodge == "A":
                hero_attack.play()
                enemy_health -= strength
                print(f"The monster's health is now {enemy_health}!")
                if enemy_health <= 0:
                    sound.stop()
                    print("YOU WIN!")                   
                    win_sound.play()
                    time.sleep(5)
                    win_sound.stop()
                    break
                if new_health <= 0:
                    print("You died...")
                    lose_sound.play()
                    break
                print("The monster attacks you.")
                monster_attack.play()
                new_health -= enemy_attack
                print(f"Your health is {new_health}")
            elif attack_or_dodge == "D":
                print("You attack too!")
                hero_attack.play()
                enemy_health -= strength
                print(f"The monster's health is now {enemy_health}!")
                if enemy_health <= 0:
                    sound.stop()
                    print("YOU WIN!")
                    win_sound.play()
                    time.sleep(5)
                    win_sound.stop()
                    break
                if new_health <= 0:
                    print("You died...")
                    lose_sound.play()
                    break
            else:
                new_health -= strength
                monster_attack.play()
                print("You've been hit! What are you doing?")
                print(f"Your health: {new_health}!")
            if new_health <= 0:
                print("You died...")
                lose_sound.play()
                break
            if enemy_health <= 0:
                sound.stop()
                print("YOU WIN!")
                win_sound.play()
                time.sleep(5)
                win_sound.stop()
                break

        anim_print("Loading...", delay=0.135)
        time.sleep(3)

easy_fight()