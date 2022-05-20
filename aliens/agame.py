import pygame
# from pygame import Surface


class AGame:

    __instance = None
    screen = None
    ship = None
    bug = None
    bullet = None
    bullets = []

    @staticmethod
    def get_instance():

        if AGame.__instance is None:
            AGame()
        return AGame.__instance

    def __init__(self) -> None:

        if AGame.__instance is not None:
            raise Exception("Fuck you!")
        else:
            self.WINDOW_TITLE = "ACID RAIN"
            self.WINDOW_SIZE = (800, 600)
            self.BACKGROUND_IMAGE = "images/background.jpg"

            AGame.__instance = self

    def start_game(self):

        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)
        pygame.display.set_caption(self.WINDOW_TITLE)
        background_image = pygame.image.load(self.BACKGROUND_IMAGE)
        return background_image


if __name__ == '__main__':

    screen = AGame()
    print(screen.WINDOW_TITLE)

    # screen1 = AScreen.get_instance()
    # print(screen1.WINDOW_TITLE)

    # screen2 = AScreen.get_instance()
    # print(screen2.WINDOW_TITLE)

    # sur = Surface((1600, 900))
    # print(dir(sur))
