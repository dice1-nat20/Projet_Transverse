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
from math import sin, cos, tan
from partiePhysique import *


class Player:
    def __init__(self,sprite,x,y,masse,jf):
        self.playerSpr = pygame.image.load(sprite)
        # position initiale
        self.playerX = x
        self.playerY = y
        # caractéristiques pour la partie physique
        self.masse = masse
        self.jumpForce = jf # la force (en Newton ?) qu'il deploit pour sauter
        self.yChange = 0 # changement lié à la gravité
        self.vitesse = 0

    def drawPlayer(self,window):
        window.blit(self.playerSpr,(self.playerX,self.playerY))

    def playerJump(self):
        a = 45 # la déduction est triviale
        y0 = self.player.playerY
        v0 = self.player.vitesse
        t = 1
        y = y0 + 1

        while y != y0:
            y = (-1/2) * constanteDeGravitation * t**2 + (v0 * sin(a)) * t + y0
            self.playerY = y

    def playerGoRight(self):
        return
    def playerGoLeft(self):
        return
    def playerMovements(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.playerJump(self)
        elif keys[pygame.K_d]:
            self.playerGoRight(self)
        elif keys[pygame.K_q]:
            self.playerGoLeft(self)


