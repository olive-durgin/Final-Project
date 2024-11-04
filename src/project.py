import time

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

def opening_scene():
    time.sleep(.07)
    anim_print("Loading...", delay=0.135)
    time.sleep(1.5)
    username = anim_input("Input your name: ")
    username = username.capitalize()
    adjective_01 = anim_input("Adjective 01: ")
    adjective_02 = anim_input("Adjective 02: ")
    anim_print("Loading...", delay=0.135)
    time.sleep(1.5)
    anim_print(f"Hello, {username}!")
    anim_print("Welcome...")
    anim_print("You feel... odd.")
    anim_print("Who are you?")
    anim_print("Your choices have consequences.")
    anim_print("So choose wisely...")


# Can input a name at the beginning.
# Loading...
# Hello. Please answer a few questions.
    # adjective 01: ___.
    # adjective 02: ___.
    # number between 1-10 (unspecified): ___.
# Player has the choice of picking between 3 different characters.
    # Characters have a descirption using adjectives.
    # Special skill.
    # Strength.
# Each player has a different ability, 
# Third character has the input name, adjectives in description, and strength is 1-10.
# Loading...
# Welcomed by the UI.
# 

if __name__ == "__main__":
    opening_scene()
