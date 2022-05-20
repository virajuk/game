import pygame
# from pygame import Surface


class AScreen:

    __instance = None

    @staticmethod
    def get_instance():

        if AScreen.__instance is None:
            AScreen()
        return AScreen.__instance

    def __init__(self) -> None:
        """

        :rtype: object
        """
        if AScreen.__instance is not None:
            raise Exception("Fuck you!")
        else:
            self.WINDOW_TITLE = "ACID RAIN"
            self.WINDOW_SIZE = (800, 600)
            self.BACKGROUND_IMAGE = "images/background.jpg"

            AScreen.__instance = self


if __name__ == '__main__':

    screen = AScreen()
    print(screen.WINDOW_TITLE)

    # screen1 = AScreen.get_instance()
    # print(screen1.WINDOW_TITLE)

    # screen2 = AScreen.get_instance()
    # print(screen2.WINDOW_TITLE)

    # sur = Surface((1600, 900))
    # print(dir(sur))
