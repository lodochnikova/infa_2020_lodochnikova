import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
# draw emotoicon shape
circle(screen, (255, 255, 0), (200, 175), 150)
circle(screen, (0, 0, 0), (200, 175), 150, 1)
# draw eyes
circle(screen, (0, 0, 0), (270, 150), 30, 3)
circle(screen, (255, 0, 0), (270, 150), 30)
circle(screen, (0, 0, 0), (130, 150), 40, 3)
circle(screen, (255, 0, 0), (130, 150), 40)
# draw pupils
circle(screen, (0, 0, 0), (270, 150), 10)
circle(screen, (0, 0, 0), (130, 150), 12)
# draw eyebrows
polygon(screen, (0, 0, 0), [(180,140), (185,130),
                               (70,70), (65,80)])
polygon(screen, (0, 0, 0), [(240,130), (235,120),
                                (330,90), (335, 100)])
# draw mouth
polygon(screen, (0, 0, 0), [(130, 270), (130, 280),
                                (280,280), (280, 270)])
                                
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
