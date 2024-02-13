from random import random

SIZE = 10

grid = [[random() > 0.5 for _ in range(SIZE)] for _ in range(SIZE)]



def display(grid):
    for x in range(SIZE):
        print(grid[x])


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



if __name__ == '__main__':
    print("Original grid")
    display(grid)
    counts = compute_counts_grid(grid)
    print("Counts grid")
    display(counts)
