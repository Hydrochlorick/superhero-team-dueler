import random
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          abilities: List
          armors: List
          name: String
          starting_health: Integer
          current_health: Integer
        '''
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
        self.kills = 0
        self.deaths = 0

    def add_ability(self, ability):
        self.abilities.append(ability)

    def add_armor(self, armor):
        self.armors.append(armor)

    def add_weapon(self, weapon):
        self.abilities.append(weapon)

    def add_kill(self, num_kills):
        self.kills += num_kills

    def add_death(self, num_deaths):
        self.deaths += num_deaths

    def attack(self):
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def defend(self, damage_amt):
        damage = 0
        if len(self.armors) == 0:
            return damage_amt
        for armor in self.armors:
            damage = damage_amt - armor.block()
        return damage

    def take_damage(self, damage):
        self.current_health -= self.defend(damage)

    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True
    
    def fight(self, opponent):
        if len(self.abilities) == 0 and opponent.abilities == 0:
            print("It's a draw!")
            return
        fight_over = False
        while fight_over == False:
            self.take_damage(self.defend(opponent.attack()))
            opponent.take_damage(opponent.defend(self.attack()))
            if self.is_alive() == False or opponent.is_alive() == False:
                fight_over = True
        if self.current_health >= opponent.current_health:
            print(f"{self.name} is the winner!")
            self.add_kill(1)
            opponent.add_death(1)
        else:
            print(f"{opponent.name} is the winner!")
            self.add_death(1)
            opponent.add_kill(1)

if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())