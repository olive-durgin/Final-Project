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

seen_inputs = set()
all_choices = {"leaves", "table", "wall"}

looking = True
while looking:
    to_look = anim_input("You look at the leaves, table, or wall: ").lower()
    if to_look in seen_inputs:
        anim_print("You already looked there. Try again.")
    else:
        seen_inputs.add(to_look)
        if to_look == "leaves":
            looking = True
            anim_print("You find a crowbar in the leaves.")
        if to_look == "table":
            looking = True
            anim_print("You find a key under the table.")
        if to_look == "wall":
            looking = True
            anim_print("You break a bar off the window.")
    if seen_inputs == all_choices:
        looking = False
