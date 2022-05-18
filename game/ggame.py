import cv2
import numpy as np

from .gworld import GWorld

from logs import get_logger
logger = get_logger('my_app')


class GGame:

    def __init__(self, world: GWorld) -> None:
        self.world = world
        self.world.save_grid()
