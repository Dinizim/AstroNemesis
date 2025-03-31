#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from code.enemyShot import EnemyShoot
from code.entity import Entity
from code.Const import ENTITY_SPEED, W_WIDTH


class Enemy(Entity):
    def __init__(self, name : str, position: tuple):
        super().__init__(name, position)
        self.shot_cooldown = 20

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self,):
        self.shot_cooldown -= 1
        if self.shot_cooldown == 0:
            self.shot_cooldown = random.randint(20, 30)
            if random.randint(0, 100) < 20:
                return EnemyShoot(name=f'{self.name}Shot', position=(self.rect.centerx - 20, self.rect.centery))
            else :
                return None