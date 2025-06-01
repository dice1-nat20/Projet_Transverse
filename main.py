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
from Plateform import *
from windows import *
import time


pygame.init()
clock = pygame.time.Clock()

# création du joueur
player = Player()

# création des ennemis
enemies = [Enemy(500,SCREEN_HEIGHT-100)]

# création des plateformes
plateformes = [Plateform(400,groundLvL - 200, 100),
               Plateform(800,groundLvL - 250, 150),
               Plateform(1200,groundLvL - 300, 120)]

# quelques variables utiles
scroll = 0
decalageDuBackgroundEnX = 0

listeDesPointsDeLaTrajectoire = []
dureeAvantSupression = 0

estVictoire = False
estSurLaPlateforme = False

# jeu
jeuEstEnCoursDeFonctionnement = True
while jeuEstEnCoursDeFonctionnement:
    clock.tick(FPS)

    # fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jeuEstEnCoursDeFonctionnement = False

    # actions du joueur
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        player.poids += 0.1
    if keys[pygame.K_UP]:
        player.poids = max(0.4, player.poids - 0.1)
    player.update(keys)

    # mouvements de l'écran (du background)
    scroll = int(player.rect.x - SCREEN_WIDTH//2) * VITESSE_DE_SCROLL

    # mouvement de l'ennemi
    for enemi in enemies:
        enemi.update()

    # gestion des collisions
    playerHitBox = pygame.Rect(player.rect.x + scroll, player.rect.y, player.rect.width, player.rect.height)

    # joueur/plateformes
    for plt in plateformes:
        plt.update(scroll)
    for plt in plateformes:
        if player.vel_y >= 0 and player.rect.colliderect(plt.rect):
            if player.rect.bottom - plt.rect.top <= 10:
                player.rect.bottom = plt.rect.top
                player.vel_y = 0
                player.isJumping = False

    # affichage de la courbe lors du saut
    if player.isJumping:
        listeDesPointsDeLaTrajectoire.append((player.rect.centerx + scroll,player.rect.centery))
        dureeAvantSupression = pygame.time.get_ticks()
    if not player.isJumping:
        if pygame.time.get_ticks() - dureeAvantSupression > 1000:
            listeDesPointsDeLaTrajectoire.clear()

    # joueur/ennemies
    for enemi in enemies:
        enemiHitBox = pygame.Rect(enemi.rect.x, enemi.rect.y, enemi.rect.width, enemi.rect.height)
        if playerHitBox.colliderect(enemiHitBox):
            print("Collision détectée !\n    ===========\n     Game Over\n    ===========")
            jeuEstEnCoursDeFonctionnement = False

    # joueur/zone de fin
    if playerHitBox.colliderect(VICTORY_ZONE):
        estVictoire = True
        jeuEstEnCoursDeFonctionnement = False

    drawWindow(player,enemies,plateformes,decalageDuBackgroundEnX,scroll,listeDesPointsDeLaTrajectoire)

# ici c'est que pour les winners
if estVictoire:
    font = pygame.font.SysFont("Arial", 48)
    surfaceDuTexte = font.render("Vous avez Gagné ! gg ez", True, (255,255,0))
    screen.fill((0,0,0))
    screen.blit(surfaceDuTexte,(SCREEN_WIDTH // 2 - surfaceDuTexte.get_width() // 2, SCREEN_HEIGHT // 2 - surfaceDuTexte.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(4500)

pygame.quit()
sys.exit()
