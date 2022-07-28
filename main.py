from player import Player
import threading
from menu import Menu



import pygame
pygame.init()

WIDTH, HEIGHT = 640, 480

pygame.display.set_caption("My Game")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

m = Menu(screen)
m.chosse_button()
player = Player("John",screen)
# thread = threading.Thread(target=player.play_dungeon)
# thread.start()



screen.fill((128,64,0))
pygame.draw.rect(screen, (255,0,0), pygame.Rect(0,480-150,640,200))


player.play_dungeon()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    
    
