from player import Player
import threading
from menu import Menu

import pygame
pygame.init()

WIDTH, HEIGHT = 640, 480
renderfont = pygame.font.Font("8514oem.fon", 20)
pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

m = Menu(screen)
m.chosse_button()
player = Player("John",screen,renderfont)

screen.fill((128,64,0))
pygame.draw.rect(screen, (255,0,0), pygame.Rect(0,480-150,640,200))


player.play_dungeon()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.flip()
    
    
