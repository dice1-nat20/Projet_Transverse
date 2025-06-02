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
        self.poids = 1.0

    def update(self, keys):
        if not self.isJumping:
            # mouvements au sol
            if keys[pygame.K_q]:
                self.vel_x = -VITESSE_DEPLACEMENT
            elif keys[pygame.K_d]:
                self.vel_x = VITESSE_DEPLACEMENT
            # prise en compte de la friction
            else:
                if self.vel_x > 0:
                    self.vel_x -= FRICTION
                    if self.vel_x < 0:
                        self.vel_x = 0
                elif self.vel_x < 0:
                    self.vel_x += FRICTION
                    if self.vel_x > 0:
                        self.vel_x = 0

            # limite de vitesse (par rapport à l'inertie)
            if self.vel_x > VITESSE_MAX:
                self.vel_x = VITESSE_MAX
            if self.vel_x < -VITESSE_MAX:
                self.vel_x = -VITESSE_MAX

            self.rect.x += self.vel_x

            # saut
            if keys[pygame.K_SPACE] and not self.isJumping:
                self.vel_y = -FORCE_DU_SAUT
                self.isJumping = True
                self.t = 0
                self.x0 = self.rect.x
                self.y0 = self.rect.y

        else:
            self.rect.x += self.vel_x
            self.vel_y += self.poids
            self.rect.y += self.vel_y

            # gestion collision avec le sol
            if self.rect.bottom >= SCREEN_HEIGHT-50:
                self.rect.bottom = SCREEN_HEIGHT - 50
                #self.vel_x = 0
                self.vel_y = 0
                self.isJumping = False
