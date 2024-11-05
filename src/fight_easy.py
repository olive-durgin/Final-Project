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

def easy_fight(strength):
        sound.play(loops=-1)
        anim_print("You've been ambushed by a low-level enemy!")
        anim_print("The rules are simple.")
        anim_print("Try not to get hit.")
        anim_print("Right after the enemy attacks, you have a window of opportunity to fight back.")
        anim_print("Don't miss this chance.")
        anim_print("Be strategic about this, because sometimes, the enemy can be smarter than it looks.")
        anim_print("You shouldn't have any issues with this particular enemy though.")
        anim_print("Feel free to take your time.")
        anim_print("You won't need an inventory for this fight either.")
        anim_print("Unfortunately, since this is your first fight, you're nervous.")
        anim_print("So, you're attacks aren't as strong.")
        anim_print("Your attack is set to 5")
        strength = float(5)
        health = float(100)
        enemy_attack = float(5)
        enemy_health = float(15)
        new_health = health - enemy_attack
        # access inventory
        anim_print("The enemy in front of you boasts sharp teeth!")
        anim_print("The enemy moves slowly but still manages to hit you!")
        new_health -= enemy_attack
        anim_print(f"Your health decreases by {enemy_attack}!")
        anim_print(f"Your health dropped to {new_health}!")
        anim_print("Now is your chance!")
        anim_print("Show that monster what you got before it gets a chance to attack again!")
        while enemy_health > 0:
            attack_or_dodge = input("Type A to 'attack' or D to 'dodge': ")
            attack_or_dodge = attack_or_dodge.capitalize()
            if attack_or_dodge == "A":
                hero_attack.play()
                enemy_health -= strength
                anim_print(f"The monster's health is now {enemy_health}!")
                if enemy_health <= 0:
                    sound.stop()
                    anim_print("YOU WIN!")                   
                    win_sound.play()
                    time.sleep(5)
                    win_sound.stop()
                    break
                if new_health <= 0:
                    anim_print("You died...")
                    time.sleep(4)
                    lose_sound.stop()
                    anim_print("Overriding program...")
                    time.sleep(2)
                    anim_print("Resetting...")
                    lose_sound.play()
                    break
                anim_print("The monster attacks you.")
                monster_attack.play()
                new_health -= enemy_attack
                anim_print(f"Your health is {new_health}")
            elif attack_or_dodge == "D":
                anim_print("You successfully dodged the monster's attack!")
                anim_print("Be careful! Next time you might not be so lucky!")
                anim_print("You're are able to attack while the monster picks itself up off the ground!")
                hero_attack.play()
                enemy_health -= strength
                anim_print(f"The monster's health is now {enemy_health}!")
                if enemy_health <= 0:
                    sound.stop()
                    anim_print("YOU WIN!")
                    win_sound.play()
                    time.sleep(5)
                    win_sound.stop()
                    break
                if new_health <= 0:
                    lose_sound.play()
                    anim_print("You died...")
                    time.sleep(4)
                    lose_sound.stop()
                    anim_print("Overriding program...")
                    time.sleep(2)
                    anim_print("Resetting...")
                    break
            else:
                new_health -= strength
                monster_attack.play()
                anim_print("You've been hit! What are you doing?")
                anim_print(f"Your health: {new_health}!")
            if new_health <= 0:
                print("You died...")
                lose_sound.play()
                time.sleep(4)
                lose_sound.stop()
                anim_print("Overriding program...")
                time.sleep(2)
                anim_print("Resetting...")
                break
            if enemy_health <= 0:
                sound.stop()
                anim_print("YOU WIN!")
                win_sound.play()
                time.sleep(5)
                win_sound.stop()
                break

        anim_print("Loading...", delay=0.135)
        time.sleep(3)

easy_fight(100)