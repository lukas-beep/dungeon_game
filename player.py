from hero import Hero
from dungeon import Dungeon

class Player:
    def __init__(self, name, screen, renderfont):
        self.name = name
        self.hero = Hero()
        self.screen = screen
        self.renderfont = renderfont

    def play_dungeon(self):
        dungeon = Dungeon("lol", self, 1, 1, self.screen, self.renderfont)
        dungeon.play_round()