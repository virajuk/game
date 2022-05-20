import pygame

from logs import get_logger
logger = get_logger('my_app')

from aliens.agame import AGame
from aliens.abullet import ABullet


class AShip:

    def __init__(self):
        self.image = pygame.image.load("images/alien-ship.png")
        self.game = AGame.get_instance()
        self.x = int(self.game.WINDOW_SIZE[0]/2) - 32
        self.y = self.game.WINDOW_SIZE[1] - 64
        self.change = 0
        self.bullet = ABullet()

    def fly(self):
        self.x += self.change
        self.check_x()
        self.game.screen.blit(self.image, (self.x, self.y))

    def check_x(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.game.WINDOW_SIZE[0] - 64:
            self.x = self.game.WINDOW_SIZE[0] - 64

    def fire_bullet(self):
        self.bullet.x = self.x
        self.bullet.y = self.y
        self.bullet.fire()
        self.game.bullet = self.bullet
        self.game.bullets.append(self.bullet)
        self.bullet = ABullet()
