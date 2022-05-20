import pygame

from aliens import AShip
from aliens import AGame
from aliens import ABug
from aliens import ABullet

from logs import get_logger
logger = get_logger('my_app')

pygame.init()
game = AGame()

background_image = game.start_game()

game.ship = AShip()
game.bug = ABug()

# game loop
running = True
while running:

    game.screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q):
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                # logger.info(f" LEFT pressed")
                game.ship.change = -0.3
            if event.key == pygame.K_RIGHT:
                # logger.info(f" RIGHT pressed")
                game.ship.change = 0.3
            if event.key == pygame.K_SPACE:
                if game.ship.bullet.state == "READY":
                    game.ship.fire_bullet()
                    logger.info(f" ship fired bullet {(game.ship.x, game.ship.y)}")

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                # logger.info(f" KEY released")
                game.ship.change = 0

    game.ship.fly()
    game.bug.fly()

    if game.ship.bullet.state == "FIRED":
        game.ship.bullet.fire()

    pygame.display.update()
