# Game of life (one hour)

This repo contains a minimal implementation
of [Conway's game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
[Ludwig Schubert](https://github.com/ludwigschubert) and I did it in about 50 minutes during a pair-programming session.

## Getting started

```
# Install dependencies (there is none woops 🙈)
poetry install

# Run the game of life !
poetry run python main.py
```

## Rules of the game

Each cell in the grid corresponds to either a 'live cell' (filled with `#`) or a 'dead cell' (empty: ` `).

At initialization, each cell of the grid is randomly assigned a live (`#`) or dead (` `) status.
Then, the game of life follows these four rules:

- Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies, as if by overpopulation.
- Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

