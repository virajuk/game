import pygame
import math


class Knight(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load("images/1_KNIGHT/idle/Knight_01__IDLE_000.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/idle/Knight_01__IDLE_001.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/idle/Knight_01__IDLE_002.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/idle/Knight_01__IDLE_003.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/idle/Knight_01__IDLE_004.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/idle/Knight_01__IDLE_005.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/idle/Knight_01__IDLE_006.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/idle/Knight_01__IDLE_007.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/idle/Knight_01__IDLE_008.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/idle/Knight_01__IDLE_009.png"))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.change_x, self.change_y = 0, 0
        self.current_x, self.current_y = x, y
        self.new_x, self.new_y = 0, 0

    def update(self):

        self.current_sprite += 0.3
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0
        self.image = self.sprites[int(self.current_sprite)]

        if self.current_x != self.new_x or self.current_y != self.new_y:
            self.current_x += self.change_x
            self.current_y += self.change_y
            self.rect.center = (self.current_x, self.current_y)

            print(self.current_x, self.new_x, self.change_x, self.current_y, self.new_y, self.change_y)
            print(self.rect.center)

    def walk(self):
        self.sprites = []
        self.sprites.append(pygame.image.load("images/1_KNIGHT/walk/Knight_01__WALK_000.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/walk/Knight_01__WALK_001.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/walk/Knight_01__WALK_002.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/walk/Knight_01__WALK_003.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/walk/Knight_01__WALK_004.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/walk/Knight_01__WALK_005.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/walk/Knight_01__WALK_006.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/walk/Knight_01__WALK_007.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/walk/Knight_01__WALK_008.png"))
        self.sprites.append(pygame.image.load("images/1_KNIGHT/walk/Knight_01__WALK_009.png"))

        self.current_sprite = 3

        self.current_sprite += 0.3
        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 3
        self.image = self.sprites[int(self.current_sprite)]

        self.current_x, self.current_y = self.rect.center
        self.new_x, self.new_y = pygame.mouse.get_pos()
        self.change_x, self.change_y = 4, 1
        self.update()





    # def move(self):
    #     start_x, start_y = self.rect.center
    #     end_x, end_y = pygame.mouse.get_pos()
    #
    #     self.rect.center = pygame.mouse.get_pos()

