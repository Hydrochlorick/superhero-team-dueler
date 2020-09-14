from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team
import random

class Arena:
    def __init__(self):
        self.team_one = Team("One")
        self.team_two = Team("Two")

    def create_ability(self):
        name = input("What is the ability name? ")
        max_damage = int(input("What is the max damage of the ability? "))

        return Ability(name, max_damage)

    def create_weapon(self):
        name = input("What is the name of the weapon? ")
        max_damage = int(input("What is this weapon's max damage? "))

        return Weapon(name, max_damage)

    def create_armor(self):
        name = input("What piece of armor are you making? ")
        max_block = int(input("What is it's maximum block rating? "))

        return Armor(name, max_block)

    def create_hero(self):
        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None
        while add_item != "4":
           add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
           if add_item == "1":
               ability = self.create_ability()
               hero.add_ability(ability)
           elif add_item == "2":
               weapon = self.create_weapon()
               hero.add_weapon(weapon)
           elif add_item == "3":
               armor = self.create_armor()
               hero.add_armor(armor)
        return hero

    def build_team_one(self):
        numOfTeamMembers = int(input("How many members would you like on Team One?\n"))
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_one.add_hero(hero)

    def build_team_two(self):
        numOfTeamMembers = int(input("How many members would you like on Team Two?\n"))
        for _ in range(numOfTeamMembers):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        self.team_one.attack(self.team_two)

    def show_stats(self):
        print("\n")
        print(self.team_one.name + " statistics: ")
        self.team_one.stats()
        print("\n")
        print(self.team_two.name + " statistics: ")
        self.team_two.stats()
        print("\n")

        team1_kills = 0
        team1_deaths = 0
        for hero in self.team_one.heroes:
            team1_kills += hero.kills
            team1_deaths += hero.deaths
        if team1_deaths == 0:
            team1_deaths = 1
        print(self.team_one.name + " average K/D was: " + str(team1_kills/team1_deaths))

        team2_kills = 0
        team2_deaths = 0
        for hero in self.team_two.heroes:
            team2_kills += hero.kills
            team2_deaths += hero.deaths
        if team2_deaths == 0:
            team2_deaths = 1
        print(self.team_two.name + " average K/D was: " + str(team2_kills/team2_deaths))

        for hero in self.team_one.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_one.name + ": " + hero.name)

        for hero in self.team_two.heroes:
            if hero.deaths == 0:
                print("survived from " + self.team_two.name + ": " + hero.name)

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
