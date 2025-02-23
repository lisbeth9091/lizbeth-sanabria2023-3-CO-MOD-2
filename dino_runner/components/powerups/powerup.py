import random
import pygame
from pygame.sprite import Sprite
from dino_runner.utils.constants import SCREEN_WIDTH, HAMMER 

class Powerup(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.rect.y = random.randint(125, 175)
        self.start_time = 0

    def update(self, game_speed, powerups):
        # Configurando la animacion del powerup de derecha a izquierda
        self.rect.x -= game_speed
        # eliminando powerup que esta a la izquierda fuera de la panatalla
        if self.rect.x < -self.rect.width:
            powerups.pop()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Launcher(Sprite):
    def __init__(self):
        self.image = HAMMER 
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0

    def update(self, game ):
        self.rect.x += game.game_speed
        if self.rect.x == SCREEN_WIDTH + 200:
            game.flag_hammer = False
            
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x, self.rect.y))
             
    
    
