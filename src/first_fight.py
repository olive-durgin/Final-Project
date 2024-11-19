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

    game_is_running = True
    while game_is_running:
        sound.play(-1)
        strength = float(5)
        new_health = float(100)
        enemy_attack = float(25)
        enemy_health = float(15)
        while enemy_health > 0:
            attack_or_dodge = anim_input("Type A to 'attack' or D to 'dodge': ").capitalize()
            if attack_or_dodge == "A":
                enemy_health -= strength
                anim_print(f"The rat's health is now {enemy_health}!")
                if enemy_health <= 0:
                    anim_print("YOU WIN!")
                    sound.stop()
                    game_is_running = False
                    break
                new_health -= enemy_attack
                anim_print(f"Your health is now {new_health}!")
                if new_health <= 0:
                    anim_print("You died...")
                    sound.stop()
                    game_is_running = False
                    break
            elif attack_or_dodge == "D":
                enemy_health -= strength
                anim_print(f"The rat's health is now {enemy_health}!")
                if enemy_health <= 0:
                    game_is_running = False
                    anim_print("YOU WIN!")
                    break
            else:
                new_health -= enemy_attack
                anim_print("You've been hit! What are you doing?")
                anim_print(f"Your health is now {new_health}!")
                if new_health <= 0:
                    anim_print("You died...")
                    sound.stop()
                    game_is_running = True
                    break
    time.sleep(2) 
    sound.stop()
    anim_print("Loading...", delay=0.135)
    time.sleep(3)
easy_fight()
