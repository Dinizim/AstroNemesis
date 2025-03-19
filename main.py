import pygame
from pygame import Surface, Rect

W_WIDTH = 1240
W_HEIGHT = 720

pygame.init()

window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            running = False

pygame.quit()