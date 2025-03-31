#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.Const import ENTITY_SPEED
from code.entity import Entity
from code.playerShot import PlayerShoot


class Player(Entity):
    def __init__(self, name : str, position: tuple):
        super().__init__(name, position)
        self.shot_cooldown = 40

        pass

    def update(self, ):
        pass

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < 324:
            self.rect.centery += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < 567:
            self.rect.centerx += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        pass

    def shoot(self,):
        self.shot_cooldown -= 10
        if self.shot_cooldown == 0:
            self.shot_cooldown = 40
            pressed_key = pygame.key.get_pressed()
            if pressed_key[pygame.K_SPACE]:
                return PlayerShoot(name=f'{self.name}Shot',position=(self.rect.centerx + 20, self.rect.centery))
            else :
                return None
