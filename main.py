from game import GTree, GBuildWorld, GScout, GWorld

# world = GWorld(3)
# world.read_grid()
# print('#'*30)
# print(world.grid)

world = GBuildWorld(25)
world.build_maze()
world.read_grid()

# tree1 = GTree()
# coord = (0, 2)
# world.add_tree(coord, tree1)
#
# tree2 = GTree()
# coord = (4, 0)
# world.add_tree(coord, tree2)
#
# scout1 = GScout()
# coord = (4, 1)
# world.add_scout(coord, scout1)
#
# scout2 = GScout()
# coord = (8, 2)
# world.add_scout(coord, scout2)

########################
# game = GGame(world)


# scout.move("N", world)
# scout.move("E", world)
# scout.move("S", world)
# scout.move("W", world)
# scout.move("E", world)

world.examine_grid()
