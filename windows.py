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
import pygame, sys



background_color = (0,255,0)
width = 1000
heigh = 800


screen = pygame.display.set_mode((width,heigh))
pygame.display.set_caption("test_window_2")
screen.fill(background_color)
pygame.display.flip()

