from ability import Ability
import random

class Weapon(Ability):
    def attack(self):
        halfie = self.max_damage // 2
        return random.randint(halfie, self.max_damage)