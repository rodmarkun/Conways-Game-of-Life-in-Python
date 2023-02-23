import time
import pygame
import constants
import numpy as np


def update(screen, cells, size, with_progress=False):
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


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))

    cells = np.zeros((60, 80))
    screen.fill(constants.COLOR_GRID)
    update(screen, cells, 10)
    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10)
                pygame.display.update()

        screen.fill(constants.COLOR_GRID)

        if running:
            cells = update(screen, cells, 10, with_progress=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__ == '__main__':
    main()
