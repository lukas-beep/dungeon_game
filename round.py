#TODO: this will manage actual fight
import pygame
# from main import update_health
from sympy import symbols, Eq, solve
class Round:
    def __init__(self, player,enemies, screen):
        self.enemies = enemies
        self.player = player
        self.screen = screen

    def start_round(self):
        while True:
            self.player_turn()
            self.update_health_bars()
            input()
            self.enemy_turn()
            self.update_health_bars()
            input()

            print("Player health:", self.player.hero.health, "Enemy health:", self.enemies[-1].health)

            alive = self.check_alive()
            if alive[0] == False:
                print("You lost!")
                return False
            elif alive[1] == False:
                return True
        

    def check_alive(self):
        for enemy in self.enemies:
            if enemy.is_alive() == False:
                self.enemies.remove(enemy)

        return (bool(self.player.hero.is_alive()) , bool(self.enemies))
            
    def player_turn(self):
        card = self.choose_card()
        self.player.hero.attack_enemy(self.enemies[-1], card[1])

    def enemy_turn(self):
        for enemy in self.enemies:
            enemy.attack_hero(self.player.hero)

    def choose_card(self):
        #TODO: implement this
        # return information (name, damage, cost) about the card
        return ("card", 7,0)

    def update_health_bars(self):
        pygame.draw.rect(self.screen, (255,0,0), (440, 175 - 20, 50, 10)) # HP bar

        pygame.draw.rect(self.screen, (0,128,0), (440, 175 - 20, 50 - (50//self.enemies[-1].full_health)*(self.enemies[-1].full_health-self.enemies[-1].health) , 10)) # 100 means health

        pygame.draw.rect(self.screen, (255,0,0), (50, 175 - 20, 50, 10)) # HP bar
        pygame.draw.rect(self.screen, (0,128,0), (50, 175 - 20, 50 - (50//self.player.hero.full_health)*(self.player.hero.full_health-self.player.hero.health), 10)) # 100 means health
        pygame.display.update()
