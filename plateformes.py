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


class Plateforme:
    def __innit__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load('images&otherFiles/plateforme.png')
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def platformHitbox(self):
        return self.rect, self.rect.size
