from game import GTree, GBuildWorld, GScout, GWorld

# world = GWorld(3)
# world.read_grid()
# print('#'*30)
# print(world.grid)

world = GBuildWorld(25)
# world.build_maze()
world.read_grid()

scouts = world.scouts
print(scouts)

########################
# game = GGame(world)


# scout.move("N", world)
# scout.move("E", world)
# scout.move("S", world)
# scout.move("W", world)
# scout.move("E", world)

world.examine_grid()
