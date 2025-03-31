#W
import pygame


W_WIDTH = 567 
W_HEIGHT = 324

#C
C_ORANGE = (255, 165, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREENNESS = (0, 255, 0)
C_GREY = (0, 255, 255)

#E
EVENT_ENEMYFAST = pygame.USEREVENT + 1
ENTITY_SPEED = {
    "level1Bg0" : 0.5,
    "level1Bg1" : 0.51,
    "level1Bg2" : 0.9,
    "level1Bg3" : 1.2,
    "level1Bg4" : 2.0,    
    "level1Bg5" : 2,
    "PlayerShip" : 3,
    "EnemyFast" : 7,
    "EnemyFat" : 4, 
    "PlayerShipShot": 10,  
    "EnemyFatShot" : 40,
    "EnemyFastShot" : 1,
}
ENTITY_HEALTH = {
    "level1Bg0" : 9999,
    "level1Bg1" : 9999,
    "level1Bg2" : 9999,
    "level1Bg3" : 9999,
    "level1Bg4" : 9999,   
    "level1Bg5" : 9999,
    "PlayerShip" : 100,
    "EnemyFast" : 20,
    "EnemyFat" : 50,
    "PlayerShipShot": 1,
    "EnemyFatShot" : 1,
    "EnemyFastShot" : 1,
}
ENTITY_DAMAGE = {
    "level1Bg0": 0,
    "level1Bg1": 0,
    "level1Bg2": 0,
    "level1Bg3": 0,
    "level1Bg4": 0,
    "level1Bg5": 0,
    "PlayerShip": 1,
    "PlayerShipShot": 25,
    "EnemyFat": 1,
    "EnemyFatShot": 20,
    "EnemyFast": 1,
    "EnemyFastShot": 15,
}
ENTITY_SCORE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level2Bg0': 0,
    'Level2Bg1': 0,
    'Level2Bg2': 0,
    'Level2Bg3': 0,
    'Level2Bg4': 0,
    'PlayerShip': 0,
    'PlayerShipShot': 0,
    'EnemyFat': 200,
    'EnemyFatShot': 0,
    'EnemyFast': 125,
    'EnemyFastShot': 0,
}
#MENU_OPTION
MENU_OPTION = ["NEW GAME 1P",
               "NEW GAME 2P - COOPERATIVE",
               "NEW GAME 2P - COMPETITIVE",
               "SCORE",
               "QUIT"]
