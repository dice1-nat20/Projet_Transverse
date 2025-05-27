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

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

enemies = pygame.sprite.Group()
for i in range(1):
    enemy = Enemy(300 + i * 150, SCREEN_HEIGHT - 150)
    enemies.add(enemy)

# jeu
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)
    enemies.update()

    if pygame.sprite.spritecollide(player, enemies, False):
        print("Game Over!")
        running = False

    screen.fill(WHITE)
    player_group.draw(screen)
    enemies.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()

# en gros, on a besoni de transformer FORCE_DU_SAUT et VITESSE_DEPLACEMENT en variables pour pouvoir utilisé les equations horraires.
# avec vitesse_deplacement (en variable), on aurait de l'inertie, et force_du_saut (en variable aussi) dépendrait de vitesse_deplacement
# on pourrait ensuite ajouter une touche (genre fleche haut et bas) qui modifierait la gravité, QUE si isJumping == False !!
# après pour le niveau il faudra modifier le groundLvL pour faire genre c'est une plateformes (alors que ce sera totalement une image)