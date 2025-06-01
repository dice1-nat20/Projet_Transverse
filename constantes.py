import pygame


# fenêtre
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
FPS = 60
backgroundIMG = pygame.image.load("images&otherFiles/jk.png")
GREEN = (0, 255, 0)
VITESSE_DE_SCROLL = 2.5
VICTORY_ZONE = pygame.Rect(2000,0, 100, SCREEN_HEIGHT)

# sprites
PLAYER_SPRITE = pygame.image.load("images&otherFiles/placeHolderPlayer.png")
ENNEMI_SPRITE = pygame.image.load("images&otherFiles/placeHolderOther.png")

# joueurs
PLAYER_X = 50
PLAYER_Y = 50

# constantes
FORCE_DU_SAUT = 21
VITESSE_DEPLACEMENT = 3
VITESSE_MAX = 20
FRICTION = 0.3
groundLvL = SCREEN_HEIGHT - 50
