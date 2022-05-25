import pygame
from config import *


class Game:

    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("MAN KIND")
        self.clock = pygame.time.Clock()

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_q):
                    running = False

            self.screen.fill('black')
            pygame.display.update()
            self.clock.tick(FPS)

        pygame.quit()


if __name__ == '__main__':

    game = Game()
    game.run()
