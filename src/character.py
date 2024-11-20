username = input("Name: ").capitalize()
correct_choice = False
while not correct_choice:
        print("Who are you?")
        character_choice = input("Choose wisely: ").capitalize()
        if character_choice == "Ana" or character_choice == "Louis" or character_choice == username:
            correct_choice = True
        else:
            print("This is not what I asked for.")
if character_choice == "Ana":
    print("Okay...")
    print("Creating scenario...")
    print("Loading...")