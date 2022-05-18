import cv2
import numpy as np

from logs import get_logger
logger = get_logger('my_app')


class GGrid:

    def __init__(self, size: int) -> None:
        self.width = size
        self.height = size
        self.grid = np.ones([self.height, self.width, 3])
        self.trees = []
        self.scouts = []

    def save_grid(self) -> None:

        logger.info(f"{self.__class__.__name__} Image : {self.grid.shape}")
        cv2.imwrite('images/grid.png', self.grid)

    def examine_grid(self) -> None:
        logger.info(f"{self.__class__.__name__} Trees : {len(self.trees)}")
        logger.info(f"{self.__class__.__name__} Trees : {len(self.scouts)}")


class GTree:

    def __init__(self):
        self.color = (0, 255, 0)
        self.coordinates = ()

    def plant(self, x: int, y: int, grid: GGrid) -> None:

        assert (x <= (grid.width - 1) and y <= (grid.height - 1)), "Can't plant a tree out side grid"

        assert not self.already_planted(grid), "This tree already planted"

        self.coordinates = (x, y)

        grid.grid[x, y, :] = self.color
        grid.save_grid()

        grid.trees.append(self)

        logger.info(f"{self.__class__.__name__} Coordinates : {self.coordinates}")

    def already_planted(self, grid: GGrid) -> bool:

        if self in grid.trees:
            return True
        return False


class GScout:

    def __init__(self):
        self.color = (255, 0, 0)
        self.coordinates = ()
        self.movements = ["N", "W", "S", "E"]

    def place(self, x: int, y: int, grid: GGrid) -> None:

        assert (x <= (grid.width - 1) and y <= (grid.height - 1)), "Can't go out side grid"

        self.coordinates = (x, y)
        grid.grid[x, y, :] = self.color
        grid.save_grid()

        grid.scouts.append(self)

        logger.info(f"{self.__class__.__name__} Coordinates : {self.coordinates}")

    def move(self, direction: str):

        assert direction in self.movements, "Can't move"


