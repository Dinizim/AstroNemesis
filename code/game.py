#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from code.Const import MENU_OPTION, W_HEIGHT, W_WIDTH
from code.level import Level
from code.menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window: Surface = pygame.display.set_mode(size=(W_WIDTH, W_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            return_menu = menu.run()
            
            if return_menu in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                level = Level(self.window, "level1", return_menu)
                level_return = level.run()
            elif return_menu == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass



