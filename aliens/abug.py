import random

import pygame

from logs import get_logger
logger = get_logger('my_app')

from aliens.ascreen import AScreen


class ABug:

    def __init__(self):
        self.image = pygame.image.load("images/bug.png")
        self.screen = AScreen.get_instance()
        self.x = random.randint(0, self.screen.WINDOW_SIZE[0] - 64)
        self.y = random.randint(50, int(self.screen.WINDOW_SIZE[1]*0.1))
        self.x_change = 0.3
        self.y_change = 10

    def check_location(self):
        if self.x < 0:
            self.x_change = 0.3
            self.y += self.y_change
            # logger.info(f"{self.__class__.__name__} stopped {self.x}")
        elif self.x > self.screen.WINDOW_SIZE[0] - 64:
            self.x_change = -0.3
            self.y += self.y_change
            # logger.info(f"{self.__class__.__name__} stopped {self.x}")


