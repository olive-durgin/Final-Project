import time, random
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
        
        
anim_print("Type 'M' to move forward.")
walking_forward = True
count = 0
while walking_forward:
    move_forward = anim_input("Continue on? ").upper()
    while count < 6:
        chance = random.randint(1, 100)
        if move_forward == 'M':
            if chance <= 25 or chance >= 65:
                anim_print("You hear the rustling grow louder as something approaches you!")
                anim_print("INSERT ATTACK HERE!")
                anim_print("You were safely able to fend off your attacker!")
                anim_print("You should hurry up and get off of this trail.")
                anim_print("You're bound to be attacked again.")
                time.sleep(1)
                move_forward = False
                break
            else:
                anim_print("You safely move forward along the trail.")
                anim_print("You best hurry to the town.")
                time.sleep(1)
                count += 1
                if count == 6:
                    walking_forward = False
                    break
                else:
                    move_forward = False
                    break
        else:
            anim_print("You stop to take in your surrounding instead of moving forward.")
            anim_print("But you hear something rush up from behind you.")
            anim_print("You have no time to react!")
            anim_print("INSERT ATTACK HERE!")
            anim_print("You were safely able to fend off your attacker!")
            anim_print("You should hurry up and get off of this trail.")
            anim_print("You're bound to be attacked again.")
            time.sleep(1)
            move_forward = False
            break