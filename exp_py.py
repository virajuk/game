import pygame
from experiment.knight import Knight

pygame.init()
clock = pygame.time.Clock()

# game screen
screen_width = 1600
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))
background = pygame.image.load("images/back.jpg")

# knight
knight = Knight(500, 400)
knight_group = pygame.sprite.Group()
knight_group.add(knight)

# game loop
running = True
while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q):
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                knight.walk()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                knight.__init__(500, 400)

    screen.blit(background, (0, 0))
    knight_group.draw(screen)
    knight_group.update()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
