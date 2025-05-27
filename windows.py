##########################################
##       Immacolato Almha               ##
##       Chen Lana                      ##
##       Gbaguidi Bryan                 ##
##       Tchana Watat Emmanuelle        ##
##       Bertaina--David Sacha          ##
##       Projet : Transverse            ##
##########################################

import pygame
from pygame.locals import *
import pygame

# constantes
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# fenêtre
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monic")
clock = pygame.time.Clock()
