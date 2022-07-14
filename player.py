from hero import Hero
from dungeon import Dungeon

class Player:
    def __init__(self, name, screen):
        self.name = name
        self.hero = Hero()
        self.screen = screen

    def play_dungeon(self):
        dungeon = Dungeon("lol", self, 1, 1, self.screen)
        dungeon.play_round()