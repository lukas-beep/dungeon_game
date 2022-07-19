#TODO:this will manage random generated stats for enemies and rounds
from round import Round
from enemy import Enemy
import random

class Dungeon:
    def __init__(self, name, player, rounds, difficulty, screen):
        self.name = name
        self.enemies = []
        self.rounds = rounds
        self.player = player
        self.difficulty = difficulty
        self.round_number = 0
        self.round = None
        self.screen = screen
        self.generate_enemies()

    def generate_enemies(self):
        #TODO: implement dificulty
        for _ in range(self.rounds):
            self.enemies.append([Enemy(damage=10,health=20,armor=5),Enemy(damage=10,health=20,armor=5)])

        print(self.enemies)

    def set_round(self):
        self.round = Round(self.player, self.enemies[self.round_number], self.screen)
        self.round_number += 1

    def play_round(self):
        while True:
            self.set_round()
            end_round = self.round.start_round()
            if end_round == False:
                return False
            elif end_round == True:
                if self.round_number >= self.rounds:
                    print("You won!")
                    return True
