#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from tkinter.font import Font
from code.entityMediator import EntityMediator
from code.Const import C_WHITE, EVENT_ENEMYFAST, W_HEIGHT
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
        self.entity_list.append(EntityFactory.get_entity('PlayerShip'))
        self.timeout = 20000
        self.speedEnemyfast = 4000
        pygame.time.set_timer(EVENT_ENEMYFAST,self.speedEnemyfast)

    def run(self):
        pygame.mixer_music.load('./layered/EpicEnd.ogg')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == EVENT_ENEMYFAST:
                 choice = random.choice(('EnemyFast', 'EnemyFat'))
                 self.entity_list.append(EntityFactory.get_entity(choice))

                 #TODO: Refatorar logica para por um limitador
                 self.speedEnemyfast -= 500
                 pygame.time.set_timer(EVENT_ENEMYFAST, self.speedEnemyfast) 

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()


            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000:.1f}s', C_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, W_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, W_HEIGHT - 20))

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pygame.display.flip()
    
    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
