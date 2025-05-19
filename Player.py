##########################################
##       Immacolato Almha               ##
##       Chen Lana                      ##
##       Gbaguidi Bryan                 ##
##       Tchana Watat Emmanuelle        ##
##       Bertaina--David Sacha          ##
##       Projet : Transverse            ##
##########################################

import pygame
from pygame.draw_py import draw_polygon
from pygame.locals import *
import pygame, sys
from math import sin, cos
from partiePhysique import *


class Player:
    def __init__(self,sprite,x,y,masse):
        self.playerSpr = pygame.image.load(sprite)
        # position initiale
        self.playerX = x
        self.playerY = y
        # caractéristiques pour la partie physique
        self.masse = masse
        self.yChange = 0 # changement lié à la gravité
        self.vitesse = 0

    def drawPlayer(self,x,y):
        self.playerX = x
        self.playerY = y
        self.move(x,y)

    def playerJump(self):
        a = 45 # par une déduction triviale # angle de la courbe, modifiable
        y0 = self.playerY   # y de départ
        y = y0 - 1
        v0 = self.vitesse   # viitesse de départ
        t = 0   # temps au début
        x = 0   # x de départ
        positions = []  # les postions qui seront retournées

        while y <= y0:
            y = (-1/2) * constanteDeGravitation * t**2 + (v0 * sin(a)) * t + y0
            x += 1
            t += 5
            positions.append((x,y))
        return positions

    def playerGoRight(self):
        return
    def playerGoLeft(self):
        return
    def playerMovements(self,window):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            positions = self.playerJump()
        elif keys[pygame.K_d]:
            self.playerGoRight()
        elif keys[pygame.K_q]:
            self.playerGoLeft()


