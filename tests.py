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
from windows import *


playerSprite = 'images&otherFiles/placeHolderPlayer.png'
running = True

while running:
    joueur = Player(playerSprite,250,650,80,10)
    Player.drawPlayer(joueur,screen)
    Player.playerMovements()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
    pygame.display.update()

pygame.quit()