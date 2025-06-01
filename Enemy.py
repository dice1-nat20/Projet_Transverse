##########################################
##       Immacolato Almha               ##
##       Chen Lana                      ##
##       Gbaguidi Bryan                 ##
##       Tchana Watat Emmanuelle        ##
##       Bertaina--David Sacha          ##
##       Projet : Transverse            ##
##########################################

import pygame

from constantes import ENNEMI_SPRITE, groundLvL


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):   # là où le joueur prends keys en param (les touches préssées), ici il prend direct des coordonnées
        super().__init__()  # comme pour le joueur, on crée une sorte d'object pour le sprite
        self.image = ENNEMI_SPRITE
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.bottom = groundLvL
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction * 4
        self.move_counter += 0.5
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1
