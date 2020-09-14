import random

class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()

    def remove_hero(self, name):
        foundHero = False
        for hero in self.heroes:
            if hero.name == name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0

    def view_all_heroes(self):
        for h in self.heroes:
            print(h.name)

    def add_hero(self, hero):
        self.heroes.append(hero)

    def stats(self):
        for hero in self.heroes:
            if hero.deaths == 0:
                hero.deaths += 1
            kd = hero.kills / hero.deaths
            print("{} Kills/Deaths:{}".format(hero.name,kd))

    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0:
            hiro = random.choice(living_heroes)
            anti_hiro = random.choice(living_opponents)
            hiro.fight(anti_hiro)
            if hiro.is_alive() == False:
                living_heroes.remove(hiro)
            if anti_hiro.is_alive() == False:
                living_opponents.remove(anti_hiro)