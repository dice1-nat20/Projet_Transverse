##########################################
##       Immacolato Almha               ##
##       Chen Lana                      ##
##       Gbaguidi Bryan                 ##
##       Tchana Watat Emmanuelle        ##
##       Bertaina--David Sacha          ##
##       Projet : Transverse            ##
##########################################
import sys

from Player import *
from Enemy import *
from windows import *
import time


pygame.init()
clock = pygame.time.Clock()

decalageDuBackgroundEnX = 0

player = Player()
#player_group = pygame.sprite.Group()
#player_group.add(player)

enemies = [Enemy(500,SCREEN_HEIGHT-100)]

plateformes = [{'x': 400, 'y': SCREEN_HEIGHT-200, 'width':150},
               {'x': 800, 'y': SCREEN_HEIGHT-250, 'width':150},
               {'x': 1000, 'y': SCREEN_HEIGHT-310, 'width':200}]

scroll = 0

listeDesPointsDeLaTrajectoire = []
dureeAvantSupression = 0

# jeu
jeuEstEnCoursDeFonctionnement = True
while jeuEstEnCoursDeFonctionnement:
    clock.tick(FPS)

    # fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeuEstEnCoursDeFonctionnement = False

    # mouvements
    keys = pygame.key.get_pressed()
    player.update(keys)

    scroll = player.rect.x - SCREEN_WIDTH//2

    for enemi in enemies:
        enemi.update()

    if player.isJumping:
        listeDesPointsDeLaTrajectoire.append((player.rect.centerx + scroll,player.rect.centery))
        dureeAvantSupression = pygame.time.get_ticks()
    if not player.isJumping:
        if pygame.time.get_ticks() - dureeAvantSupression > 1000:
            listeDesPointsDeLaTrajectoire.clear()

    playerHitBox = pygame.Rect(player.rect.x + scroll,player.rect.y,player.rect.width,player.rect.height)
    for enemi in enemies:
        enemiHitBox = pygame.Rect(enemi.rect.x,enemi.rect.y,enemi.rect.width,enemi.rect.height)
        if playerHitBox.colliderect(enemiHitBox):
            print("Collision détectée !\n     ==========\n     Game Over\n    ==========")
            jeuEstEnCoursDeFonctionnement = False

    drawWindow(player,enemies,plateformes,decalageDuBackgroundEnX,scroll,listeDesPointsDeLaTrajectoire)


pygame.quit()
sys.exit()

# en gros, on a besoin  de transformer FORCE_DU_SAUT et VITESSE_DEPLACEMENT en variables pour pouvoir utilisé les equations horraires.
# avec vitesse_deplacement (en variable), on aurait de l'inertie, et force_du_saut (en variable aussi) dépendrait de vitesse_deplacement
# on pourrait ensuite ajouter une touche (genre fleche haut et bas) qui modifierait la gravité, QUE si isJumping == False !!
# après pour le niveau il faudra modifier le groundLvL pour faire genre c'est une plateformes (alors que ce sera totalement une image)