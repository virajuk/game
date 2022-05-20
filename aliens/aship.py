import pygame

from logs import get_logger
logger = get_logger('my_app')

from aliens.agame import AGame
from aliens.abullet import ABullet


class AShip:

    def __init__(self):
        self.image = pygame.image.load("images/alien-ship.png")
        self.screen = AGame.get_instance()
        self.x = int(self.screen.WINDOW_SIZE[0]/2) - 32
        self.y = self.screen.WINDOW_SIZE[1] - 64
        self.change = 0
        self.bullet = ABullet()

    def check_x(self):
        if self.x < 0:
            self.x = 0
            logger.info(f"{self.__class__.__name__} stopped {self.x}")
        elif self.x > self.screen.WINDOW_SIZE[0] - 64:
            self.x = self.screen.WINDOW_SIZE[0] - 64
            logger.info(f"{self.__class__.__name__} stopped {self.x}")

    def fire_bullet(self):
        pass
        # fire_bullet(bullet_x, bullet_y)