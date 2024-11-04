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

    strength = True
    while strength:
        try:
            anim_print(f"Pick a number between one and ten.")
            attack = float(input("Choose wisely: "))
            if 1 <= attack <= 10:
                strength = False
            else:
                anim_print("This is not what I asked for.")
                time.sleep(0.75)
        except ValueError:
            anim_print("Do you call that a number...?")
    anim_print("Loading...", delay=0.135)
    time.sleep(1.5)
    anim_print(f"Hello, {username}!")
    anim_print("Welcome...", delay=0.14)
    anim_print("You feel... odd.")
    time.sleep(1)
    anim_print("Who are you?")
    time.sleep(1)
    anim_print("Your choices have consequences.")
    time.sleep(0.5)
    anim_print("So choose wisely...")
    time.sleep(1)
    print()

    anim_print("Character: ANA")
    time.sleep(1)
    anim_print("Description: ___")
    time.sleep(1)
    anim_print("Health: 100")
    anim_print("Attack: 4")
    anim_print("Special Abilitiy: Discernment")
    anim_print("Weakness: ")
    time.sleep(1.5)
    print()

    anim_print("Character: LOUIS")
    time.sleep(1)
    anim_print("Description: ___")
    time.sleep(1)
    anim_print("Health: 100")
    time.sleep(1)
    anim_print("Attack: 7")
    time.sleep(1)
    anim_print("Special Abilitiy: Discernment")
    time.sleep(1)
    anim_print("Weakness: ")
    time.sleep(1.5)
    print()

    anim_print(f"Character: {username}")
    time.sleep(1)
    anim_print(f"Description: {username} is {adjective_01} and kinda {adjective_02}. There's not much else to say.")
    time.sleep(1)
    anim_print("Health: 100")
    time.sleep(1)
    anim_print(f"Attack: {attack}")
    time.sleep(1)
    anim_print("Special Abilitiy: Discernment")
    time.sleep(1)
    anim_print("Weakness: ")
    time.sleep(1.5)


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
