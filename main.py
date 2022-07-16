from player import Player
import threading


import pygame
pygame.init()

pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((640, 480))

player = Player("John",screen)
# thread = threading.Thread(target=player.play_dungeon)
# thread.start()



screen.fill((128,64,0))
pygame.draw.rect(screen, (255,0,0), pygame.Rect(0,480-150,640,200))
pygame.draw.rect(screen, (0,0,0), pygame.Rect(50,175,50,100))
pygame.draw.rect(screen, (0,0,0), pygame.Rect(640-200,175,50,100))


player.play_dungeon()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    
    
