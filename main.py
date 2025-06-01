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


pygame.init()
clock = pygame.time.Clock()

backgroundX = 0


player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

enemies = [Enemy(500,SCREEN_HEIGHT-100),Enemy(1000,SCREEN_HEIGHT-100)]

plateformes = [{'x': 400, 'y': SCREEN_HEIGHT-200, 'width':100},
               {'x': 800, 'y': SCREEN_HEIGHT-250, 'width':100},
               {'x': 1000, 'y': SCREEN_HEIGHT-310, 'width':150}]

# jeu
running = True
while running:
    clock.tick(FPS)

    # fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # mouvements
    keys = pygame.key.get_pressed()
    player.update(keys)

    world_shift = 0
    if player.rect.x >= DEAD_ZONE_D:
        bougeDeLa = player.rect.x - DEAD_ZONE_D
        player.rect.x = DEAD_ZONE_D
        world_shift = bougeDeLa
    elif player.rect.x <= DEAD_ZONE_G:
        bougeDeLa = player.rect.x - DEAD_ZONE_G
        player.rect.x = DEAD_ZONE_G
        world_shift = bougeDeLa

    for enemi in enemies:
        if enemi.rect.x > player.rect.x:
            enemi.rect.x -= world_shift

    for plt in plateformes:
        if plt['x'] > player.rect.x:
            plt['x'] -= world_shift

    backgroundX -= world_shift // 2

    for enemi in enemies:
        enemi.update()

    colisions_JE = pygame.Rect(player.rect.x,player.rect.y,player.rect.width,player.rect.height)
    for enemi in enemies:
        if colisions_JE.colliderect(enemi.rect):
            print("Collision détectée !")
            running = False

    drawWindow(player,enemies,plateformes,backgroundX)
    """if pygame.sprite.spritecollide(player, enemies, False):
        print("Game Over!")
        running = False

    screen.fill(BACKGROUND)
    player_group.draw(screen)
    enemies.draw(screen)
    pygame.display.flip()"""

pygame.quit()
sys.exit()

# en gros, on a besoin  de transformer FORCE_DU_SAUT et VITESSE_DEPLACEMENT en variables pour pouvoir utilisé les equations horraires.
# avec vitesse_deplacement (en variable), on aurait de l'inertie, et force_du_saut (en variable aussi) dépendrait de vitesse_deplacement
# on pourrait ensuite ajouter une touche (genre fleche haut et bas) qui modifierait la gravité, QUE si isJumping == False !!
# après pour le niveau il faudra modifier le groundLvL pour faire genre c'est une plateformes (alors que ce sera totalement une image)