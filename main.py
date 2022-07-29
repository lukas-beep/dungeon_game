from player import Player
import threading
from menu import Menu

import pygame
pygame.init()

WIDTH, HEIGHT = 640, 480
renderfont = pygame.font.Font("8514oem.fon", 20)
bg = pygame.image.load("assets\\caves\\cave1.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.blit(bg, (0, 0))

m = Menu(screen)
m.chosse_button()
player = Player("John",screen,renderfont)

screen.fill((0,0,0))

player.play_dungeon()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()
    
    
