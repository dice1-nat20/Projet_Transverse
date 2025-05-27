##########################################
##       Immacolato Almha               ##
##       Chen Lana                      ##
##       Gbaguidi Bryan                 ##
##       Tchana Watat Emmanuelle        ##
##       Bertaina--David Sacha          ##
##       Projet : Transverse            ##
##########################################
import sys


from ennemis import *
from windows import *

pygame.init()

# constantes
PLAYER_SPRITE = pygame.image.load("images&otherFiles/placeHolderPlayer.png")
PLAYER_X = 50
PLAYER_Y = 50
GRAVITE = 1
FORCE_DU_SAUT = 25
VITESSE_DEPLACEMENT = 5



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # ça créer un autre objet pour le sprite à venir
        self.image = PLAYER_SPRITE
        self.rect = self.image.get_rect()  # le rectangle du sprite (sa hitbox)
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT - 130
        self.vel_x = 0  # la velocité en x
        self.vel_y = 0  # la velocité en y
        self.a = 0
        self.t = 0
        self.isJumping = False
        self.x0 = self.rect.x
        self.y0 = self.rect.y

    def update(self, keys):
        if not self.isJumping:
            # mouvements
            self.vel_x = 0
            if keys[pygame.K_LEFT]:
                self.vel_x = -VITESSE_DEPLACEMENT
            elif keys[pygame.K_RIGHT]:
                self.vel_x = VITESSE_DEPLACEMENT
            self.rect.x += self.vel_x

            # saut
            if keys[pygame.K_SPACE] and not self.isJumping:
                self.vel_y = -FORCE_DU_SAUT
                self.isJumping = True
                self.t = 0
                self.x0 = self.rect.x
                self.y0 = self.rect.y
        else:
            self.t += 1  # / FPS
            newX = self.vel_x * self.t
            newY = self.vel_y * self.t + 0.5 * GRAVITE * (self.t ** 2)
            self.rect.x = self.x0 + newX
            self.rect.y = self.y0 + newY

            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
                self.isJumping = False
                self.vel_x = 0
                self.vel_y = 0


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
        menus.displayGameName(screen, 250, 250)
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
