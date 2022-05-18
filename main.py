from game import GTree, GScout, GGame, GBuildWorld

world = GBuildWorld(9)

game = GGame(world)




# world = GWorld(9)
#
# tree1 = GTree()
# tree1.plant(0, 2, world)
#
# tree2 = GTree()
# tree2.plant(4, 0, world)
#
# scout = GScout()
# scout.place(4, 1, world)
#
# # scout.move("N", world)
# # scout.move("E", world)
# # scout.move("S", world)
# # scout.move("W", world)
# scout.move("E", world)
#
# world.examine_grid()
