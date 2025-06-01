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


class Plateform:
    def __init__(self,x,y,width):
        self.x = x
        self.y = y
        self.width = width
        self.height = 10
        self.color = (100,100,100)
        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)

    def update(self,scroll):
        self.rect.x = self.x - scroll
        self.rect.y = self.y

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
