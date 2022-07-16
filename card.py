#TODO: card has name, powerup, level, cost, and description

class Card:
    def __init__(self, name, powerup, level, cost, description):
        self.name = name
        self.powerup = powerup
        self.level = level
        self.cost = cost
        self.description = description

    def get_name(self):
        return self.name
    
    def get_damage(self):
        return self.powerup

    def get_level(self):
        return self.level

    def get_cost(self):
        return self.cost

    def get_description(self):
        return self.description