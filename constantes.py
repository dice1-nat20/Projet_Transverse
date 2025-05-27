import pygame

# constantes

# fenêtre
SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
FPS = 60
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# sprites
PLAYER_SPRITE = pygame.image.load("images&otherFiles/placeHolderPlayer.png")
ENNEMI_SPRITE = pygame.image.load("images&otherFiles/placeHolderOther.png")

# joueurs
PLAYER_X = 50
PLAYER_Y = 50
GRAVITE = 1
FORCE_DU_SAUT = 25
VITESSE_DEPLACEMENT = 5
groundLvL = SCREEN_HEIGHT - PLAYER_Y  # quand on voudra faire une plateforme, on ferra changer la valeur de SOL
