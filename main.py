import sys
from random import random
import os
from time import sleep

SIZE = (30,60)


# grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
# grid[3][4] = 1
# grid[3][5] = 1
# grid[3][6] = 1


def convert_nicely(state):
    if state == True:
        return "█"
    return " "


def display(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            print(convert_nicely(grid[x][y]), end="")
        print("")

def display_counts(counts_grid):
    for x in range(len(counts_grid)):
        print(counts_grid[x])


def count_neighbors(grid, x, y):
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    total = 0
    x_length = len(grid)
    y_length = len(grid[0])
    for dx, dy in neighbor_offsets:
        total += grid[(x + dx) % x_length][(y + dy) % y_length]

    return total


def compute_counts_grid(grid):
    counts = [[0] * len(grid[0]) for _ in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            counts[x][y] = count_neighbors(grid, x, y)
    return counts


def should_live(count, current_state):
    # Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    # Any live cell with two or three live neighbors lives on to the next generation.
    # Any live cell with more than three live neighbors dies, as if by overpopulation.
    # Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

    if count < 2:
        return False
    if count == 3:
        return True
    if count == 2:
        return current_state
    if count > 3:
        return False

    raise ValueError("SHould never get here")


def apply_rules(grid):
    counts_grid = compute_counts_grid(grid)
    new_grid = [[0] * len(grid[0]) for _ in range(len(grid))]
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            count = counts_grid[x][y]
            is_alive = should_live(count, grid[x][y])
            new_grid[x][y] = is_alive
    return new_grid

if __name__ == '__main__':
    grid = [[random() > 0.5 for _ in range(SIZE[1])] for _ in range(SIZE[0])]
    print("Original grid")
    display(grid)
    counts = compute_counts_grid(grid)
    print("Counts grid")
    display_counts(counts)

    while True:
        new_grid = apply_rules(grid)
        if new_grid == grid:
            print("Grid no longer evolves")
            exit(0)
        
        # display new grid
        os.system("clear")
        display(new_grid)
        sys.stdout.flush()

        grid = new_grid
        sleep(1 / 30.0)

