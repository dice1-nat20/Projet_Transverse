import pygame


class Plateforme:
    def __innit__(self):
        self.x = 0
        self.y = 0
        self.image = image.load('plateforme.png')
        self.rect = self.image.get_rect()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def platformHitbox(self):
        return self.rect.topleft, self.rect.size
