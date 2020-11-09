import pygame
from pygame.draw import *

def draw_background (screen, x, y, bottom_color, top_color, y_divide):
	rect(screen, top_color, (0, 0, x, y_divide))
	rect(screen, bottom_color, (0, y_divide, x, y - y_divide))
def draw_window (screen, x_window, y_window, width_window, height_window, frame_color, glass_color):
	rect(screen, frame_color, (x_window, y_window, width_window, height_window))
	rect(screen, glass_color, (x_window + 10, y_window + 10, (width_window - 30) / 2, (height_window - 30) / 4))
	rect(screen, glass_color, (x_window + 20 + (width_window - 30) / 2, y_window + 10, (width_window - 30) / 2, (height_window - 30) / 4))
	rect(screen, glass_color, (x_window + 10, y_window + 20 + (height_window - 30) / 4, (width_window - 30) / 2, 3 * (height_window - 30) / 4))
	rect(screen, glass_color, (x_window + 20 + (width_window - 30) / 2, y_window + 20 + (height_window - 30) / 4, (width_window - 30) / 2, 3 * (height_window - 30) / 4))
def draw_tale (x, y, width, height, cat_color, right):
	surface = pygame.Surface((width / 2, height / 3), pygame.SRCALPHA)
	ellipse = pygame.draw.ellipse(surface, BLACK, (0, 0, width / 2, height / 3))
	ellipse = pygame.draw.ellipse(surface, cat_color, (1, 1, width / 2 - 2, height / 3 - 2))
	surface = pygame.transform.rotate(surface, -15)
	if right:
		surface = pygame.transform.flip(surface, True, False)
		screen.blit(surface,(SCREEN_X - x - width, y + height / 9))
	else:
		screen.blit(surface,(x + width / 2, y + height / 9))
	pygame.display.update()
def draw_body (x, y, width, height, cat_color, right):
	surface2 = pygame.Surface((600, 800), pygame.SRCALPHA)
	ellipse = pygame.draw.ellipse(surface2, BLACK, (x + width / 7 - 1, y - 1, 2 * width / 3 + 2, 2 * height / 3 + 2))
	ellipse = pygame.draw.ellipse(surface2, cat_color, (x + width / 7, y, 2 * width / 3, 2 * height / 3))
	ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 4 * width / 50 - 1, y + 2 * height / 15 - 1, 2.5 * width / 25 + 2, 2.5 * height / 5 + 2))
	ellipse = pygame.draw.ellipse(surface2, cat_color, (x + 4 * width / 50, y + 2 * height / 15, 2.5 * width / 25, 2.5 * height / 5))
	ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 5 * width / 25 - 1, y + 11 * height / 21 - 1, 4 * width / 25 + 2, 4 * height / 21 + 2))
	ellipse = pygame.draw.ellipse(surface2, cat_color, (x + 5 * width / 25, y + 11 * height / 21, 4 * width / 25, 4 * height / 21))
	ellipse = pygame.draw.ellipse(surface2, BLACK, (x + width / 50 - 1, y + height / 22 - 1, 11 * width / 50 + 2, 11 * width / 50 + 2))
	ellipse = pygame.draw.ellipse(surface2, cat_color, (x + width / 50, y + height / 22, 11 * width / 50, 11 * width / 50))
	ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 30 * width / 50 - 1, y + 7 * height / 21 - 1, 9 * width / 50 + 2, 10 * height / 21 + 2))
	ellipse = pygame.draw.ellipse(surface2, cat_color, (x + 30 * width / 50, y + 7 * height / 21, 9 * width / 50, 10 * height / 21))
	ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 36 * width / 50 - 1, y + 14 * height / 21 - 1, 3 * width / 50 + 2, 7 * height / 21 + 2))
	ellipse = pygame.draw.ellipse(surface2, cat_color, (x + 36 * width / 50, y + 14 * height / 21, 3 * width / 50, 7 * height / 21))
	if right:
		surface2 = pygame.transform.flip(surface2, True, False)
	screen.blit(surface2,(0, 0))
	pygame.display.update()
def draw_ears (x, y, width, height, ear_color, cat_color, right):
	surface2 = pygame.Surface((600, 800), pygame.SRCALPHA)
	polygon = pygame.draw.polygon(surface2, BLACK, ((x + 2 * width / 50, y + 5 * height / 21 + 1), 
													(x + 5 * width / 50 + 2, y + 2 * height / 21 - 1), 
													(x - 1, y + 1 * height / 21 - 1)))
	polygon = pygame.draw.polygon(surface2, cat_color, ((x + 2 * width / 50, y + 5 * height / 21), 
														(x + 5 * width / 50, y + 2 * height / 21), 
														(x, y + 1 * height / 21)))
	polygon = pygame.draw.polygon(surface2, BLACK, ((x + 10 * width / 50, y + 5 * height / 21 + 2), 
													(x + 7 * width / 50 - 2, y + 2 * height / 21 - 1), 
													(x + 12 * width / 50 + 1, y + 1 * height / 21 - 1)))
	polygon = pygame.draw.polygon(surface2, cat_color, ((x + 10 * width / 50, y + 5 * height / 21), 
														(x + 7 * width / 50, y + 2 * height / 21), 
														(x + 12 * width / 50, y + 1 * height / 21)))

	polygon = pygame.draw.polygon(surface2, BLACK, ((x + 2.25 * width / 50, y + 4 * height / 21 + 1), 
													(x + 4 * width / 50 + 1, y + 2.25 * height / 21), 
													(x + width / 60 - 1, y + 1.5 * height / 21 - 1)))
	polygon = pygame.draw.polygon(surface2, ear_color, ((x + 2.25 * width / 50, y + 4 * height / 21), 
														(x + 4 * width / 50, y + 2.25 * height / 21), 
														(x + width / 60, y + 1.5 * height / 21)))
	polygon = pygame.draw.polygon(surface2, BLACK, ((x + 9.85 * width / 50, y + 4.125 * height / 21 + 1), 
													(x + 8 * width / 50 - 2, y + 2.35 * height / 21 - 1), 
													(x + 11.25 * width / 50 + 1, y + 1.5 * height / 21 - 1)))
	polygon = pygame.draw.polygon(surface2, ear_color, ((x + 9.85 * width / 50, y + 4.125 * height / 21), 
														(x + 8 * width / 50, y + 2.35 * height / 21), 
														(x + 11.25 * width / 50, y + 1.5 * height / 21)))
	if right:
		surface2 = pygame.transform.flip(surface2, True, False)
	screen.blit(surface2,(0, 0))
	pygame.display.update()
def draw_eyes(x, y, width, height, eye_color, cat_color, look, right):
	surface2 = pygame.Surface((600, 800), pygame.SRCALPHA)
	ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 2.5 * width / 50 - 1, y + 5 * height / 22 - 1, 3 * width / 50 + 2, 3 * width / 50 + 2))
	ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 6.5 * width / 50 - 1, y + 5 * height / 22 - 1, 3 * width / 50 + 2, 3 * width / 50 + 2))
	ellipse = pygame.draw.ellipse(surface2, eye_color, (x + 2.5 * width / 50, y + 5 * height / 22, 3 * width / 50, 3 * width / 50))
	ellipse = pygame.draw.ellipse(surface2, eye_color, (x + 6.5 * width / 50, y + 5 * height / 22, 3 * width / 50, 3 * width / 50))

	if look:
		ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 4.25 * width / 50, y + 5.35 * height / 22, 0.5 * width / 50, 2.25 * width / 50))
		ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 8.25 * width / 50, y + 5.35 * height / 22, 0.5 * width / 50, 2.25 * width / 50))
	else:
		ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 3.25 * width / 50, y + 5.26 * height / 22, 0.5 * width / 50, 2.45 * width / 50))
		ellipse = pygame.draw.ellipse(surface2, BLACK, (x + 7.25 * width / 50, y + 5.26 * height / 22, 0.5 * width / 50, 2.45 * width / 50))
	if right:
		surface2 = pygame.transform.flip(surface2, True, False)
	screen.blit(surface2,(0, 0))
	pygame.display.update()
def draw_glare(x, y, width, height, look, right):
	surface2 = pygame.Surface(( 3 * width / 50, 3 * width / 50), pygame.SRCALPHA)
	ellipse = pygame.draw.ellipse(surface2, WHITE, ( 0 * width / 50,  0, 1.5 * width / 50, 0.5 * width / 50))
	surface2 = pygame.transform.rotate(surface2, -60)
	if right:
		screen.blit(surface2,(SCREEN_X - x - 5 * width / 50, y))
		surface2 = pygame.transform.flip(surface2, True, False)
	else:
		screen.blit(surface2,(x, y))
	pygame.display.update()
def draw_nose(x, y, width, height, ear_color, right):
	surface2 = pygame.Surface((3 * width / 50, 3 * width / 50), pygame.SRCALPHA)
	polygon = pygame.draw.polygon(surface2, BLACK, ((0, 0), (2 + 1 * width / 50, 0), (1 + 0.5 * width / 50, 2 + 1 * height / 22)))
	polygon = pygame.draw.polygon(surface2, ear_color, ((1, 1), (1 + 1 * width / 50, 1), (1 + 0.5 * width / 50, 1 + 1 * height / 22)))
	if right:
		screen.blit(surface2,(SCREEN_X - x - 1.5 * width / 50, y))
		surface2 = pygame.transform.flip(surface2, True, False)
	else:
		screen.blit(surface2,(x, y))
	pygame.display.update()
def draw_mouth(x, y, width, height, right):
	surface2 = pygame.Surface((6 * width / 50, 6 * width / 50), pygame.SRCALPHA)
	arc = pygame.draw.arc(surface2, BLACK, (0, 0, 2 * width / 50, 2 * width / 50), -3, 0)
	if right:
		screen.blit(surface2,(SCREEN_X - x - 1.5 * width / 50, y))
		surface2 = pygame.transform.flip(surface2, True, False)
	else:
		screen.blit(surface2,(x, y))
	pygame.display.update()
def draw_whiskers(x, y, width, height, right):
	surface2 = pygame.Surface((42 * width / 50, 42 * width / 50), pygame.SRCALPHA)
	arc = pygame.draw.arc(surface2, BLACK, (0, 0, 10 * width / 50, 5 * width / 50), 1.1, 2.5)
	arc = pygame.draw.arc(surface2, BLACK, (0, 0.5 * height / 22, 15 * width / 50, 10 * width / 50), 1.6, 2.5)
	arc = pygame.draw.arc(surface2, BLACK, (0, 1 * height / 22, 15 * width / 50, 17 * width / 50), 1.6, 2.5)
	arc = pygame.draw.arc(surface2, BLACK, (3 * width / 50, 0.125 * height / 22, 15 * width / 50, 5 * width / 50), 0.25, 1.3)
	arc = pygame.draw.arc(surface2, BLACK, (3 * width / 50, 0.25 * height / 22, 15 * width / 50, 8 * width / 50), 0.25, 1.3)
	arc = pygame.draw.arc(surface2, BLACK, (3 * width / 50, 0.5 * height / 22, 15 * width / 50, 12 * width / 50), 0.5, 1.3)
	if right:
		surface2 = pygame.transform.flip(surface2, True, False)
		screen.blit(surface2,(SCREEN_X - x - 40.5 * width / 50, y))
	else:
		screen.blit(surface2,(x, y))
	pygame.display.update()
def draw_clew(x, y, radius, right):
	surface2 = pygame.Surface((4 * radius, 2 * radius), pygame.SRCALPHA)
	ellipse = pygame.draw.ellipse(surface2, BLACK, (0, 0, 2 * radius, 2 * radius))
	ellipse = pygame.draw.ellipse(surface2, GREY, (1, 1, 2 * radius - 2, 2 * radius - 2))
	arc = pygame.draw.arc(surface2, BLACK, (-0.25 * radius, radius / 4, 2 * radius, 2 * radius), 0.5, 1.5)
	arc = pygame.draw.arc(surface2, BLACK, (-0.25 * radius, radius / 2, 2 * radius, 2 * radius), 0.5, 1.7)
	arc = pygame.draw.arc(surface2, BLACK, (-0.25 * radius, 3 * radius / 4, 2 * radius, 2 * radius), 0.5, 1.9)
	arc = pygame.draw.arc(surface2, BLACK, (0.5 * radius, radius / 2, 2 * radius, 2 * radius), 2.5, 3.3)
	arc = pygame.draw.arc(surface2, BLACK, (0.75 * radius, radius / 2, 2 * radius, 2 * radius), 2.5, 3.5)
	arc = pygame.draw.arc(surface2, BLACK, (1 * radius, radius / 2, 2 * radius, 2 * radius), 2.6, 3.5)

	arc = pygame.draw.arc(surface2, GREY, (0.65 * radius, 1.5 * radius, 8 * radius, 2 * radius), 2.1, 3.9)
	arc = pygame.draw.arc(surface2, GREY, (2 * radius, 1.58 * radius, 2 * radius, 2 * radius), 0, 1.97)
	if right:
		surface2 = pygame.transform.flip(surface2, True, False)
		screen.blit(surface2,(SCREEN_X - x - 4 * radius, y))
	else:
		screen.blit(surface2,(x, y))
	pygame.display.update()
def draw_cat (x, y, size, cat_color, ear_color, eye_color, look, right):
	#look = True if cat is looking to the right
	#right = True if cat`s head is on the right
	if right:
		look = not(look)
	width = size * 4.25;
	height = size * 2;
	surface2 = pygame.Surface((600, 800), pygame.SRCALPHA)
	draw_tale(x, y, width, height, cat_color, right)
	draw_body(x, y, width, height, cat_color, right)
	draw_ears(x, y, width, height, ear_color, cat_color, right)
	draw_eyes(x, y, width, height, eye_color, cat_color, look, right)
	draw_glare(x + 1 * width / 50, y + 5 * height / 22, width, height, look, right)
	draw_glare(x + 5 * width / 50, y + 5 * height / 22, width, height, look, right)
	draw_nose(x + 5 * width / 50, y + 7.35 * height / 22, width, height, ear_color, right)
	draw_mouth(x + 4 * width / 50, y + 7.35 * height / 22, width, height, right)
	draw_mouth(x + 6 * width / 50, y + 7.35 * height / 22, width, height, right)
	draw_whiskers(x - 3 * width / 50, y + 7.65 * height / 22, width, height, right)
BROWN_LIGHT = (101, 67, 33)
BROWN_DARK = (52, 28, 2)
ORANGE_DARK = (205, 87, 0)
ORANGE_LIGHT = (255, 162, 106)
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
draw_window(screen, 380, 40, 200, 250,  BLUE_LIGHT, BLUE_DARK)
draw_window(screen, 160, 40, 200, 250, BLUE_LIGHT, BLUE_DARK)
draw_window(screen, -60, 40, 200, 250, BLUE_LIGHT, BLUE_DARK)
draw_cat(300, 400, 60, ORANGE_DARK, ORANGE_LIGHT, GREEN, True, False)
draw_cat(450, 400, 30, ORANGE_DARK, ORANGE_LIGHT, GREEN, False, True)
draw_clew(350, 380, 30, True)
draw_cat(350, 500, 60, GREY, ORANGE_LIGHT, BLUE_LIGHT, True, True)
draw_clew(350, 500, 30, False)
draw_cat(50, 550, 30, ORANGE_DARK, ORANGE_LIGHT, GREEN, False, True)
draw_clew(250, 550, 50, False)
draw_clew(460, 630, 50, False)
draw_cat(330, 650, 30, ORANGE_DARK, ORANGE_LIGHT, GREEN, True, False)
draw_cat(470, 740, 30, GREY, ORANGE_LIGHT, BLUE_LIGHT, False, False)
draw_clew(200, 700, 30, True)
draw_clew(320, 650, 60, True)
draw_cat(470, 725, 30, GREY, ORANGE_LIGHT, BLUE_LIGHT, True, True)
draw_clew(450, 650, 30, True)

pygame.display.update()
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
