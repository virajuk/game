from __future__ import annotations

import random

import cv2
import numpy as np

from logs import get_logger
logger = get_logger('my_app')

from game.gtree import GTree
from game.gscout import GScout


class GWorld:

    def __init__(self, size: int) -> None:

        logger.info(f"{self.__class__.__name__} Building")

        self.width = size
        self.height = size
        self.grid = np.zeros([self.height, self.width, 3])
        self.items = []
        self.trees = []
        self.scouts = []

    def save_grid(self) -> None:

        # logger.info(f"{self.__class__.__name__} shape : {self.grid.shape}")
        cv2.imwrite('images/grid.png', self.grid)

    def examine_grid(self) -> None:

        logger.info(f"{self.__class__.__name__} item count : {len(self.items)}")
        logger.info(f"{self.__class__.__name__} tree count : {len(self.trees)}")
        logger.info(f"{self.__class__.__name__} scout count : {len(self.scouts)}")


class GBuildWorld(GWorld):

    def __init__(self, size: int) -> None:

        super().__init__(size)
        # self.build_maze()

    def read_grid(self) -> None:

        self.items, self.trees, self.scouts = [], [], []

        self.grid = cv2.imread('images/grid.png')
        height, width, channel = self.grid.shape

        # TODO: find a better way to read numpy array
        for i in range(0, height):
            for j in range(0, width):
                if tuple(self.grid[i, j, :]) == (255, 0, 0):
                    scout = GScout()
                    coordinates = (i, j)
                    self.add_scout(coordinates, scout)
                elif tuple(self.grid[i, j, :]) == (0, 255, 0):
                    tree = GTree()
                    coordinates = (i, j)
                    self.add_tree(coordinates, tree)

        cv2.imwrite('images/grid_cp.png', self.grid)

    def build_maze(self) -> None:

        world_size = self.width*self.height
        # logger.info(f"{self.__class__.__name__} world size : {world_size}")

        tree_count = int(world_size*0.5)
        # logger.info(f"{self.__class__.__name__} tree_count : {tree_count}")

        while tree_count > len(self.trees):
            tree = GTree()
            coordinates = (random.randint(0, self.height-1), random.randint(0, self.width-1))
            try:
                self.add_tree(coordinates, tree)
            except AssertionError as msg:
                logger.info(f"{msg}")

        while not len(self.scouts):
            scout = GScout()
            coordinates = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            try:
                self.add_scout(coordinates, scout)
            except AssertionError as msg:
                logger.info(f"{msg}")

    def add_tree(self, coordinates: tuple, tree: GTree) -> None:

        self.__add_item(coordinates, tree)
        self.trees.append(tree)

    def add_scout(self, coordinates: tuple, scout: GScout) -> None:

        self.__add_item(coordinates, scout)
        self.scouts.append(scout)

    def __add_item(self, coordinates: tuple, item: GTree | GScout) -> None:

        item.x, item.y = coordinates

        assert (item.x <= (self.width - 1) and item.y <= (self.height - 1)), f"cannot add {item.__class__.__name__} out side world"
        assert self.__already_placed(item), f"{item.__class__.__name__} already placed"
        assert self.__can_place(item), f"{item.__class__.__name__} cannot place here"

        self.grid[item.x, item.y, :] = item.color
        self.save_grid()

        self.items.append(item)

    def __already_placed(self, item: GTree | GScout) -> bool:

        if item in self.items:
            return False

        return True

    def __can_place(self, item: GTree | GScout) -> bool:

        for placed_item in self.items:

            if placed_item.x == item.x and placed_item.y == item.y:
                return False

        return True
