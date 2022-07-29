
from round import Round
from enemy import Enemy
from random import randint
import pygame

class Dungeon:
    def __init__(self, name, player, rounds, difficulty, screen, renderfont):
        pygame.init()
        self.name = name
        self.enemies = []
        self.rounds = rounds
        self.player = player
        self.difficulty = difficulty
        self.round_number = 1
        self.round = None
        self.screen = screen
        self.renderfont = renderfont
        self.cave_image = pygame.transform.scale(pygame.image.load("assets\\caves\\cave1.png").convert(), self.screen.get_size()) #TODO: change on dificulty 1-4
        self.generate_enemies()

    def generate_enemies(self):
        #TODO: implement dificulty
        for _ in range(self.rounds):
            img = pygame.transform.flip(pygame.transform.scale(pygame.image.load("assets\\skeletons\\Skeleton.png").convert_alpha(), (100,100)), True, False)
            self.enemies.append([Enemy(img,damage=randint(5,10),health=randint(15,30),armor=randint(1,5)),Enemy(img,damage=randint(5,10),health=randint(15,25),armor=randint(1,5))])

        print(self.enemies)

    def set_round(self):
        self.round = Round(self.player, self.enemies[self.round_number], self.screen, self.cave_image, self.round_number, self.rounds)
        self.round_number += 1

    def play_round(self):
        x,y = self.screen.get_size()
        while True:
            self.player.hero.reset_health()
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
