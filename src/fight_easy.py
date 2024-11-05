import pygame, time, csv
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

        strength = float(10)
        health = float(100)
        enemy_attack = float(5)
        enemy_health = float(15)
        new_health = health - enemy_attack
        # access inventory
        sound.play(loops=-1)
        while enemy_health > 0:
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