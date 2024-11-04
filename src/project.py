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
    anim_print("Who are you? Do you know anymore?")
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
    anim_print("Special Ability: Observation")
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
        time.sleep(1)
        anim_print("Creating scenario...", delay=0.135)
        time.sleep(2)
        anim_print("Loading...", delay=0.135)
        time.sleep(2)
        anim_print("You open your tired eyes and look around the room.")
        anim_print("The room you're in resembles a huge metal box, but time and nature started eating away at it.")
        anim_print("Now, the large bolts that kept the room in one piece started to rust.")
        anim_print("And the metal plating that used to be the walls are warped and falling apart.")
        anim_print("Sunlight seeps through the cracks and gaps in the walls, and a strong smell of rain overwhelms your senses.")
        anim_print("You can hear the faint squeak of mice in the distance along with the rustling of trees.")
        anim_print("Despite there being a metal table in the room with a metal chair, you are lying on the cold, wet floor.")
        anim_print("Your clothes smell like mildew and moss now.")
        anim_print("What do you do? Leave or look around?")
        response = True
        while response:
            leave_or_look = anim_input("Leave or look: ").capitalize()
            if leave_or_look == "Look":
                leave_or_look = False
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
                anim_print("You slip you fingers into the crack between the wall and the door...", delay=0.14)
                time.sleep(1)
                anim_print("...but the door is too heavy to open.")
                anim_print("Maybe there is something in the room that can help you.")
                break
            if leave_or_look == "Leave":
                leave_or_look = False
                anim_print("You decide to try and find a way out of the metal box and you notice a door across the room.")
                anim_print("Your legs feel numb as you stand, and you stumble your way towards the door.")
                anim_print("Once closer, you find that the door is cracked open slightly.")
                anim_print("You slip you fingers into the crack between the wall and the door...")
                time.sleep(1)
                anim_print("...but the door is too heavy to open.")
                anim_print("Maybe you should look around for something to help you.")
                break
            else:
                leave_or_look = True
        anim_print("Looking around the room, you notice several places to investigate.")
        anim_print("Where do you look? The pile of leaves, under the table, or the hole in the wall?")
        looking = True
        while looking:
            to_look = anim_input("I look at the leaves, table, or wall: ").lower()
            if to_look == "leaves":
                looking = True
                anim_print("As your legs start to feel better, you make your way towards the pile of leaves.")
                anim_print("You reach down to move the leaves around and see if you find something.")
                anim_print("A as your hands are in the wet, mushy pile of leaves, you find a crowbar.")
                anim_print()
                anim_print("A crowbar was added to your inventory.")
            if to_look == "table":
                anim_print("You walk back over to the table you woke up next to.")
                anim_print("When you crouch down, to look under the table.")
                anim_print("You see nothing but scratches on the floor from the table legs and greenish coloured water stains.")
                anim_print("When you get up, you hit your head on the table.")
                anim_print("You found nothing but a headache.")
                anim_print("A headache was added to your inventory.")
                anim_print("As you stand there thinking about your headache, you hear soething fall to the floor.")
                anim_print("You look under the table again and see a strange, metal key on the floor.")
                anim_print("It must have been taped to the bottom of the table.")
                anim_print("A strange, metal key was added to your inventory. ")
            if to_look == "wall":
                anim_print()
        anim_print("")
        anim_print("")
        anim_print("")
        anim_print("")
        anim_print("")

    if character_choice == "Louis":
        anim_print("Interesting...")
        time.sleep(1)
        anim_print("Creating scenario...", delay=0.135)
        time.sleep(2)
        anim_print("Loading...", delay=0.135)

    if character_choice == username:
        anim_print("I see...")
        time.sleep(1)
        anim_print("Creating scenario...", delay=0.135)
        time.sleep(2)
        anim_print("Loading...", delay=0.135)


if __name__ == "__main__":
    opening_scene()
