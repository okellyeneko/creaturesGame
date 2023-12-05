# creaturesGame
by Eneko O'Kelly

This game was created using only python. 
It simulates turn-based combat between various fantasy creatures and characters. The battle takes place in rounds, where each objects: Goblin, Orc, Wizard, Archer, Wizard... takes turns to attack or perform special abilities.

Classes
Creature Class
The Creature class is the base class for all characters in the battle. It includes methods for attacking, checking life status, and selecting targets.

Goblin and Orc Classes
The Goblin and Orc classes inherit from the Creature class and represent specific types of creatures with unique abilities.

Warrior, Archer, and Wizard Classes
The Warrior, Archer, and Wizard classes are specialized characters with distinct abilities, such as shield up or shield down, power shots, and magical actions and spells.

Boss Class
The Boss class represents a formidable enemy with enhanced abilities. It can do special attacks based on certain conditions.

Battle Class
The Battle class orchestrates the entire battle. It initializes enemies, allies, and the player, sorts them based on their speed, and executes turns until a defeat condition is met.

Usage
Instantiate the Battle class.
Call the start method to start the battle.

There are mutliple commented scripts thoughout the code. This is simply to illustrate how different classes work and how objects from these classes interact with each other. Uncomment them to run them

Player Interaction:
During the player's turn, the user can choose from various actions:

F: Attack an enemy (select the enemy).
R: Recharge mana.
1: Heal an ally (select the ally).
2: Cast Firebolt on an enemy (select the enemy).
3: Perform Mass Heal on all allies.
4: Unleash a Fire Storm on all enemies.
Quit: Exit the game.

Made by Eneko O'Kelly
