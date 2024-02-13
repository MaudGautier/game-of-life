import sys
from random import random
import os
from time import sleep

SIZE = 50

grid = [[random() > 0.5 for _ in range(SIZE)] for _ in range(SIZE)]
# grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
# grid[3][4] = 1
# grid[3][5] = 1
# grid[3][6] = 1


def convert_nicely(state):
    if state == True:
        return "#"
    return " "


def display(grid):
    for x in range(SIZE):
        for y in range(SIZE):
            print(convert_nicely(grid[x][y]), end="")
        print("")

def display_counts(counts_grid):
    for x in range(SIZE):
        print(counts_grid[x])


def count_neighbors(grid, x, y):
    neighbor_offsets = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    total = 0
    for dx, dy in neighbor_offsets:
        total += grid[(x + dx) % SIZE][(y + dy) % SIZE]

    return total


def compute_counts_grid(grid):
    counts = [[0] * SIZE for _ in range(SIZE)]
    for x in range(SIZE):
        for y in range(SIZE):
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
    for x in range(SIZE):
        for y in range(SIZE):
            count = counts_grid[x][y]
            is_alive = should_live(count, grid[x][y])
            grid[x][y] = is_alive


if __name__ == '__main__':
    print("Original grid")
    display(grid)
    counts = compute_counts_grid(grid)
    print("Counts grid")
    display_counts(counts)

    for cycle in range(1000):
        sleep(0.03)
        os.system("clear")
        # print("After cycle", cycle)
        apply_rules(grid)
        display(grid)
        sys.stdout.flush()
