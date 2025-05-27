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


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = player_img
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT - 150
        self.vel_y = 0
        self.on_ground = False

    def update(self, keys):
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] and self.on_ground:
            dx = -5
        if keys[pygame.K_RIGHT] and self.on_ground:
            dx = 5

        # saut
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -25
            self.on_ground = False

        # gravité
        self.vel_y += 0.8
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # collisions
        if self.rect.bottom + dy >= SCREEN_HEIGHT - 50:
            dy = SCREEN_HEIGHT - 50 - self.rect.bottom
            self.on_ground = True
            self.vel_y = 0

        # mouvements
        self.rect.x += dx
        self.rect.y += dy

class pla:
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
        v0 = self.vitesse   # vitesse de départ
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


