
from round import Round
from enemy import Enemy
import random
import pygame

class Dungeon:
    def __init__(self, name, player, rounds, difficulty, screen, renderfont):
        pygame.init()
        self.name = name
        self.enemies = []
        self.rounds = rounds
        self.player = player
        self.difficulty = difficulty
        self.round_number = 0
        self.round = None
        self.screen = screen
        self.renderfont = renderfont
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
        x,y = self.screen.get_size()
        while True:
            self.set_round()
            end_round = self.round.start_round()
            if end_round == False:
                print("You lost!")
                status = self.renderfont.render("YOU LOST!", True, (0,0,0))
                self.screen.blit(status, (x//2, y//2))
                return False
            elif end_round == True:
                if self.round_number >= self.rounds:
                    print("You won!")
                    status = self.renderfont.render("YOU WON!", True, (0,0,0))
                    self.screen.blit(status, (x//2, y//2))
                    return True
