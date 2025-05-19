import pygame

class Ennemi:
    def __init__(self, x, y, width, height, speed, screen_width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.screen_width = screen_width

    def move_ennemi(self):
        self.x += self.speed
        if self.x <= 0 or self.x + self.width >= self.screen_width:
            self.speed *= -1

    def draw_ennemi(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))

