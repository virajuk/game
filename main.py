from game import GGrid, GTree, GScout

grid = GGrid(9)
# grid.save_png()
# grid.examine_grid()

tree1 = GTree()
tree1.plant(0, 2, grid)

tree2 = GTree()
tree2.plant(4, 0, grid)

scout = GScout()
scout.place(4, 1, grid)

scout.move("N")

grid.examine_grid()
