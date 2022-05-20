import pygame

from logs import get_logger
logger = get_logger('my_app')

from aliens.agame import AGame


class ABullet:

    def __init__(self):
        self.image = pygame.image.load("images/bullet.png")
        self.screen = AGame.get_instance()
        self.x = 0
        self.y = self.screen.WINDOW_SIZE[1] - 64
        self.change = 2
        self.state = "READY"
