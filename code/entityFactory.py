#!/usr/bin/python
# -*- coding: utf-8 -*-

import random
from code.Const import W_HEIGHT, W_WIDTH
from code.background import Background
from code.enemy import Enemy
from code.player import Player


class EntityFactory:
    @staticmethod
    def get_entity(entity_name : str, position=(0,0)):
        match entity_name:
            case 'level1Bg' :
                list_bg = []
                for i in range(6):
                    if i in [2, 3, 4, 5]:
                        x_position = random.randint(-W_WIDTH, W_WIDTH) 
                        y_position = random.randint(50, W_HEIGHT - 50)
                    else : 
                        x_position = 0
                        y_position = 0
                    list_bg.append(Background(f'level1Bg{i}', (x_position, y_position)))
                    list_bg.append(Background(f'level1Bg{i}', (W_WIDTH + x_position, y_position)))
                return list_bg
            case 'PlayerShip' :
                return Player('PlayerShip', position=(15, W_HEIGHT // 2))
            case 'EnemyFast' :
                return Enemy('EnemyFast', position=(W_WIDTH + 50, random.randint(100, W_HEIGHT - 100)))
            case 'EnemyFat' :
                return Enemy('EnemyFat', position=(W_WIDTH + 50, random.randint(110, W_HEIGHT - 110)))