
import pygame
from pygame.draw import *

def draw_background (screen, x, y, bottom_color, top_color, y_divide):
	rect(screen, top_color, (0, 0, x, y_divide))
	rect(screen, bottom_color, (0, y_divide, x, y-y_divide))
def draw_window (screen, x_window, y_window, width_window, height_window, frame_color, glass_color):
	rect(screen, frame_color, (x_window, y_window, width_window, height_window))
	#
ORANGE_DARK = (205, 87, 0)
ORANGE_LIGHT = (255, 162, 106)
BROWN_LIGHT = (101, 67, 33)
BROWN_DARK = (52, 28, 2)
GREY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE_LIGHT = (135, 206, 250)
BLUE_DARK = (0, 191, 255)
SCREEN_X = 600
SCREEN_Y = 800
FPS = 30

pygame.init()
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
draw_background(screen, SCREEN_X, SCREEN_Y, BROWN_LIGHT, BROWN_DARK, 350)

                                
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
