import cv2
import numpy as np

from .gworld import GWorld

from logs import get_logger
logger = get_logger('my_app')


class GScout:

    def __init__(self):
        self.color = (255, 0, 0)
        self.coordinates = ()
        self.movements = ["N", "W", "S", "E"]

    def place(self, x: int, y: int, grid: GWorld) -> None:

        assert (x <= (grid.width - 1) and y <= (grid.height - 1)), "Can't go out side grid"

        self.coordinates = (x, y)
        grid.grid[x, y, :] = self.color
        grid.save_grid()

        grid.scouts.append(self)
        logger.info(f"{self.__class__.__name__} Coordinates : {self.coordinates}")

    def move(self, direction: str, grid: GWorld) -> None:

        assert direction in self.movements, "Can't move"

        (x, y) = self.coordinates
        grid.grid[x, y, :] = (0, 0, 0)

        if direction == "N":
            x -= 1
        elif direction == "E":
            y += 1
        elif direction == "S":
            x += 1
        else:
            y -= 1

        self.coordinates = (x, y)
        grid.grid[x, y, :] = self.color
        grid.save_grid()
