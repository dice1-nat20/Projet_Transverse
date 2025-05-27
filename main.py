import pygame
import sys
from pygame.locals import *
import menus

background_color = (0,0,255)
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("test-window")
screen.fill(background_color)
pygame.display.flip()
running = True

while running:
    for event in pygame.event.get():
        menus.displayGameName(screen, 250, 250)
        if event.type == pygame.QUIT:
            running = False

