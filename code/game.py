#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from code.menu import Menu

W_WIDTH = 1240
W_HEIGHT = 720

class Game:
    def __init__(self):
        pygame.init()
        self.window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.Run()
            pass



        # running = True
        # while running:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:  
        #             running = False
        # pygame.quit()


