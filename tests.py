##########################################
##       Immacolato Almha               ##
##       Chen Lana                      ##
##       Gbaguidi Bryan                 ##
##       Tchana Watat Emmanuelle        ##
##       Bertaina--David Sacha          ##
##       Projet : Transverse            ##
##########################################

import pygame
from pygame.draw_py import draw_pixel
from pygame.locals import *
import pygame, sys
from Player import Player
from windows import screen
from time import sleep


playerSprite = 'images&otherFiles/placeHolderPlayer.png'
running = True

while running:
    x = 250
    y = 500

    joueur = Player(playerSprite,x,y,80)
    screen.blit(joueur.playerSpr,(x,y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            running = False
        elif event.type == pygame.K_SPACE:
            pos = joueur.playerJump()
            for i in pos:
                joueur.playerX = i[0]
                joueur.playerY = i[1]
                joueur.drawPlayer(joueur.playerX,joueur.playerY)
                pygame.display.update()
                pygame.display.flip()
                sleep(10)
                i += 1
    pygame.display.update()

pygame.quit()