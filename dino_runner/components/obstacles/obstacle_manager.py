import pygame
from dino_runner.components.cactus import cactus
from dino_runner.utils.constants import SMALL_CACTUS 

class obstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            cactus = cactus(SMALL_CACTUS)
            self.obstacles.append(cactus)

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen):