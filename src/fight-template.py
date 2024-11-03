def main():

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
                print("The monster attacks you.")
                new_health -= enemy_attack
                print(f"Your health is {new_health}")
            elif attack_or_dodge == "D":
                print("You attack too!")
                enemy_health -= strength
                print(f"The monster's health is now {enemy_health}!")
            else:
                new_health -= strength
                print("You've been hit! What are you doing?")
                print(f"Your health: {new_health}!")

            if new_health <= 0:
                print("You died...")
                break

main()