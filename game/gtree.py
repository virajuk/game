import cv2
import numpy as np

from logs import get_logger
logger = get_logger('my_app')


class GTree:

    def __init__(self):
        self.color = (0, 255, 0)
        self.x, self.y = 0, 0
