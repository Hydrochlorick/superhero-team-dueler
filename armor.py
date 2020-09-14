import random

class Armor:
    def __init__(self, name, max_block):
        '''Instantiate instance properties. name: String; max_block: Integer'''
        self.name = name
        self.max_block = max_block

    def block(self):
        blocking_powah = random.randint(0, self.max_block)
        return blocking_powah

if __name__ == "__main__":
    armor = Armor("Debugging Shield", 10)
    print(armor.name)
    print(armor.block())