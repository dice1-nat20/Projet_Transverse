


##########################################
##       Immacolato Almha               ##
##       Chen Lana                      ##
##       Gbaguidi Bryan                 ##
##       Tchana Watat Emmanuelle        ##
##       Bertaina--David Sacha          ##
##       Projet : Transverse            ##
##########################################

import pygame

class Ennemi:
    def __init__(self, x_centre, y, width, height, speed, amplitude):
        self.x_centre = x_centre
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.amplitude = amplitude
        self.x = x_centre - amplitude

    def move_ennemi(self):
        self.x += self.speed
        if self.x <= self.x_centre - self.amplitude or self.x + self.width >= self.x_centre + self.amplitude:
            self.speed *= -1

    def draw_ennemi(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def get_rect(self):
        # Cette méthode retourne le rectangle de l'ennemi pour détecter la collision
        return pygame.Rect(self.x, self.y, self.width, self.height)
