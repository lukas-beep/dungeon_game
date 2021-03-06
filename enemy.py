class Enemy:
    def __init__(self, img,name="enemy" , damage=0, health=0, armor=0):
        self.name = name
        self.damage = damage
        self.full_health = health
        self.health = health
        self.armor = armor
        self.img = img
        self.alive = True
        self.rect = None

    def take_damage(self, damage):
        if damage > self.armor:
            self.health -= damage - self.armor
            self.armor = 0
            if self.health <= 0:
                self.alive = False
        else:
            self.armor -= damage

    def get_rect(self):
        return self.rect

    def get_img(self):
        return self.img

    def set_rect(self, rect):
        self.rect = rect

    def get_damage(self):
        return self.damage

    def get_health(self):
        return self.health

    def get_full_health(self):
        return self.full_health
    
    def get_armor(self):
        return self.armor

    def is_alive(self):
        return self.alive

    def attack_hero(self, hero):
        hero.take_damage(self.damage)

    def __str__(self):
        return "Name: {}, Lives: {}, Hit Points: {}".format(self.name, self.lives, self.hit_points)
