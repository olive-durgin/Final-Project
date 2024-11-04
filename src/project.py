import time

def anim_print(AIUI_speech):

    for character in AIUI_speech:
        print(character, end = "", flush = True)
        time.sleep(0.052)
    print()

def opening_scene():
    anim_print("Loading...")


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
