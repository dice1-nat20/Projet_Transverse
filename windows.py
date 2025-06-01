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
from constantes import SCREEN_HEIGHT, SCREEN_WIDTH, backgroundIMG


# fenêtre
worldShift = 0
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monic")
clock = pygame.time.Clock()

def drawWindow(player,enemies,plateformes, backgroundX):
    backgroundW = backgroundIMG.get_width()
    tiles = (SCREEN_WIDTH//backgroundW)+2

    for i in range(tiles):
        screen.blit(backgroundIMG,(i*backgroundW-(backgroundX%backgroundW),0))

    for plt in plateformes:
        pygame.draw.rect(screen,(100,100,100),(plt['x'],plt['y'],plt['width'],10))

    for enemi in enemies:
        screen.blit(enemi.image, (enemi.rect.x, enemi.rect.y))

    screen.blit(player.image,(player.rect.x,player.rect.y))
    pygame.display.flip()