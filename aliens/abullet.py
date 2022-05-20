import pygame

from logs import get_logger
logger = get_logger('my_app')

from aliens.agame import AGame


class ABullet:

    def __init__(self):
        self.image = pygame.image.load("images/bullet.png")
        self.game = AGame.get_instance()
        self.x = 0
        self.y = 0
        self.change = 0.5
        self.state = "READY"

    def fire(self):
        self.state = "FIRED"
        self.game.screen.blit(self.image, (self.x + 16, self.y))
        self.y -= self.change
        self.check_location()
        # logger.info(f"{self.__class__.__name__} bullet fired {(self.x, self.y)}")

    def check_location(self):
        if self.y < 0:
            self.game.bullets.remove(self)
            # self.y = self.game.WINDOW_SIZE[1] - 64
            # self.state = "READY"
            # logger.info(f" bullet y coord {self.y}")
