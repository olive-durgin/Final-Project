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

    def attack_level():
        strength = True
        while strength:
            anim_print(f"On a scale of one to ten, how strong are you?")
            user_input = float(input("Choose wisely: "))
            if user_input >= float(1) and user_input <= float(10):
                strength = False
            if user_input > float(10) or user_input <= float(0):
                anim_print("This number is no good! Choose again!")
        attack_level = user_input
        return user_input
            # INSERT ELIF (ie. elif strength contains non#) - add a response for when the player responds with any sort of non-alphabetical character. 
            # if user_input != #numerical_value:
            # running = True
            # print("You call this a number...?")
            # starts over when the player answers something that isn't a number.
    attack_level()


    anim_print("Loading...", delay=0.135)
    time.sleep(1.5)
    anim_print(f"Hello, {username}!")
    anim_print("Welcome...")
    anim_print("You feel... odd.")
    anim_print("Who are you?")
    anim_print("Your choices have consequences.")
    anim_print("So choose wisely...")

    anim_print("Character: ANA")
    time.sleep(1)
    anim_print("Description: ___")
    time.sleep(1)
    anim_print("Health: 100")
    time.sleep(1)
    anim_print("Attack: 4")
    time.sleep(1)
    anim_print("Special Abilitiy: Discernment")
    time.sleep(1)
    anim_print("Weakness: ")
    time.sleep(1.5)

    anim_print("Character: LOUIS")
    time.sleep(1)
    anim_print("Description: ___")
    time.sleep(1)
    anim_print("Health: 100")
    time.sleep(1)
    anim_print("Attack: 4")
    time.sleep(1)
    anim_print("Special Abilitiy: Discernment")
    time.sleep(1)
    anim_print("Weakness: ")
    time.sleep(1.5)

    anim_print(f"Character: {username}")
    time.sleep(1)
    anim_print("Description: ___")
    time.sleep(1)
    anim_print("Health: 100")
    time.sleep(1)
    anim_print("Attack: 4")
    time.sleep(1)
    anim_print("Special Abilitiy: Discernment")
    time.sleep(1)
    anim_print("Weakness: ")
    time.sleep(1.5)

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
