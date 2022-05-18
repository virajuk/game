import cv2
import numpy as np

from .gworld import GWorld

from logs import get_logger
logger = get_logger('my_app')


class GTree:

    def __init__(self):
        self.color = (0, 255, 0)
        self.coordinates = ()

    def plant(self, x: int, y: int, grid: GWorld) -> None:

        assert (x <= (grid.width - 1) and y <= (grid.height - 1)), "Can't plant a tree out side grid"

        assert not self.already_planted(grid), "This tree already planted"

        self.coordinates = (x, y)

        grid.grid[x, y, :] = self.color
        grid.save_grid()

        grid.trees.append(self)

        logger.info(f"{self.__class__.__name__} Coordinates : {self.coordinates}")

    def already_planted(self, grid: GWorld) -> bool:

        if self in grid.trees:
            return True
        return False
