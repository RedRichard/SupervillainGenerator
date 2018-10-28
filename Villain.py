import random

class Villain:
    def __init__(self, values = []):
        self.abilities = values

    def generate_abilities(self):
        self.abilities = random.choices(range(0,6), k=10)

    def get_abilities(self):
        return self.abilities
    
    def add_ability(self, val):
        self.abilities.append(val)


# vil = Villain()
# vil.generate_abilities()
# print(vil.abilities) 