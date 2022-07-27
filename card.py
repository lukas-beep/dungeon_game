
class Card:
    def __init__(self, name, powerup, level, cost, description):
        self.name = name
        self.powerup = powerup
        self.level = level
        self.cost = cost
        self.description = description
        self.hoverd = False
        self.draging = False
        self.rect = None

    def get_name(self):
        return self.name
    
    def get_powerup(self):
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

class MeeleCard(Card):
    def __init__(self, name, powerup, level, cost, description):
        super().__init__(name, powerup, level, cost, description)
        self.type = "Meele"

    def do_powerup(self, enemy):
        enemy.take_damage(self.powerup)

class RangeCard(Card):
    def __init__(self, name, powerup, level, cost, description):
        super().__init__(name, powerup, level, cost, description)
        self.type = "Range"

    def do_powerup(self, enemy):
        enemy.take_damage(self.powerup)
        