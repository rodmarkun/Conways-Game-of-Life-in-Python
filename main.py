import time
import pygame
import constants
import numpy as np


def update(screen, cells, size, with_progress=False):
    '''
    Updates all cells status for the current cycle.

    :param screen: Screen in which the game is displayed.
    :param cells: Cells matrix.
    :param size: Size of each cell.
    :param with_progress: Whether the game is currently playing or not.
    :return: Updated cells matrix.
    '''
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))

    for row, col in np.ndindex(cells.shape):
        # All neighbours:
        alive = np.sum(cells[row - 1:row + 2, col - 1:col + 2]) - cells[row, col]
        color = constants.COLOR_BG if cells[row, col] == 0 else constants.COLOR_ALIVE_NEXT

        # If cell is alive
        if cells[row, col] == 1:
            # Die by either being alone or because of overpopulation
            if alive < 2 or alive > 3:
                if with_progress:
                    color = constants.COLOR_DIE_NEXT
            elif 2 <= alive <= 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = constants.COLOR_ALIVE_NEXT
        # If cell is dead
        else:
            # Become alive
            if alive == 3:
                updated_cells[row, col] = 1
                if with_progress:
                    color = constants.COLOR_ALIVE_NEXT

        pygame.draw.rect(screen, color, (col * size, row * size, size - 1, size - 1))

    return updated_cells

def add_cell(screen, cells):
    '''
    Adds a cell in the current mouse position (activated whenever the user left-clicks on a cell).

    :param screen: Screen in which the game is displayed.
    :param cells: Cells matrix.
    :return: None
    '''
    pos = pygame.mouse.get_pos()
    cells[pos[1] // 10, pos[0] // 10] = 1
    update(screen, cells, 10)
    pygame.display.update()

def main():
    '''
    Main method which runs the game.

    :return: None
    '''

    # Initialize Pygame
    pygame.init()

    # Display config
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    cells = np.zeros(constants.CELL_AMOUNT)
    screen.fill(constants.COLOR_GRID)
    update(screen, cells, 10)
    pygame.display.flip()
    pygame.display.update()

    # Pause/Resume
    running = False

    # Main playable loop
    while True:
        for event in pygame.event.get():
            # Quit game
            if event.type == pygame.QUIT:
                print("Quitting game...")
                pygame.quit()
                return
            # Pause/Resume game
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if running:
                        print("Game paused.")
                    else:
                        print("Game resumed.")
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            # If user left-clicks, add a cell
            if pygame.mouse.get_pressed()[0]:
                add_cell(screen, cells)

        screen.fill(constants.COLOR_GRID)

        # If game is not paused, continue with the simulation
        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__ == '__main__':
    main()
