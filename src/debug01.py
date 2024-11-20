import random

health = 100
attack = 5
new_health = health - attack

looping = True
while looping:
    print(f"Your health is {health}!")
    attack_or_dodge = input("Attack or dodge? ").lower()
    idx = random.choice([True, False])
    if idx == True:
        attack_or_dodge = True
        print("You've been attacked!")
        print(f"Your health is now {new_health}")
    if idx == False:
        attack_or_dodge = True
        print("You've dodged successfully!")
        print(f"Your health is {health}")
