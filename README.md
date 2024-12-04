# Project Title
MYSTEYR OF SEONA (demo)

## Demo Video
Demo Video Link: [LINK GOES HERE]

## GitHub Repository
GitHub Repository Link: https://github.com/olive-durgin/Final-Project.git

## Description
Mystery of Seona follows the story of a person who wakes up alone in a worn down, overgrown room. They later escape to find that the world around them is in ruins. Throughout the game demo, the player has to collect clues to find out what happened to the city of Seona, and figure out what caused the end of the world. The player can make various choices that changes the outcome of the game, and the player must fight off enemy attack in turn-based combat.

## Different Files
The game demo consists of various files with the main file being project.py. The other files including fight scenes and csv files for stats and inventories are imported into the main file.

### Project.py
The main file, project.py contains the main story of the game where the player makes choices that affects the sotry of the game. For this part of the game, the story is rather linear since the demo only contains the prologue and part of the first chapter, but when given prompts on what to do, the player has a choice between choosing to do different little things. To keep the story interesting and not soley just reading text on the screen without interaction, the player often chooses which path to take and what doors to open, and walking in certain directions allows for the player to mainally move forward once. When the player moves forward, there is a random chance that they can be ambushed. Everytime the player is ambushed, they do not move forward, and if they give an incorrect input, they move back one time. A counter is implimented so that the number of times the player moves forward is kept track of. Once the number of times that the player moves forward is met, which is usually around 5, they reach their destination and the story continues.

### First_fight.py
Fight_fight.py is the first fight that the player gets into to against an enemy once they escape the room that they are trapped in. This is essentially a demo version that walks the player through how a basic fight against an enemy works. Since this is essentially a tutorial, this file is only imported once. The fight itself is rather basic and you can only attack or dodge. The attack and dodge is gauranteed to work, unlike in the main fight file to help the player get accustomed to the controls.

### Random_fight.py
Random_fight.py is the main file used whenever the player is ambushed throughout the game. This file is the most complex file out of all of them since it has the most features. The file contains a list of enemies that are chosen at random so that everytime the file is run, the enemy can potentially be different. Each enemy has a different chance of showing up. There is around an 80% chance of getting an easier enemy, and the other 20% is reserved for harder enemies. Each enemy has a different description that is read when the player is ambushed by them, the attack and health of each enemy is also different, and if you get two of the harder enemies, the music in the background changes so something eerier. Depending on the enemy as well, he/him/himself, she/her/herself, and it/its/itself is used and the grammar of sentences will change slightly depending on the enemy (ie. if the enenmy is "odd elk", the code will print "an odd elk", not "a odd elk").

In this fight file, the player can attack, dodge, run away, access their inventory, or reveal a secret.

When the player attacks an enemy, there is a 50% chance that the attack will succeed. If the attack succeeds, the enemy loses health and the player can take another turn. If the attack fails, the player loses health and can take another turn. However, if the enemy is "Ana" or "Syuuran", they have a 50% chance of their attacks failing because they are special enemies. In the beginning of the game, the player has a chance to choose Ana, Syuuran, or whatever name they input to continue with for their story. Ana and Syuuran are not available options because this is the demo game, but they are potential enemies in fight levels. Since all three potential characters can be controlled by the player, that is why Ana and Syuuran's chance of attacking is 50%.

When the player dodges an enemy's attack, there is a 50% chance that the dodge will succeed. The rules are essentially the same for dodge like in attack, and Ana and Syuuran have a 50% chance of hitting you if you dodge fails. This time, if the player fails to dodge, the enemy's attack is 1.5 times stronger.

When the player attempts to run away, there is a 20% chance that the player will succeed. If the player succeeds, the round ends and the player is brought back to the main story. If the player fails, the enemy attacks and the attack is 2 times stronger. Like in attack and dodge, Ana and Syuuran have a 50% chance of hitting the player if they fail to run away.

When the player accesses their inventory, if their inventory is empty, only their statistics (including health and attack) are read to them. If there is an item in their inventory, the statistics and the items in their inventory are read to them. When changing stats in the csv file, I just removed and readded stats to the file because I kept messing up the code on simply replacing the file and I kept creating bugs. To give the illusion that all of the items in the statistics lists are in the same order, I had the code read the items in the list in a specified order.

Later on in the game, there is a survivor that you meet and she joins you when you fight. There is a counter that is put in place, and every two attacks you make, the survivor can make one attack, which has a 90% success rate. If the survivor is the only thing in your inventory and the survivor is not ready to attack, the code will read that the inventory is empty. If the survivor is the only thing in the inventory but is also ready to attack, you can access your inventory. I did this because if the survivor is not ready to attack, the survivor is the only thing in the inventory, and the player tries to use the survivor to attack the enemy, there will be an infinate loop of the player not being able to leave their inventory, because the survivor will always not be ready to attack. I thought it would be easier to not read the survivor as in the inventory until the counter is ready rather than code an exception for the loop.

Items in your inventory can be used as weapons. Later on, I will had the chance to use special items as healing items, but I haven't coded that yet. For now, the player's inventory is read and the player is asked whether they want to use an item against the enemy. If they say yes, they are given the option to choose an item. If the item is not in the inventory, the player is asked again to choose an item. When they choose an item that is in the inventory, it is deleted and the item's number associated with it is converted to a float and used against the enemy. If the item they selected is the survivor, the survivor is not deleted from the inventory and the counter just resets to 0. Using items as weapons, including the survivor's attack, has a 90% success rate.

Since some of the items in the inventory that you collect can be super powerful, you cannot access your inventory two times in a row. If you do, you will be asked to input again.

There are basic secrets in the random_fight.py file and there is a 1/1000 chance that you can get a hint while in the fight. The hint is only shown once per fight whether the player accepts the hint or not. If you get a chance to get a hint, a hint is given to you at random. There is a chance that you are given a phrase to input when asked to attack, dodge, etc. And if you input this phrase, you get a secret item. That item is added to two files. The inventory and a secret_items.csv file. It is added to both files so that even if the player uses the item and it is removed from their inventory, the item is still in the secrets file. If the player tries to type in the phrase again, the code will read that the secret item is in the secret_item.py file still, and the player will be attacked as if they gave an incorrect input.

If the player gives an input that is not a part of the options, the player is attacked by the enemy.

The player's health is overriden everytime a turn ends and the code loops so that if the player looks at their inventory and sees their stats, the player's health is accurately read from the csv file. The health also updates before the loop starts when the player is initially ambushed and their health goes down. The initial health that the player has when the code starts is saved, in the csv file, and if the player dies, the player's health is overridden to match the initial health that the player had when they were first ambushed. The enemy's health resets as well. Once the player wins, the initial health is overridden to match the health that the player wins the game with. For example, if the player kills the enemy and their final health is 80 and their initial health is 30, the initial health will be overridden to match 80.

Once the player wins, their attack increases by a specified amount. If the player kills a harder enemy, Ana, or Syuuran, their level up is higher. If the player kills an easy enemy, their level up is lower. If the player runs away, their level up is automatically set to 1 no matter what enemy they fought.

### Hard_random_enemy.py
Hard_random_enemy.py is a fight file that is imported into the main script. It is nearly identical to random_fight.py, but the enemy list is shorter, containing only the harder enemies to fight in random_fight.py. This script is essentially a mini boss fight, and there is a lesser chance that the player can run away when fighting.