from globals import *
import pygame

DARK_GRAY = (150, 150, 150)
LIGHT_GRAY = (230, 230, 230)
BLACK = (0, 0, 0)

button_width = 105
button_height = 30
spacing = 10
total_width = 4 * button_width + 3 * spacing

start_x = (WINDOW_WIDTH - total_width) // 2

buttons = [
    {"label": "Place cell", "rect": pygame.Rect(start_x, WINDOW_HEIGHT - 35, button_width, button_height), "state": False, "action": "toggle_draw"},
    {"label": "Break", "rect": pygame.Rect(start_x + button_width + spacing, WINDOW_HEIGHT - 35, button_width, button_height), "state": True, "action": "toggle_break"},
    {"label": "+", "rect": pygame.Rect(start_x + 2 * (button_width + spacing), WINDOW_HEIGHT - 35, button_width, button_height), "action": "increase_speed"},
    {"label": "-", "rect": pygame.Rect(start_x + 3 * (button_width + spacing), WINDOW_HEIGHT - 35, button_width, button_height), "action": "decrease_speed"}
]

def tool_bar(window, inputs, font, draw, break_state, speed):
    if inputs["left"][1]:
        inputs["left"][1] = False
        mouse_pos = pygame.mouse.get_pos()
        for button in buttons:
            if button["rect"].collidepoint(mouse_pos):
                if button["action"] == "toggle_draw":
                    draw = not draw
                    button["state"] = draw
                    print("draw: ", draw)
                elif button["action"] == "toggle_break":
                    break_state = not break_state
                    button["state"] = break_state
                    print("break: ", break_state)
                elif button["action"] == "increase_speed":
                    speed *= 2
                    print("speed increased to: ", speed)
                elif button["action"] == "decrease_speed":
                    speed /= 2
                    print("speed decreased to: ", speed)
    if (speed > 50):
        speed = 32
    for button in buttons:
        pygame.draw.rect(window, DARK_GRAY if button.get("state", False) else (200, 200, 200), button["rect"])
        pygame.draw.rect(window, BLACK, button["rect"], 2)
        text = font.render(button["label"], True, LIGHT_GRAY if button.get("state", False) else BLACK)
        text_rect = text.get_rect(center=button["rect"].center)
        window.blit(text, text_rect)
    return draw, break_state, speed

