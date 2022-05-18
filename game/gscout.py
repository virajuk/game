import cv2
import numpy as np

from logs import get_logger
logger = get_logger('my_app')


class GScout:

    def __init__(self):
        self.color = (255, 0, 0)
        self.x, self.y = 0, 0
        self.movements = ["N", "W", "S", "E"]

    # def move(self, direction: str, grid: GWorld) -> None:
    #
    #     assert direction in self.movements, "Can't move"
    #
    #     (x, y) = self.coordinates
    #     grid.grid[x, y, :] = (0, 0, 0)
    #
    #     if direction == "N":
    #         x -= 1
    #     elif direction == "E":
    #         y += 1
    #     elif direction == "S":
    #         x += 1
    #     else:
    #         y -= 1
    #
    #     self.coordinates = (x, y)
    #     grid.grid[x, y, :] = self.color
    #     grid.save_grid()
