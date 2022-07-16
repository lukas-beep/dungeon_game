#TODO: card has name, powerup, level, cost, and description

class Card:
    def __init__(self, name, powerup, level, cost, description):
        self.name = name
        self.powerup = powerup
        self.level = level
        self.cost = cost
        self.description = description
        self.hoverd = False
        self.rect = None

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

    def set_rect(self, rect):
        self.rect = rect

    def get_rect(self):
        return self.rect