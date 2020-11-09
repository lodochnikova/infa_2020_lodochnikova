import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 20
HEIGHT = 900
WIDTH = 1200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
res = 0
time = 100

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
n = 5
def new_ellipse():
	global x_e, y_e, r_e
	x_e = randint(100,1100)
	y_e = randint(100,800)
	r_e = randint(30,50)
	vx_e = randint(-10, 10)
	vy_e = randint(-10, 10)
	color_e = COLORS[randint(0, 5)]
	return x_e, y_e, r_e, color_e, vx_e, vy_e

def new_ball():
	global x, y, r
	x = randint(100,1100)
	y = randint(100,800)
	r = randint(30,50)
	vx = randint(-10, 10)
	vy = randint(-10, 10)
	color = COLORS[randint(0, 5)]
	return x, y, r, color, vx, vy

def draw_ellipse(ellipse):
	x, y, r, color, vx, vy = ellipse
	circle(screen, color, (x, y), r)
	circle(screen, (255, 255, 255), (x, y), r-5)
	
def draw_ball(ball):
	x, y, r, color, vx, vy = ball
	circle(screen, color, (x, y), r)

def move_ellipse(ellipse):
	x, y, r, color, vx, vy = ellipse
	x+=vx
	y+=vy
	
	if x<=0 + r or x >= WIDTH - r:
		vx*=-1
	if y<=0 + r or y >= HEIGHT - r:
		vy*=-1
		
	return x, y, r, color, vx, vy

def move_ball(ball):
	x, y, r, color, vx, vy = ball
	x+=vx
	y+=vy
	
	if x<=0 + r or x >= WIDTH - r:
		vx*=-1
	if y<=0 + r or y >= HEIGHT - r:
		vy*=-1
		
	return x, y, r, color, vx, vy

def is_clicked(event, ball):
	x, y, r, color, vx, vy = ball
	ex, ey = event.pos
	for i in range(n):
		if ((ex - x) ** 2 + (ey - y) ** 2 <= r ** 2):
			return True
	return False

def check_time(time):
	if time <= 0:
		add_res("Results.txt", res)
		pygame.quit()
		exit()
	
def add_res(input_filename, res):
    reses = []
    with open(input_filename) as input_file:
        for line in input_file:
            reses.append(int(line))
    reses.append(res)
    reses.sort(reverse=True)
    with open(input_filename, 'w') as out_file:
        for r in reses[:10]:
            print("%d" % (r), file=out_file)
            
pygame.display.update()
clock = pygame.time.Clock()
finished = False
balls = []
ellipses = []
for i in range(n):
	balls.append(new_ball())
	ellipses.append(new_ellipse())

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True
		elif event.type == pygame.MOUSEBUTTONDOWN:
			for i, ball in enumerate(balls):
				if is_clicked(event, ball):	
					res += 1
					print(res)
					balls[i] = new_ball()
			for i, ellipse in enumerate(ellipses):
				if is_clicked(event, ellipse):	
					res += 5
					print(res)
					ellipses[i] = new_ellipse()
	for i, ball in enumerate(balls):
		time -= 1
		balls[i] = move_ball(ball)
		draw_ball(ball)
		check_time(time)
	for i, ellipse in enumerate(ellipses):
		time -= 1
		ellipses[i] = move_ellipse(ellipse)
		draw_ellipse(ellipse)
		check_time(time)
	pygame.display.update()
	screen.fill(BLACK)

pygame.quit()
