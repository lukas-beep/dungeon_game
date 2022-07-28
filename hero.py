from card import MeeleCard, RangeCard

class Hero:
    def __init__(self):
        self.health = 100
        self.full_health = 100
        self.mana = 100
        self.attack = 10
        self.armor = 0
        self.intelligence = 10
        self.luck = 10
        self.exp = 0
        self.gold = 0
        self.upgrade_points = 0
        self.alive = True
        self.hand = [MeeleCard("Sword", 10, 1, 0, "A sword that can be used to attack"),MeeleCard("Knife", 8, 1, 0, "A knife that can be used to attack"),RangeCard("Bow", 10, 1, 0, "A bow that can be used to attack"),RangeCard("Crossbow", 10, 1, 0, "A crossbow that can be used to attack")]
        self.cards = []

    # def level_up(self, upgrade):
    #     if upgrade == "health":
    #         self.health += 10
    #     elif upgrade == "mana":
    #         self.mana += 10
    #     elif upgrade == "attack":
    #         self.attack += 1
    #     elif upgrade == "luck":
    #         self.intelligence += 1
    #         self.luck += 1
        
    #     self.upgrade_points -= 1

    def get_upgrade_points(self):
        return self.upgrade_points

    def get_level(self):
        return self.level

    def get_health(self):
        return self.health

    def get_full_health(self):
        return self.full_health

    def get_mana(self): 
        return self.mana

    def get_attack(self):
        return self.attack

    def get_armor(self):
        return self.armor

    def get_speed(self):
        return self.speed

    def get_intelligence(self):     
        return self.intelligence

    def get_luck(self):    
        return self.luck

    def get_exp(self):
        return self.exp

    def get_gold(self):
        return self.gold

    def add_upgrade_points(self, points):
        self.upgrade_points += points

    def add_exp(self, exp):
        self.exp += exp

    def add_gold(self, gold):
        self.gold += gold   

    def take_damage(self, damage):
        if damage > self.armor:
            self.health -= damage - self.armor
            if self.health <= 0:
                self.alive = False
        else:
            self.armor -= damage

    def take_mana(self, mana):
        self.mana -= mana

    def attack_enemy(self, enemy, card):
        enemy.take_damage(card.get_damage())

    def cast_spell(self, spell):
        pass

    def is_alive(self):
        return self.alive




