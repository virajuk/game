import random

import pygame

from logs import get_logger
logger = get_logger('my_app')

from aliens.agame import AGame


class ABug:

    def __init__(self):
        self.image = pygame.image.load("images/bug.png")
        self.game = AGame.get_instance()
        self.x = random.randint(0, self.game.WINDOW_SIZE[0] - 64)
        self.y = random.randint(50, int(self.game.WINDOW_SIZE[1]*0.1))
        self.x_change = 0.3
        self.y_change = 10

    def fly(self):
        self.x += self.x_change
        self.check_location()
        self.game.screen.blit(self.image, (self.x, self.y))

    def check_location(self):
        if self.x < 0:
            self.x_change = 0.3
            self.y += self.y_change
        elif self.x > self.game.WINDOW_SIZE[0] - 64:
            self.x_change = -0.3
            self.y += self.y_change


