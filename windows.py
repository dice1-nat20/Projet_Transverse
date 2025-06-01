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
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Monic")
clock = pygame.time.Clock()

def drawWindow(player,enemies,plateformes, backgroundX,scroll,pointsDeLaTrajectoire):
    if backgroundIMG:
        backgroundLargeur = backgroundIMG.get_width()
        tiles = (SCREEN_WIDTH//backgroundLargeur)+2
        for i in range(tiles):
            screen.blit(backgroundIMG,(i*backgroundLargeur-(scroll % backgroundLargeur),0))
    else:
        screen.file((255,255,255))

    for x,y in pointsDeLaTrajectoire:
        pygame.draw.circle(screen,(0,255,0),(x - scroll,y),3)

    for plt in plateformes:
        pygame.draw.rect(screen,(100,100,100),(plt['x']-scroll,plt['y'],plt['width'],10))

    for enemi in enemies:
        screen.blit(enemi.image, (enemi.rect.x - scroll, enemi.rect.y))

    screen.blit(player.image,(player.rect.x,player.rect.y))
    pygame.display.flip()