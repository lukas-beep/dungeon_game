import pygame
import random

class Round:
    def __init__(self, player,enemies, screen):
        pygame.init()
        self.renderfont = pygame.font.Font("8514oem.fon", 20)
        self.enemies = enemies
        self.player = player
        self.screen = screen
        self.clock = pygame.time.Clock()

    def start_round(self):
        self.set_rect_enemies()
        self.update_health_bars()
        while True:
            self.player_turn()
            self.update_health_bars()
            self.enemy_turn()
            self.update_health_bars()

            alive = self.check_alive()
            if alive[0] == False:
                return False
            elif alive[1] == False:
                return True
        

    def check_alive(self):
        for enemy in self.enemies:
            if enemy.is_alive() == False:
                self.enemies.remove(enemy)

        return (bool(self.player.hero.is_alive()) , bool(self.enemies))
            
    def player_turn(self):
        card, enemy = self.choose_card()
        card.do_powerup(enemy)

    def enemy_turn(self):
        for enemy in self.enemies:
            enemy.attack_hero(self.player.hero)

    def choose_card(self):
        self.update_screen()
        pygame.image.save(self.screen,"screenshot.jpg")
        # return information ((name, damage, cost),enemy) about the card
        redraw = False
        re_health = True
        re_enemies = True
        re_cards = True
        while True:
            if redraw:
                self.update_screen(re_cards, re_enemies, re_health)
                redraw = False
                re_health = True
                re_enemies = True
                re_cards = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                pos = pygame.mouse.get_pos()
                for card in self.player.hero.hand:
                    h = card.hoverd
                    card.hoverd = card.rect.collidepoint(pos)
                    if not( card.hoverd == h) and not card.hoverd and not card.draging:
                        redraw = True
                        re_enemies = False
                        re_health = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for card in self.player.hero.hand:

                        if event.button == 1:            
                            if card.rect.collidepoint(event.pos):
                                card.draging = True
                                draging_card = card
                                mouse_x, mouse_y = event.pos
                                offset_x = card.rect.x - mouse_x
                                offset_y = card.rect.y - mouse_y

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:      
                        for card in self.player.hero.hand:     
                            card.draging = False


                        self.update_screen()

                    for i,enemy in enumerate(self.enemies[::-1]):
                        if enemy.rect.collidepoint(pos):
                            for card in self.player.hero.hand:
                                if card == draging_card:
                                    if card.type == "Meele":
                                        if i == 0:
                                            return (card, enemy) 
                                    elif card.type == "Range":
                                        return (card, enemy)
                                    self.set_default_rect_cards()

                elif event.type == pygame.MOUSEMOTION:
                    for card in self.player.hero.hand:
                        if card.draging:
                            mouse_x, mouse_y = event.pos
                            card.rect.x = mouse_x + offset_x
                            card.rect.y = mouse_y + offset_y

                            self.update_draging_card(draging_card)
                            
            self.clock.tick(60)


    def update_health_bars(self):
        for enemy in self.enemies:  
            pygame.draw.rect(self.screen, (255,0,0), (enemy.rect.x, 175 - 20, 50, 10)) # HP bar
            pygame.draw.rect(self.screen, (0,128,0), (enemy.rect.x, 175 - 20, (50/enemy.full_health)*enemy.health , 10))

        pygame.draw.rect(self.screen, (255,0,0), (50, 175 - 20, 50, 10)) # HP bar
        pygame.draw.rect(self.screen, (0,128,0), (50, 175 - 20,(50/self.player.hero.full_health)*self.player.hero.health, 10))
        pygame.display.update()

    def set_default_rect_cards(self, card_=None):
        for i,card in enumerate(self.player.hero.hand):  
            if card_ != card:
                card.set_rect(pygame.Rect(125 + (100*i+i),480-125,100,120))

    def set_rect_enemies(self):
        for i,enemy in enumerate(self.enemies):
            enemy.set_rect(pygame.Rect(640 -70- (100*i+i),175,50,100))

    def update_hand_cards(self):
        card_not_set = None
        for card in self.player.hero.hand:
            if card.draging:
                card_not_set = card
        self.set_default_rect_cards(card_not_set)
        pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(0,480-150,640,200))
        for card in self.player.hero.hand:  
            if card.hoverd: card.rect.y -= 10
            #TODO images for cards
            self.update_hand_card(card)

    def update_hand_card(self, card):

        #TODO image for card
        rect = card.get_rect()
        pygame.draw.rect(self.screen, (0,255,0), rect)
        label_name = self.renderfont.render(card.get_name(), True, (0,0,0))
        self.screen.blit(label_name, (rect.x + 10, rect.y + 10))
        label_damage = self.renderfont.render(str(card.get_powerup()), True, (50,100,125))
        self.screen.blit(label_damage, (rect.x + 10, rect.y + 10+30))
        pygame.display.update()

    def update_draging_card(self, card):
        rect = card.get_rect()
        screenshot = pygame.image.load("screenshot.jpg").convert()
        rect = screenshot.get_rect()
        self.screen.blit(screenshot, rect)
        self.update_hand_card(card)
        
    def update_enemies(self):
        self.set_rect_enemies()
        for enemy in self.enemies:
            pygame.draw.rect(self.screen, (255,140,25), enemy.get_rect())
            #TODO damage label
            # label_damage = self.renderfont.render(str(enemy.get_damage()), True, (50,100,125))
            # self.screen.blit(label_damage, (enemy.get_rect().x,enemy.get_rect().y-30+30))
            pygame.display.update()

    def update_screen(self, cards=True, enemies=True, health=True):
        if enemies:
            self.screen.fill((128,64,0))
            pygame.draw.rect(self.screen, (255,0,0), pygame.Rect(0,480-150,640,200))
            pygame.draw.rect(self.screen, (0,0,0), pygame.Rect(50,175,50,100)) #player
            self.update_enemies()
        if health: self.update_health_bars()
        if cards: self.update_hand_cards()
        pygame.display.update()
        