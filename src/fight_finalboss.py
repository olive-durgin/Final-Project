# Easy fights are not complex.
# Medium fights are slightly harder.
# Hard fights are really hard.
# Boss fights have a custom enemy that the user inputs.
# Final fight is the player's weakness. The fight does not loop if you lose,
# and you have to start the entire game over.

def finalboss_fight():

        strength = float(10)
        health = float(100)
        enemy_attack = float(5)
        enemy_health = float(15)
        new_health = health - enemy_attack

        while enemy_health > 0:
            attack_or_dodge = input("Type A to 'attack' or D to 'dodge': ")
            attack_or_dodge = attack_or_dodge.capitalize()
            if attack_or_dodge == "A":
                enemy_health -= strength
                print(f"The monster's health is now {enemy_health}!")
                if enemy_health <= 0:
                    print("YOU WIN!")
                    break
                if  new_health <= 0:
                    print("You died...")
                    break
                print("The monster attacks you.")
                new_health -= enemy_attack
                print(f"Your health is {new_health}")
            elif attack_or_dodge == "D":
                print("You attack too!")
                enemy_health -= strength
                print(f"The monster's health is now {enemy_health}!")
                if enemy_health <= 0:
                    print("YOU WIN!")
                    break
                if new_health <= 0:
                    print("You died...")
                    break
            else:
                new_health -= strength
                print("You've been hit! What are you doing?")
                print(f"Your health: {new_health}!")
            if new_health <= 0:
                print("You died...")
                break
            if enemy_health <= 0:
                print("YOU WIN!")
                break

finalboss_fight()