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
    anim_print("Running info collection program...", delay=0.135)
    time.sleep(1.5)
    username = anim_input("Input your name: ").capitalize()
    adjective_01 = anim_input("Adjective 01: ")
    adjective_02 = anim_input("Adjective 02: ")
    ability = anim_input("What are you good at? ")
    weakness = anim_input("What scares you? ")
    strength = True
    while strength:
        try:
            anim_print(f"Pick a number between one and ten.")
            attack = float(anim_input("Choose wisely: "))
            if 1 <= attack <= 10:
                strength = False
            else:
                anim_print("This is not what I asked for.")
                time.sleep(0.75)
        except ValueError:
            anim_print("Do you call that a number...?")
    anim_print("Loading...", delay=0.135)
    time.sleep(1.5)
    print()
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
    anim_print("Description: Ana is happy and kinda brave. There's not much else to say.")
    time.sleep(1)
    anim_print("Health: 100")
    anim_print("Attack: 6")
    anim_print("Special Ability: Discernment")
    anim_print("Weakness: Spiders")
    time.sleep(1.5)
    print()

    anim_print("Character: LOUIS")
    time.sleep(1)
    anim_print("Description: Louis is scared and kinda alone. There's not much else to say.")
    time.sleep(1)
    anim_print("Health: 100")
    anim_print("Attack: 4")
    anim_print("Special Ability: Persuasion")
    anim_print("Weakness: Mice")
    time.sleep(1.5)
    print()

    anim_print(f"Character: {username.upper()}")
    time.sleep(1)
    anim_print(f"Description: {username.title()} is {adjective_01} and kinda {adjective_02}. There's not much else to say.")
    time.sleep(1)
    anim_print("Health: 100")
    anim_print(f"Attack: {attack}")
    anim_print(f"Special Ability: {ability.capitalize()}")
    anim_print(f"Weakness: {weakness.capitalize()}")
    time.sleep(2)
    print()
    correct_choice = True
    correct_choice = False
    while not correct_choice:
            anim_print("Who are you?")
            character_choice = anim_input("Choose wisely: ").capitalize()
            if character_choice == "Ana" or character_choice == "Louis" or character_choice == username:
                correct_choice = True
            else:
                anim_print("This is not what I asked for.")

    if character_choice == "Ana":
        anim_print("Okay...")
        anim_print("Creating scenario...", delay=0.135)
        time.sleep(2)
        anim_print("Loading...", delay=0.135)
        time.sleep(2)
        anim_print("You open your tired eyes and look around the room.")
        anim_print("The room resembles a huge metal box, but time and nature started eating away at it.")
        anim_print("Now, the large bolts that kept the room in one piece started to rust.")
        anim_print("And the metal plating that used to be the walls are warped and falling apart.")
        anim_print("Sunlight seeps through the cracks and gaps in the walls, and a strong smell of rain overwhelms your senses.")
        anim_print("You can hear the faint squeak of mice in the distance along with the rustling of trees.")
        anim_print("What do you do? Leave or look around?")
        choice = anim_input("Leave or look: ").capitalize()
        if choice == "Look":
            anim_print("You look at your surroundings.")
            anim_print("You notice moss is slowly but surely inching its way along the walls.")
            anim_print("In time, the walls will be covered in it.")
            time.sleep(.75)
            anim_print("You see that leaves adorn the floor of the metal room closest to the broken wall.")
            anim_print("Leaves must have fallen into the room from outside.")
            time.sleep(.75)
            anim_print("You look across the room.")
            time.sleep(.10)
            anim_print("There is a door...")
            anim_print("Maybe you'll be able to leave. And hopefully find a way home.")
            anim_print("Your legs feel numb as you stand, and you stumble your way towards the door.")
            anim_print("Once closer, you find that the door is cracked open slightly.")
            anim_print("You slip you fingers into the crack between the wall and the door...")
            time.sleep(1)
            anim_print("...but the door is too heavy to open.")
            anim_print("Maybe there is something in the room that can help you.")
        if choice == "Leave":
            anim_print("You decide to try and find a way out of the metal box and you notice a door across the room.")
            anim_print("Your legs feel numb as you stand, and you stumble your way towards the door.")
            anim_print("Once closer, you find that the door is cracked open slightly.")
            anim_print("You slip you fingers into the crack between the wall and the door...")
            time.sleep(1)
            anim_print("...but the door is too heavy to open.")
            anim_print("Maybe you should look around for something to help you.")
        anim_print("")
        anim_print("")
        anim_print("")
        anim_print("")
        anim_print("")
        anim_print("")
        anim_print("")

    if character_choice == "Louis":
        anim_print("Interesting...")
        anim_print("Creating scenario...", delay=0.135)
        time.sleep(2)
        anim_print("Loading...", delay=0.135)

    if character_choice == username:
        anim_print("I see...")
        anim_print("Creating scenario...", delay=0.135)
        time.sleep(2)
        anim_print("Loading...", delay=0.135)


if __name__ == "__main__":
    opening_scene()
