import pygame


def displayGameName(screen, x, y):
    title = pygame.image.load("Title.png", 'r')
    screen.blit(title, (x, y))


def displayNames(screen, x, y):
    title = pygame.image.load("Names.png", 'r')
    screen.blit(title, (x, y))
