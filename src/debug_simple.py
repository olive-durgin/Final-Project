import csv
filename = "project_inventory.csv"

print("Open the door.")
opening_door = True
while opening_door:
    inventory = True
    with open(filename, 'r') as collected_items:
        reader = csv.reader(collected_items)
        items = list(reader)
        print()
        nonexistent_item = True
        while nonexistent_item:
            item_to_remove = input("Enter the item to remove: ").strip().capitalize()
            item_exists = any(row[0].capitalize() == item_to_remove for row in items)
            if item_exists:
                nonexistent_item = False
                items = [row for row in items if row[0].capitalize() != item_to_remove]
                with open(filename, 'w', newline='') as collected_items:
                    writer = csv.writer(collected_items)
                    writer = csv.writer(collected_items)
                    writer.writerows(items)
                    print(f"{item_to_remove} removed.")
            else:
                nonexistent_item = True
                print(f"{item_to_remove} is not in the list.")
                print()
        if item_to_remove == "Rusty crowbar".capitalize():
            opening_door = True
            print("It breaks.")
        elif item_to_remove == "thick, metal bar".capitalize():
            opening_door = False
            print("It works! Bar is bent.")
            with open(filename, 'a', newline='') as file:
                new_item = "bent, metal bar"
                attack = 9
                csv_writer = csv.writer(file)
                csv_writer.writerow([new_item, attack])
        elif item_to_remove != "Thick, metal bar" and item_to_remove != "Rusty crowbar":
            opening_door = True
            print("It does not work.")
            with open(filename, 'a', newline='') as file:
                new_item = item_to_remove
                attack = 2
                csv_writer = csv.writer(file)
                csv_writer.writerow([new_item, attack])
            print("Item is damaged.")

print("Win!")
