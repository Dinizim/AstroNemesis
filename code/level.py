#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.entity import Entity

import pygame

from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, menu_list):
        self.window = window
        self.name = name
        self.menu_list = menu_list
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.flip()
