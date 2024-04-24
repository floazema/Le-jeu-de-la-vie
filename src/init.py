import pygame
import json
from globals import *
from main_loop import main_loop
from grid import init_grid

def main():    
    window = init_game()
    inputs = init_inputs()
    grid = init_grid()
    main_loop(window, inputs, grid)


def init_game():
    with open('json/init.json', 'r') as file:
        config = json.load(file)
    pygame.init()
    pygame.font.init()
    icon = pygame.image.load(config["window"]["icon"])
    window_title = config["window"]["title"]
    window_width = config["window"]["width"]
    window_height = config["window"]["height"]
    resizable = config["window"]["resizable"]
    fullscreen = config["window"]["fullscreen"]
    flags = pygame.RESIZABLE if resizable else 0
    if fullscreen:
        flags |= pygame.FULLSCREEN
    screen = pygame.display.set_mode((window_width, window_height), flags)
    pygame.display.set_caption(window_title)
    pygame.display.set_icon(icon)
    return screen

def init_inputs():
    with open('json/init.json', 'r') as file:
        config = json.load(file)
    inputs = {}
    for key in config["inputskeyboard"]:
        inputs[key] = [getattr(pygame, config["inputskeyboard"][key]), False, False]
    for key in config["inputsmouse"]:
        inputs[key] = [getattr(pygame, config["inputsmouse"][key]), False, False]
    return inputs
