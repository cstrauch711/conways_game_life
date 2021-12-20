# This is the main script for Conway's game of life

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

#define parameters
cell_color = "white"
background_color = "black"
n_cells = 12

#make grid of cells
#0 is dead and 1 is alive
def create_grid(n_cells, random_init=True):
    if random_init:
        grid = []
        for i in range(n_cells):
            row = []
            for j in range(n_cells):
                row.append( round(random.betavariate(alpha=1, beta=2.5)) )
            grid.append(row)
        return grid

def plot_grid(grid):
    plt.axes()
    for i in range(n_cells):
        for j in range(n_cells):
            if grid[i][j] == 1:
                rectangle = plt.Rectangle((10*i,10*j), 10, 10, fc=cell_color)
                plt.gca().add_patch(rectangle)
            else:
                rectangle = plt.Rectangle((10*i,10*j), 10, 10, fc=background_color)
                plt.gca().add_patch(rectangle)

    plt.axis("scaled")
    plt.show()

grid1 = create_grid(n_cells)
plot_grid(grid1)

#def update_grid():
