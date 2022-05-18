import cv2
import numpy as np

from logs import get_logger
logger = get_logger('my_app')


class GWorld:

    def __init__(self, size: int) -> None:

        logger.info(f"{self.__class__.__name__} Building")

        self.width = size
        self.height = size
        self.grid = np.ones([self.height, self.width, 3])
        self.trees = []
        self.scouts = []

    def save_grid(self) -> None:

        logger.info(f"{self.__class__.__name__} shape : {self.grid.shape}")
        cv2.imwrite('images/grid.png', self.grid)

    def examine_grid(self) -> None:
        logger.info(f"{self.__class__.__name__} Trees count : {len(self.trees)}")
        logger.info(f"{self.__class__.__name__} Scouts count : {len(self.scouts)}")


class GBuildWorld(GWorld):

    def __init__(self, size: int) -> None:

        super().__init__(size)
