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
from joueur import *


background_color = (0,0,255)
width = 1000
heigh = 750
playerSprite = 'images&otherFiles/placeHolderPlayer.png'
running = True

screen = pygame.display.set_mode((width,heigh))
pygame.display.set_caption("test_window_2")
screen.fill(background_color)
pygame.display.flip()

while running:
    Player.drawPlayer(playerSprite,screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
    pygame.display.update()
pygame.quit()


