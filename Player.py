##########################################
##       Immacolato Almha               ##
##       Chen Lana                      ##
##       Gbaguidi Bryan                 ##
##       Tchana Watat Emmanuelle        ##
##       Bertaina--David Sacha          ##
##       Projet : Transverse            ##
##########################################

import pygame
import pygame, sys
from constantes import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # ça créer un autre objet pour le sprite à venir
        self.image = PLAYER_SPRITE
        self.rect = self.image.get_rect()  # le rectangle du sprite (sa hitbox)
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT
        self.rect.bottom = groundLvL
        self.vel_x = 0  # la velocité en x
        self.vel_y = 0  # la velocité en y
        self.a = 0
        self.t = 0
        self.isJumping = False
        self.x0 = self.rect.x
        self.y0 = self.rect.y

    def update(self, keys):
        if not self.isJumping:
            # mouvements
            self.vel_x = 0
            if keys[pygame.K_q]:
                self.vel_x = -VITESSE_DEPLACEMENT
            elif keys[pygame.K_d]:
                self.vel_x = VITESSE_DEPLACEMENT
            self.rect.x += self.vel_x

            # saut
            if keys[pygame.K_SPACE] and not self.isJumping:
                self.vel_y = -FORCE_DU_SAUT
                self.isJumping = True
                self.t = 0
                self.x0 = self.rect.x
                self.y0 = self.rect.y
        else:
            self.t += 1  # / FPS
            newX = self.vel_x * self.t
            newY = self.vel_y * self.t + 0.5 * GRAVITE * (self.t ** 2)
            self.rect.x = self.x0 + newX
            self.rect.y = self.y0 + newY

            # gestion collision avec le sol
            if self.rect.bottom >= groundLvL:
                self.rect.bottom = groundLvL
                self.isJumping = False
                self.vel_x = 0
                self.vel_y = 0
