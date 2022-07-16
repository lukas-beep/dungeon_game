#TODO: this will manage actual fight
import pygame
import random
class Round:
    def __init__(self, player,enemies, screen):
        pygame.init()
        default_font = pygame.font.get_default_font()
        self.renderfont = pygame.font.Font(default_font, 30)
        self.enemies = enemies
        self.player = player
        self.screen = screen

    def start_round(self):
        while True:
            self.player_turn()
            self.update_health_bars()
            self.enemy_turn()
            self.update_health_bars()

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
        self.update_hand_cards()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.hand_cards_[0].collidepoint(pygame.mouse.get_pos()):
                        return (self.player.hero.hand[0].get_name(), self.player.hero.hand[0].get_damage(), self.player.hero.hand[0].get_cost())
                    # elif self.hand_cards_[1].collidepoint(pygame.mouse.get_pos()):
                    #     return ("Sword", 10, 1)
                    # elif self.hand_cards_[2].collidepoint(pygame.mouse.get_pos()):
                    #     return ("Sword", 10, 1)
                    # elif self.hand_cards_[3].collidepoint(pygame.mouse.get_pos()):
                    #     return ("Sword", 10, 1)
                    else:
                        print("Wrong card")

    def update_health_bars(self):
        pygame.draw.rect(self.screen, (255,0,0), (440, 175 - 20, 50, 10)) # HP bar

        pygame.draw.rect(self.screen, (0,128,0), (440, 175 - 20, (50/self.enemies[-1].full_health)*self.enemies[-1].health , 10))

        pygame.draw.rect(self.screen, (255,0,0), (50, 175 - 20, 50, 10)) # HP bar
        pygame.draw.rect(self.screen, (0,128,0), (50, 175 - 20,(50/self.player.hero.full_health)*self.player.hero.health, 10))
        pygame.display.update()

    def update_hand_cards(self):  
        self.hand_cards_ = []  
        for card in self.player.hero.hand:
            self.hand_cards_.append(pygame.Rect(150,480-125,100,120))
            #TODO images for cards
            pygame.draw.rect(self.screen, (0,255,0), self.hand_cards_[-1])
            label = self.renderfont.render(card.get_name(), True, (0,0,0))
            self.screen.blit(label, (150,480-125))
            pygame.display.update()
