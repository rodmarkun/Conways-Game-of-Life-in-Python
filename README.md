# Conway's Game of Life
This Python program simulates the Game of Life, a cellular automaton devised by mathematician John Conway in 1970. The program uses Pygame to display the simulation and NumPy to handle the two-dimensional grid of cells.

## Rules of the Game of Life

The game is played on a grid of cells, where each cell can either be alive or dead. The game evolves over time, with the status of each cell in the grid changing based on a set of rules:

    1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
    2. Any live cell with two or three live neighbors lives on to the next generation.
    3. Any live cell with more than three live neighbors dies, as if by overpopulation.
    4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

These rules are applied to every cell simultaneously, with each generation of the game being determined by the status of the cells in the previous generation. The Game of Life is considered a "zero-player" game, as the game's evolution is determined by the initial state of the grid and the rules, with no further input needed from the player once the game has started. The game has been studied extensively and is known to exhibit a wide range of interesting behaviors, including stable patterns, oscillations, and complex, chaotic behavior.

## main.py
The `update()` function updates the state of each cell in the grid according to the rules of the Game of Life. The function takes as input the screen object, the current grid of cells, the size of each cell in pixels, and an optional with_progress argument that determines whether to show the intermediate state of each cell as it is updated. The function returns the updated grid of cells.

The `main()` function initializes Pygame, creates the initial grid of cells, and displays it on the screen. It then enters a loop that checks for user input and updates the grid of cells accordingly. The loop ends when the user quits the program.

If the user presses the space bar, the program starts or stops running the simulation. If the user clicks the left mouse button, the program sets the cell at the clicked location to be alive. The `time.sleep(0.001)` statement limits the frame rate of the simulation.

## constants.py
The constants module defines various constants used in the program, such as the screen size, the colors of the cells, and the size of each cell.
