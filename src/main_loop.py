import pygame
from grid import draw_grid, zoom_dezoom, navigate_on_grid
from globals import *
from bar import *
from algo import add_cells, algo

def get_inputs(inputs):
    for key in inputs:
        inputs[key][1] = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            for key in inputs:
                if event.key == inputs[key][0]:
                    inputs[key][1] = True
                    inputs[key][2] = True
        if event.type == pygame.KEYUP:
            for key in inputs:
                if event.key == inputs[key][0]:
                    inputs[key][1] = False
                    inputs[key][2] = False
        if event.type == pygame.MOUSEBUTTONUP:
            for key in inputs:
                if event.button == inputs[key][0]:
                    inputs[key][2] = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for key in inputs:
                if event.button == inputs[key][0]:
                    inputs[key][1] = True
                    inputs[key][2] = True
    return inputs

def main_loop(window, inputs, grid):
    draw = False
    VIEW_X = 0
    VIEW_Y = 0
    break_state = True
    speed = 1
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)
    last_time_called = 0
    while True:
        inputs = get_inputs(inputs)
        current_time = pygame.time.get_ticks()
        interval = 1000 // speed if speed != 0 else float('inf')
        if not buttons[1]["state"] and current_time > last_time_called + interval:
            last_time_called = current_time
            grid = algo(grid)
        window.fill((0, 0, 0))
        draw_grid(window, grid, VIEW_X, VIEW_Y)
        c_size = zoom_dezoom(inputs)
        VIEW_X, VIEW_Y = navigate_on_grid(inputs, VIEW_X, VIEW_Y, draw)
        draw, break_state, speed = tool_bar(window, inputs, font, draw, break_state, speed)
        add_cells(inputs, grid, draw, break_state, VIEW_X, VIEW_Y, c_size)
        pygame.display.flip()
        clock.tick(30)
