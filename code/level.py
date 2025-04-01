#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from tkinter.font import Font
from code.enemy import Enemy
from code.player import Player
from code.entityMediator import EntityMediator
from code.Const import C_GREENNESS, C_WHITE, EVENT_ENEMYFAST, EVENT_TIMEOUT, W_HEIGHT, W_WIDTH
from code.entity import Entity
import pygame

from code.entityFactory import EntityFactory
from code.player import Player


class Level:
    def __init__(self, window, name, menu_list):
        self.window = window
        self.name = name
        self.menu_list = menu_list
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('PlayerShip'))
        self.timeout = 0
        self.speedEnemyfast = 4000
        pygame.time.set_timer(EVENT_ENEMYFAST, self.speedEnemyfast)
        pygame.time.set_timer(EVENT_TIMEOUT, 100)
        self.lastScore = 0

    def run(self):
        pygame.mixer_music.load('./Assets/EpicEnd.ogg')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        running = True
        while running:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, Player) or (hasattr(ent, 'name') and ent.name == 'EnemyFat'):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'PlayerShip':
                    self.level_text(20, f'Player - Health: {ent.health} | Score: {ent.score} | Timeout  {self.timeout / 1000:.1f}s', C_GREENNESS, (10, 25))
                    self.last_score = ent.score
                    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == EVENT_ENEMYFAST:
                    choice = random.choice(('EnemyFast', 'EnemyFat'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout += 100

                found_player = False
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True
                if not found_player:
                    self.game_over(self.last_score)
                    running = False
                    

            self.level_text(14, f'fps: {clock.get_fps():.0f}', C_WHITE, (10, W_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, W_HEIGHT - 20))

            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            pygame.display.flip()

    def game_over(self, score_player):
        pygame.mixer_music.stop()  
        pygame.mixer_music.load('./Assets/Defeated.ogg')
        pygame.mixer_music.play(-1)

        # Exibe o fundo do nível
        for ent in self.entity_list:
            if ent.name.startswith("level1Bg"):  
                self.window.blit(source=ent.surf, dest=ent.rect)

        # Exibe os textos de "Game Over", Score, Timeout e Total
        self.level_text(
            text_size=48,
            text="GAME OVER",
            text_color=C_GREENNESS, 
            text_pos=(W_WIDTH // 2 - 120, W_HEIGHT // 2 - 80)  
        )
        self.level_text(
            text_size=24,
            text=f"Score: {score_player}",
            text_color=C_WHITE,  
            text_pos=(W_WIDTH // 2 - 120, W_HEIGHT // 2 - 20)  
        )
        self.level_text(
            text_size=24,
            text=f"Time Survived: {self.timeout / 1000:.1f}s",
            text_color=C_WHITE, 
            text_pos=(W_WIDTH // 2 - 120, W_HEIGHT // 2)
        )
        self.level_text(
            text_size=24,
            text=f"Total: {score_player + self.timeout / 1000:.1f}",
            text_color=C_WHITE, 
            text_pos=(W_WIDTH // 2 - 120, W_HEIGHT // 2 + 50)
        )
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    waiting = False

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)