import pygame
import random
from globals import *
from bar import *

def init_grid():
    return [[ 0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def draw_grid(window, grid, VIEW_X, VIEW_Y):
    window.fill(BLACK)

    start_x = max(0, VIEW_X)
    end_x = min(GRID_SIZE, start_x + (WINDOW_WIDTH // CELL_SIZE) + 1)
    start_y = max(0, VIEW_Y)
    end_y = min(GRID_SIZE, start_y + (WINDOW_HEIGHT // CELL_SIZE) + 1)

    for y in range(start_y, end_y):
        for x in range(start_x, end_x):
            rect = pygame.Rect((x - VIEW_X) * CELL_SIZE, (y - VIEW_Y) * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(window, WHITE if grid[y][x] else BLACK, rect)
            pygame.draw.rect(window, GRAY, rect, 1)

def zoom_dezoom(inputs):
    global CELL_SIZE
    if inputs["scrollup"][1]:
        CELL_SIZE += 1
    if inputs["scrolldown"][1]:
        CELL_SIZE -= 1
    if CELL_SIZE < 15:
        CELL_SIZE = 15
    if CELL_SIZE > 75:
        CELL_SIZE = 75
    return CELL_SIZE

def navigate_on_grid(inputs, VIEW_X, VIEW_Y, draw):
    global last_mouse_pos
    if inputs["left"][2] == False:
        last_mouse_pos = None
    if inputs["left"][2] and draw == False:
        print(VIEW_X, VIEW_Y)
        current_mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            if button["rect"].collidepoint(current_mouse_pos):
                return VIEW_X, VIEW_Y
        if last_mouse_pos != None:
            dx = (last_mouse_pos[0] - current_mouse_pos[0]) // CELL_SIZE
            dy = (last_mouse_pos[1] - current_mouse_pos[1]) // CELL_SIZE
            VIEW_X += dx
            VIEW_Y += dy
        last_mouse_pos = current_mouse_pos

    if inputs["kleft"][2]:
        VIEW_X -= 1
    if inputs["kright"][2]:
        VIEW_X += 1
    if inputs["kup"][2]:
        VIEW_Y -= 1
    if inputs["kdown"][2]:
        VIEW_Y += 1

    if VIEW_X < 0:
        VIEW_X = 0
    if VIEW_Y < 0:
        VIEW_Y = 0
    if VIEW_X > GRID_SIZE - (WINDOW_WIDTH // CELL_SIZE):
        VIEW_X = GRID_SIZE - (WINDOW_WIDTH // CELL_SIZE)
    if VIEW_Y > GRID_SIZE - (WINDOW_HEIGHT // CELL_SIZE):
        VIEW_Y = GRID_SIZE - (WINDOW_HEIGHT // CELL_SIZE)
    return VIEW_X, VIEW_Y