from __future__ import annotations

import cv2
import numpy as np

from game.gworld import GBuildWorld
from game.gscout import GScout
from game.gtree import GTree

from logs import get_logger
logger = get_logger('my_app')


class GGame:

    def __init__(self, world: GBuildWorld) -> None:
        self.world = world

    def move(self, direction: str, item: GTree | GScout) -> None:

        valid = item.valid_move(direction)
        if not valid:
            logger.info(f"{item.__class__.__name__} move direction : {direction}")
            raise Exception("Not a valid move")

        logger.info(f"{item.__class__.__name__} coordinates before try to move {direction} : {item.x, item.y}")
        item.try_move(direction)
        logger.info(f"{item.__class__.__name__} coordinates after try to move {direction} : {item.x, item.y}")

        possible = self.world.can_place(item)
        if not possible:
            logger.info(f"{item.__class__.__name__} not possible move from {item.x, item.y} to {direction}")
            raise Exception("Not a possible move")

        self.world.grid[item.x, item.y, :] = (0, 0, 0)
        item.move(direction)
        self.world.grid[item.x, item.y, :] = item.color

        self.world.save_grid()

