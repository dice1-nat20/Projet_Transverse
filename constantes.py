import pygame


# fenêtre
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 800
FPS = 60
backgroundIMG = pygame.image.load("images&otherFiles/jk.png")
GREEN = (0, 255, 0)
DEAD_ZONE_G = SCREEN_WIDTH // 4
DEAD_ZONE_D = SCREEN_WIDTH * 3 // 4

# sprites
PLAYER_SPRITE = pygame.image.load("images&otherFiles/placeHolderPlayer.png")
ENNEMI_SPRITE = pygame.image.load("images&otherFiles/placeHolderOther.png")

# joueurs
PLAYER_X = 50
PLAYER_Y = 50

# constantes
GRAVITE = 1
FORCE_DU_SAUT = 21
VITESSE_DEPLACEMENT = 4
VITESSE_MAX = 20
FRICTION = 0.3
groundLvL = SCREEN_HEIGHT - PLAYER_Y  # quand on voudra faire une plateforme, on ferra changer la valeur de SOL
