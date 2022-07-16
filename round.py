#TODO: this will manage actual fight
import pygame
import random
class Round:
    def __init__(self, player,enemies, screen):
        pygame.init()
        default_font = pygame.font.get_default_font()
        self.renderfont = pygame.font.Font(default_font, 20)
        self.enemies = enemies
        self.player = player
        self.screen = screen

    def start_round(self):
        self.update_health_bars()
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
        redraw = True
        while True:
            if redraw:
                self.update_hand_cards()
                redraw = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                pos = pygame.mouse.get_pos()
                for card in self.player.hero.hand:
                    h = card.hoverd
                    card.hoverd = card.rect.collidepoint(pos)
                    if not card.hoverd == h:
                        redraw = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for card in self.player.hero.hand:
                        if card.rect.collidepoint(pygame.mouse.get_pos()):
                            return (card.get_name(), card.get_damage(), card.get_cost())
                    else:
                        print("Wrong card")

    def update_health_bars(self):
        pygame.draw.rect(self.screen, (255,0,0), (440, 175 - 20, 50, 10)) # HP bar

        pygame.draw.rect(self.screen, (0,128,0), (440, 175 - 20, (50/self.enemies[-1].full_health)*self.enemies[-1].health , 10))

        pygame.draw.rect(self.screen, (255,0,0), (50, 175 - 20, 50, 10)) # HP bar
        pygame.draw.rect(self.screen, (0,128,0), (50, 175 - 20,(50/self.player.hero.full_health)*self.player.hero.health, 10))
        pygame.display.update()

    def update_hand_cards(self): 
        pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(0,480-150,640,200))
        for i,card in enumerate(self.player.hero.hand):  
            if card.hoverd:
                up = 10
            else:
                up =0
            card.set_rect(pygame.Rect(125 + (100*i+i),480-125-up,100,120))
            #TODO images for cards
            pygame.draw.rect(self.screen, (0,255,0), card.get_rect())
            label_name = self.renderfont.render(card.get_name(), True, (0,0,0))
            self.screen.blit(label_name, (125+ (100*i+i),480-125-up))
            label_damage = self.renderfont.render(str(card.get_damage()), True, (50,100,125))
            self.screen.blit(label_damage, (125+ (100*i+i),480-125-up+30))
            pygame.display.update()
