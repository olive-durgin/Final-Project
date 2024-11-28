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

seen_towns = set()
all_choices = {"market", "school", "hospital", "playground", "pond"}
explore = True
while explore:
    if seen_towns == all_choices:
        explore = False
        break
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
        else:
            explore = True
            anim_print(f"You don't remember seeing {to_explore} on the map.")
            time.sleep(1)
anim_print("It works!")