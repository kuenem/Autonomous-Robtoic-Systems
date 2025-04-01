import pygame 
import math
import time

from const import *
import robot

WIN = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Robot Simulation")
FPS = 60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    WIN.fill(WHITE)
    pygame.display.update()
    time.sleep(1/FPS)