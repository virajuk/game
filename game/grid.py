import cv2
import numpy as np

from logs import get_logger
logger = get_logger('my_app')


class GGrid:

    def __init__(self, size: int) -> None:
        self._width = size
        self._height = size
        self.grid = np.ones([self._height, self._width, 3])

    def save_png(self) -> None:

        self.grid[0, 2, :] = (255, 0, 0)
        self.grid[0, 3, :] = (0, 255, 0)

        logger.info(f"{self.__class__.__name__} Image : {self.grid.shape}")

        cv2.imwrite('images/grid.png', self.grid)

    def examine_grid(self) -> None:

        image = cv2.imread('/home/viraj/HUSTLE/GAME/images/gimp.png')
        # cv2.imshow("image", image)
        # cv2.waitKey()

        logger.info(f"{self.__class__.__name__} Image : {image.shape}")
        logger.info(f"{self.__class__.__name__} Image : {image[:, :, 0]}")
        logger.info(f"{self.__class__.__name__} Image : {image[:, :, 1]}")
        logger.info(f"{self.__class__.__name__} Image : {image[:, :, 2]}")


class GTree:

    def __init__(self):
        pass
