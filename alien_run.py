import time
import random

import pygame

from aliens import AShip
from aliens import AScreen
from aliens import ABug
from aliens import ABullet

from logs import get_logger
logger = get_logger('my_app')

pygame.init()
game = AScreen()

BULLET_IMAGE = "images/bullet.png"

# create screen
screen = pygame.display.set_mode(game.WINDOW_SIZE)
pygame.display.set_caption(game.WINDOW_TITLE)
background_image = pygame.image.load(game.BACKGROUND_IMAGE)

ship = AShip()

bug = ABug()



# game loop
running = True
while running:

    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q):
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # logger.info(f" LEFT pressed")
                ship.change = -0.3
            if event.key == pygame.K_RIGHT:
                # logger.info(f" RIGHT pressed")
                ship.change = 0.3
            if event.key == pygame.K_SPACE:
                if ship.bullet.state == "READY":
                    ship.bullet.x = ship.x
                    logger.info(f" bullet x {ship.bullet.x}")
                    # fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                # logger.info(f" KEY released")
                ship.change = 0

    ship.x += ship.change
    ship.check_x()
    screen.blit(ship.image, (ship.x, ship.y))

    bug.x += bug.x_change
    bug.check_location()
    screen.blit(bug.image, (bug.x, bug.y))

    # screen.blit(ship.bullet.image, (ship.bullet.x, ship.bullet.y))

    pygame.display.update()
