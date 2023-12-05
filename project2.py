import random
import time

class Creature:
    def __init__(self, name, maxHP=10):
        self.name = name
        self.maxHP = maxHP
        self.HP = maxHP
        self.abilities = {'Attack': 1, 'Defence': 5, 'Speed': 5}
        self.fainted = False

    def check_life(self):
        if self.HP <= 0:
            if self.fainted == False:
              self.HP = 0
              self.fainted = True
              print(f"{self.name} has fainted.")
        return self.HP

    def attack(self, other):
        if self.check_life() > 0:
            roll = random.randint(1, 20)
            if roll < other.abilities['Defence'] + other.abilities['Speed']:
                return f'{self.name} attacks {other.name}.\nAttack missed...'
            else:
                damage = self.abilities['Attack'] + random.randint(0, 4)
                if other.HP - damage < 0:
                    other.HP = 0  
                else:
                    other.HP -= damage
                    if other.HP < 0:
                        other.HP = 0
                return f'{self.name} attacks {other.name}.\nAttack hits for {damage} damage. HP left of {other.name}: {other.HP}.'
        
    def auto_select(self, target_list):
        alive = []
        for x in target_list:
            if x.check_life() > 0:
                alive.append(x)
        if alive:
          chosenTarget = random.choice(alive)
          return chosenTarget
        else:
          return None
        
    def turn(self, round_num, target_list):
        # print(f"Round: {round_num}")
        if self.check_life() > 0:
            target = self.auto_select(target_list)
            if target:
                result = self.attack(target)
                print(result)
                target.check_life()
            else:
                print(f'{self.name} has no targets, all opponents have fainted')

    


# def winner(creatures):
#     return all(creature.HP <= 0 for creature in creatures)

# team1 = [Creature("Frodo"), Creature("Samwise"), Creature("Pippin")]
# team2 = [Creature("Merry"), Creature("Aragorn"), Creature("Legolas")]


# for round in range(1, 21):
#     print(f"\nRound: {round}")
    
#     for x in team1:
#         if x.check_life() > 0:
#           x.turn(round, team2) 

#     for y in team2:
#       if y.check_life() > 0:
#         y.turn(round, team1)  

#     if winner(team1):
#         print("All Team 1 has fainted! Team 2 wins.")
#         break
#     elif winner(team2):
#         print("All Team 2 has fainted! Team 1 wins.")
#         break


class Goblin(Creature):
        def __init__(self, name, maxHP=15):
            super().__init__(name, maxHP=maxHP)
            self.abilities = {'Attack': 3, 'Defence': 6, 'Speed': 6}

class Orc(Creature):
        def __init__(self, name, maxHP=50):
            super().__init__(name, maxHP=maxHP)
            self.abilities = {'Attack': 5, 'Defence': 8, 'Speed': 3}
            self.attackBoost = False

        def heavy_attack(self, target):
            if self.attackBoost == False:
              self.abilities['Attack'] += 5
              self.abilities['Defence'] -= 3
              self.attackBoost = True
              print(f"{self.name} is in rage! attack +5, defence -3")

            return super().attack(target)
            
        def attack(self, target):
            if self.attackBoost == True:
              self.abilities['Attack'] -= 5
              self.abilities['Defence'] += 3
              self.attackBoost = False
              print(f"{self.name} is cooled down! attack -5, defence +3")
            return super().attack(target)
        
        def turn(self, round_num, target_list):
            target = self.auto_select(target_list)
            if target:
                if round_num % 4 == 0:
                    result = self.heavy_attack(target)
                else:
                    result = self.attack(target)
                print(result)
                target.check_life()
            else:
                print(f'{self.name} has no targets, all opponents have fainted')


# def winner(creatures):
#     return all(creature.HP <= 0 for creature in creatures)

# team1 = [Goblin("Goblin1")]
# team2 = [Orc("Orc")]

# for round in range(1, 21):
#     print(f"\nRound: {round}")
    
#     for x in team1:
#         if x.check_life() > 0:
#           x.turn(round, team2) 

#     for y in team2:
#       if y.check_life() > 0:
#         y.turn(round, team1)  

#     if winner(team1):
#         print("All Team 1 has fainted! Team 2 wins.")
#         break
#     elif winner(team2):
#         print("All Team 2 has fainted! Team 1 wins.")
#         break


class Warrior(Creature):
    def __init__(self, name, maxHP=50):
        super().__init__(name, maxHP=maxHP)
        self.abilities = {'Attack': 5, 'Defence': 10, 'Speed': 4}
        self.shield = False
    
    def shield_up(self):
        if self.shield == False:
          self.abilities['Attack'] -= 4
          self.abilities['Defence'] += 4
          self.shield = True
          print(f"{self.name} brings shield up! attack -4, defence +4")
  
    def shield_down(self):
        if self.shield == True:
          self.abilities['Attack'] += 4
          self.abilities['Defence'] -= 4
          self.shield = False
          print(f"{self.name} brings shield down! attack +4, defence -4")
    
    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        if target:
            if round_num % 4 == 0:
                self.shield_down()
                result = self.attack(target)
                print(result)
            elif round_num % 4 == 1:
                result = self.attack(target)
                print(result)
                self.shield_up()
            else:
                result = self.attack(target)
                print(result)
            target.check_life()
        else:
            print(f'{self.name} has no targets, all opponents have fainted')

# def winner(creatures):
#     return all(creature.HP <= 0 for creature in creatures)

# team1 = [Creature("Gollum")]
# team2 = [Warrior("Boromir")]

# for round in range(1, 21):
#     print(f"\nRound: {round}")
    
#     for x in team1:
#         if x.check_life() > 0:
#           x.turn(round, team2) 

#     for y in team2:
#       if y.check_life() > 0:
#         y.turn(round, team1)  

#     if winner(team1):
#         print("All Team 1 has fainted! Team 2 wins.")
#         break
#     elif winner(team2):
#         print("All Team 2 has fainted! Team 1 wins.")
#         break

class Archer(Creature):
    def __init__(self, name, maxHP=30):
        super().__init__(name, maxHP=maxHP)
        self.abilities = {'Attack': 7, 'Defence': 9, 'Speed': 8}
        self.arrowBoost = False
    
    def power_shot(self, target):
        roll1 = random.randint(1, 20)
        roll2 = random.randint(1, 20)
        roll = max(roll1, roll2)

        if self.abilities['Speed'] > target.abilities['Speed']:
            difference = self.abilities['Speed'] - target.abilities['Speed']
            roll += difference
        if self.arrowBoost == False:
          self.abilities['Attack'] += 3
          self.abilities['Defence'] -= 3
          self.arrowBoost = True
          print(f"{self.name} power shot ready! attack +3, defence -3")

        damage = random.randint(1, 8) + self.abilities['Attack']

        if target.check_life() > 0:
            if roll < target.abilities['Defence'] + target.abilities['Speed']:
                result = f'{self.name} power shot on {target.name} missed...'
            else:
                target.HP -= damage
                if target.HP < 0:
                    target.HP = 0
                result = f'{self.name} power shot on {target.name} successful! damage: {damage}. HP of {target.name}: {target.HP}.'

        return result
        
    def attack(self, target):
        if self.arrowBoost == True:
          self.abilities['Attack'] -= 3
          self.abilities['Defence'] += 3
          self.arrowBoost = False
          print(f"{self.name} power shot not ready!")
        return super().attack(target)
        
    def auto_select(self, target_list):
        alive = []
        for x in target_list:
            if x.check_life() > 0:
                alive.append(x)
        if alive:
            chosenTarget = min(alive, key=lambda x: x.HP)
            return chosenTarget
        else:
            return None
        
    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        if target:
            if round_num % 4 == 1:
                result = self.power_shot(target)
            else:
                result = self.attack(target)
            print(result)
            target.check_life()
    

    
class Fighter(Creature):
    def __init__(self, name):
        super().__init__(name, maxHP=50)
        self.abilities = {'Attack': 5, 'Defence': 8, 'Speed': 5}
    
    def auto_select(self, target_list):
        alive = []
        for x in target_list:
            if x.check_life() > 0:
                alive.append(x)
        if alive:
            chosenTarget = max(alive, key=lambda x: x.HP)
            return chosenTarget
        else:
            return None
    
    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        if target:
            result = self.attack(target)
            print(result)
            self.abilities['Attack'] -= 3
            print(f"{self.name} unleashes a flurry of strikes. He is tired: -3 attack points until next turn.")
            for attack in range(2):
                if target.check_life() > 0:
                    result = self.attack(target)
                    print(result)
                else:
                    target = self.auto_select(target_list)
                    if target:
                        result = self.attack(target)
                        print(result)
                    else:
                        break
        self.abilities['Attack'] += 3

# def winner(creatures):
#     return all(creature.HP <= 0 for creature in creatures)

# team1 = [Archer("Legolas")]
# team2 = [Fighter("Aragorn")]

# for round in range(1, 21):
#     print(f"\nRound: {round}")
    
#     for x in team1:
#         if x.check_life() > 0:
#           x.turn(round, team2) 

#     for y in team2:
#       if y.check_life() > 0:
#         y.turn(round, team1)  

#     if winner(team1):
#         print("All Team 1 has fainted! Team 2 wins.")
#         break
#     elif winner(team2):
#         print("All Team 2 has fainted! Team 1 wins.")
#         break


class OrcGeneral(Orc, Warrior):
    def __init__(self, name):
        super().__init__(name)  
        self.maxHP = 80
        self.HP = self.maxHP
        self.abilities = self.abilities

    def turn(self, round_num, target_list):
        target = self.auto_select(target_list)
        if target:
            if round_num % 4 == 1:
                result = self.attack(target)
                print(result)
                self.shield_up()
            elif round_num % 4 == 2:
                result = self.attack(target)
                print(result)
            elif round_num % 4 == 3:
                self.shield_down()
                result = self.attack(target)
                print(result)
            elif round_num % 4 == 0:
                result = self.heavy_attack(target)
                print(result)
            target.check_life()
        else:
            print(f'{self.name} has no targets, all opponents have fainted')


class GoblinKing(Goblin, Archer):
    def __init__(self, name):
        super().__init__(name)  
        self.maxHP = 50
        self.HP = self.maxHP
        self.abilities = self.abilities
    
    def turn(self, round_num, target_list):
        Archer.turn(self, round_num, target_list) 

        
# def winner(creatures):
#     return all(creature.HP <= 0 for creature in creatures)

# team1 = [OrcGeneral("generalOrc")]
# team2 = [GoblinKing("KingGoblin")]

# for round in range(1, 21):
#     print(f"\nRound: {round}")
    
#     for x in team1:
#         if x.check_life() > 0:
#           x.turn(round, team2) 

#     for y in team2:
#       if y.check_life() > 0:
#         y.turn(round, team1)  

#     if winner(team1):
#         print("All Team 1 has fainted! Team 2 wins.")
#         break
#     elif winner(team2):
#         print("All Team 2 has fainted! Team 1 wins.")
#         break


class Boss(Orc):
    def __init__(self, name):
        super().__init__(name, maxHP=200)
        self.abilities = {'Attack': 5, 'Defence': 8, 'Speed': 5}
    
    def auto_select(self, target_list, mode):
        alive = []
        for x in target_list:
            if x.check_life() > 0:
                alive.append(x)
        
        if alive:
            if mode == "Random":
                mode = random.choice(["Strong", "Weak"])
            
            if mode == "Strong":
                chosenTarget = max(alive, key=lambda x: x.HP)
                return chosenTarget
            
            elif mode == "Weak":
                chosenTarget = min(alive, key=lambda x: x.HP)
                return chosenTarget
        
        return None
        
    def turn(self, round_num, target_list):
        if round_num % 4 == 1:
            target = self.auto_select(target_list, "Weak")
            if target:
                result = self.attack(target)
                print(result)
                self.abilities['Attack'] -= 3
                print(f"{self.name} unleashes a flurry of strikes. He is tired: -3 attack points until next turn.")
                if "missed" not in result.lower():
                    for attack in range(2):
                        if target.check_life() > 0:
                            result = self.attack(target)
                            print(result)
                else:
                    for attack in range(2):
                        target = self.auto_select(target_list, "Random")
                        if target:
                            result = self.attack(target)
                            print(result)
                        else:
                            break
            self.abilities['Attack'] += 3
        else:
            target = self.auto_select(target_list, "Strong")
            if target:
                result = self.attack(target)
                print(result)
                self.abilities['Attack'] -= 3
                print(f"{self.name} unleashes a flurry of strikes. He is tired: -3 attack points until next turn.")
                for attack in range(2):
                    if target.check_life() > 0:
                        result = self.attack(target)
                        print(result)
                    else:
                        target = self.auto_select(target_list, "Strong")
                        if target:
                            result = self.attack(target)
                            print(result)
                        else:
                            break
            self.abilities['Attack'] += 3


# def winner(creatures):
#     return all(creature.HP <= 0 for creature in creatures)

# team1 = [OrcGeneral("generalOrc")]
# team2 = [Boss("Boss")]

# for round in range(1, 21):
#     print(f"\nRound: {round}")
    
#     for x in team1:
#         if x.check_life() > 0:
#           x.turn(round, team2) 

#     for y in team2:
#       if y.check_life() > 0:
#         y.turn(round, team1)  

#     if winner(team1):
#         print("All Team 1 has fainted! Team 2 wins.")
#         break
#     elif winner(team2):
#         print("All Team 2 has fainted! Team 1 wins.")
#         break


class Wizard(Creature):
        def __init__(self, name, maxHP=20):
            super().__init__(name, maxHP=maxHP)
            self.name = name
            self.maxHP = maxHP
            self.HP = maxHP
            self.abilities = {'Attack': 3, 'Defence': 5, 'Speed': 5, 'Arcana': 10}
            self.mana = 100

        def attack(self, target):
            result = super().attack(target) 
            self.mana += 20 
            if self.mana > 100:
                self.mana = 100
            print(f"{self.name} + 20 mana! Mana: {self.mana}.")
            return result
            
        
        def recharge(self):
            self.mana += 30
            if self.mana > 100:
                self.mana = 100
            print(f"{self.name} channels magical energy...")
            return f"Mana +30. Recharges mana to {self.mana}."
        
        def fire_bolt(self, target):
            roll = random.randint(1, 20) + self.abilities['Arcana']//2
            if roll < self.abilities['Defence'] + self.abilities['Speed']:
                return f'{self.name} fires a bolt on {target.name}. Missed...'
            else:
                damage = range(1, self.abilities['Arcana'])
                damage = random.choice(damage)
                if target.HP - damage < 0:
                    target.HP = 0
                else:
                    self.mana += 10
                    target.HP -= damage
                return f'{self.name} fires a bolt on {target.name}. Damage: {damage}. HP of {target.name}: {target.HP}.\nMana is: {self.mana}.'
            
        def heal(self, target):
            if self.mana < 20:
                return f'{self.name} does not have enough mana to heal.'
            else:
                self.mana -= 20
                healPoints = random.randint(0, 8)
                target.HP += healPoints
                if target.HP > target.maxHP:
                    target.HP = target.maxHP
                print("Mana -20.")
                return f'{self.name} heals {target.name} for {healPoints} HP. HP of {target.name}: {target.HP}.\nMana is: {self.mana}.'
        
        def mass_heal(self, allies):
            if self.mana < 30:
                return f'{self.name} does not have enough mana to heal all allies.'
            else:
                self.mana -= 30
                for x in allies:
                    if x.HP > 0:
                        healPoints = random.randint(0, 10) + self.abilities['Arcana']
                        x.HP += healPoints
                        if x.HP > x.maxHP:
                            x.HP = x.maxHP
                        print(f"{self.name} heals {x.name} for {healPoints} HP. HP of {x.name}: {x.HP}/{x.maxHP}.")
                return f'Mana -30. All allies healed. Mana is: {self.mana}.'

            
        def fire_storm(self, enemies):
            if self.mana < 50:
                return f'{self.name} does not have enough mana for a fire storm.'
            else:
                self.mana -= 50
                for x in enemies:
                    damage = random.randint(0, 20) + self.abilities['Speed']
                    if damage >= self.abilities['Arcana']:
                        damage = damage//2
                    else:
                        damage = random.randint(5, 20) + self.abilities['Arcana']
                    if x.HP > 0:
                        if x.HP - damage < 0:
                            x.HP = 0
                            x.check_life()
                        else:
                            x.HP -= damage
                        print(f"{self.name} fires a fire storm on {x.name}. Damage: {damage}. HP of {x.name}: {x.HP}.")
                return f'Mana -50. All enemies damaged. Mana is: {self.mana}.'



        def select_target(self, target_list):
            available_targets = []
            for x in target_list:
                if x.HP > 0:
                    available_targets.append(x)

            while True:
                for i, x in enumerate(available_targets):
                    print(f"{i+1}. {x.name}, HP: {x.HP}/{x.maxHP}")

                target = input("Select target: ")
                if target.isdigit():
                    target = int(target)
                    if 1 <= target <= len(available_targets):
                        return available_targets[target - 1]
                    else:
                        print("Please enter a valid target number.")
                else:
                    print("Invalid input. Please enter a number.")
            



# wizard = Wizard("Gandalf")

# targets = [
#     GoblinKing("KingGoblin"),
#     OrcGeneral("GeneralOrc"),
#     Creature("Gollum")
# ]

# for x in targets:
#     print('===Attack method:===\n') 
#     print(wizard.attack(x))
#     print('\n===Recharge method:===\n') 
#     print(wizard.recharge())
#     print('\n===Fire bolt method:===\n') 
#     print(wizard.fire_bolt(x))
#     print('\n===Heal method:===\n') 
#     print(wizard.heal(x))
#     print('\n===Mass heal method:===\n') 
#     print(wizard.mass_heal(targets))
#     print('\n===Recharge method:===\n') 
#     print(wizard.recharge())
#     print('\n===Fire storm method:===\n') 
#     print(wizard.fire_storm(targets))




class Battle:
    def __init__(self):
        self.enemies = [GoblinKing('KingGoblin'), OrcGeneral('GeneralOrc'), Goblin('Goblin'), Orc('Orc')]
        self.allies = [Fighter('Fighter'), Archer('Legolas'), Warrior('Frodo'), Creature('Gollum')]
        self.boss = Boss('Boss')
        self.player = Wizard('Eneko')

    def start(self):
        orderList = self.enemies + self.allies 
        orderList.append(self.player)
        self.allies.append(self.player)
        orderList.sort(key=lambda x: x.abilities['Speed'], reverse=True)
        print()
        print('Battle is about to begin. All combatants:')
        for x in orderList:
            time.sleep(0.2)
            print()
            print(f"{x.name}, HP: {x.HP}/{x.maxHP}. Abilities: {x.abilities}")  
        print()
        print('THE BATTLE BEGINS')
        print("=======================================================")
        round = 1
        while any(character.HP > 0 for character in self.enemies) and any(character.HP > 0 for character in self.allies) and self.player.HP > 0:
            print(f"\nRound: {round}")
            for x in orderList:
                time.sleep(1)
                if x.check_life() > 0:
                    print("=======================================================")
                    if x in self.enemies:
                        x.turn(round, self.allies)
                    elif x in self.allies and x != self.player:
                        x.turn(round, self.enemies)
                    elif x == self.player:
                        self.player_turn()
                    elif x == self.boss: 
                        x.turn(round, self.allies)
            
            if all(enemy.HP <= 0 for enemy in self.enemies):
                print('Allies win!')
                break
            elif all(ally.HP <= 0 for ally in self.allies):
                print('Enemies win!')
                break
            elif self.player.HP <= 0:
                print('You died!')
                break
                
            
            print("=======================================================")
            print(f'End of of round: {round}')
            print("=======================================================")
            round += 1
            enemiesCount = 0
            for enemy in self.enemies:
                if enemy.HP > 0:
                    enemiesCount += 1
            if enemiesCount == 1 and self.boss not in self.enemies:
                print('Only one enemy is remaining')
                print("!!BOSS INCOMING!!")
                orderList.append(self.boss)
                self.enemies.append(self.boss)

    def player_turn(self):
        while True:
            print(f"Player: {self.player.name}. HP: {self.player.HP}/{self.player.maxHP}. Mana: {self.player.mana}/100")
            print("Allies:\n")
            for x in self.allies:
                if x.check_life() > 0:
                    print(f"{x.name} HP: {x.HP}/{x.maxHP}")
            print("=======================================================")
            player_choice = input("Actions. F: Attack(Select enemy) R: Recharge Mana: \nSpells. 1: Heal(Select ally) 2: Firebolt(Select enemy) 3: Mass Heal(all allies) 4: Fire Storm(all enemies)\nTo Quit game type: Quit: \n")
            print("=======================================================")

            if player_choice == "F":
                target = self.player.select_target(self.enemies)
                if target:
                    print(self.player.attack(target))
                    break
                else:
                    print("No target selected.")
            elif player_choice == "R":
                print(self.player.recharge())
                break
            elif player_choice == "1":
                target = self.player.select_target(self.allies)
                if target:
                    print(self.player.heal(target))
                    break
                else:
                    print("No target selected.")
            elif player_choice == "2":
                target = self.player.select_target(self.enemies)
                if target:
                    print(self.player.fire_bolt(target))
                    break
                else:
                    print("No target selected.")
            elif player_choice == "3":
                print(self.player.mass_heal(self.allies))
                break
            elif player_choice == "4":
                print(self.player.fire_storm(self.enemies))
                break
            elif player_choice == "Quit":
                print("You quit the game.")
                quit()
            else:
                print("Invalid input. Please enter a valid action.")
                continue
            


battle = Battle()
battle.start()
