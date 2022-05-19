from game import GTree, GBuildWorld, GScout, GWorld, GGame

# world = GWorld(3)
# world.read_grid()
# print('#'*30)
# print(world.grid)

world = GBuildWorld(7)


# world.build_maze()
world.read_grid()

scouts = world.scouts

########################
game = GGame(world)

scout = game.world.scouts[0]

game.move("E", scout)

# scout.move("N", world)
# scout.move("E", world)
# scout.move("S", world)
# scout.move("W", world)
# scout.move("E", world)

world.examine_grid()
