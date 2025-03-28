#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
import pygame
from code.Const import ENTITY_SPEED, W_HEIGHT, W_WIDTH
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        if name in ['level1Bg0', 'level1Bg1']:
            self.surf = pygame.transform.scale(self.surf, (W_WIDTH, W_HEIGHT))

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]
        if self.rect.right <= -W_WIDTH / 2:
            self.rect.left += W_WIDTH * 2
            if self.name in ['level1Bg2', 'level1Bg3', 'level1Bg4', 'level1Bg5']:  # Apenas planetas e asteroides
                self.rect.y = random.randint(100, W_HEIGHT - self.rect.height)  # Aleatoriza a posição vertical