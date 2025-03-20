import pygame
from pygame.locals import *
import pygame, sys


background_color = (0,0,255)
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("test-window")
screen.fill(background_color)
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

