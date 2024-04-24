import pygame
from globals import *
from bar import *

def add_cells(inputs, grid, draw, brake_state, VIEW_X, VIEW_Y, c_size):
    if draw == False:
        return
    if brake_state == False:
        return
    print(c_size)
    if inputs["left"][2]:
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            if button["rect"].collidepoint(mouse_pos):
                return
        x = (mouse_pos[0] // c_size) + VIEW_X
        y = (mouse_pos[1] // c_size) + VIEW_Y
        if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE:
            grid[y][x] = 1

def get_neighbors(x, y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx != 0 or dy != 0:
                yield (x + dx, y + dy)

def algo(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    live_cells = {(x, y) for y in range(rows) for x in range(cols) if grid[y][x] == 1}
    new_live_cells = set()
    cells_to_check = set()
    for cell in live_cells:
        cells_to_check.add(cell)
        cells_to_check.update(get_neighbors(*cell))

    for cell in cells_to_check:
        x, y = cell
        if x < 0 or x >= cols or y < 0 or y >= rows:
            continue
        live_neighbors = sum((nx, ny) in live_cells for nx, ny in get_neighbors(x, y))
        if (grid[y][x] == 1 and live_neighbors in [2, 3]) or (grid[y][x] == 0 and live_neighbors == 3):
            new_live_cells.add(cell)

    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]
    for x, y in new_live_cells:
        new_grid[y][x] = 1

    return new_grid