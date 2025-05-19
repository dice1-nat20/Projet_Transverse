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


class Player:
    def __init__(self,sprite):
        player_img = pygame.image.load(sprite)
        playerX, playerY = 100,500 #position initiale
    def drawPlayer(self,window):
        window.blit(self.player_img,(self.playerX,self.playerY))


