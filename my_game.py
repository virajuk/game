import pygame
import time
import random

from logs import get_logger
logger = get_logger('my_app')

pygame.init()

WINDOW_TITLE = "ACID RAIN"
WINDOW_SIZE = (1600, 900)
BACKGROUND_COLOR = (0, 20, 0)
ALIEN_SHIP = "images/alien-ship.png"
BUG = "images/bug.png"
BACKGROUND_IMAGE = "images/background.jpg"
BULLET_IMAGE = "images/bullet.png"

# create screen
screen = pygame.display.set_mode(WINDOW_SIZE)

# title
pygame.display.set_caption(WINDOW_TITLE)

# player
player_image = pygame.image.load(ALIEN_SHIP)
player_x = 770
player_y = 836
player_change = 0

# enemy
enemy_image = pygame.image.load(BUG)
enemy_x = random.randint(0, 1536)
enemy_y = random.randint(50, 150)
enemy_xchange = 0.3
enemy_ychange = 10

# bullet
bullet_image = pygame.image.load(BULLET_IMAGE)
bullet_x = 0
bullet_y = 836
# bullet_xchange = 0.3
bullet_ychange = 2
bullet_state = "READY"

# background
background_image = pygame.image.load(BACKGROUND_IMAGE)


def player(x, y):
    screen.blit(player_image, (x, y))


def enemy(x, y):
    screen.blit(enemy_image, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "FIRED"
    screen.blit(bullet_image, (x + 16, y))


# #game loop
running = True
while running:

    screen.fill(BACKGROUND_COLOR)

    screen.blit(background_image, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q):
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                logger.info(f" LEFT pressed")
                player_change = -0.3
            if event.key == pygame.K_RIGHT:
                logger.info(f" RIGHT pressed")
                player_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state == "READY":
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                logger.info(f" KEY released")
                player_change = 0

            # if event.key == pygame.K_SPACE:
            #     bullet_state = "READY"

    player_x += player_change

    if player_x <= 0:
        player_x = 0
    elif player_x >= 1536:
        player_x = 1536

    player(player_x, player_y)

    enemy_x += enemy_xchange

    if enemy_x <= 0:
        enemy_xchange = 0.3
        enemy_y += enemy_ychange
    elif enemy_x >= 1536:
        enemy_xchange = -0.3
        enemy_y += enemy_ychange

    if bullet_y <= 0:
        bullet_y = 836
        bullet_state = "READY"
    if bullet_state is "FIRED":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_ychange

    enemy(enemy_x, enemy_y)
    pygame.display.update()
