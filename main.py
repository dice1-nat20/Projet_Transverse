##########################################
##       Immacolato Almha               ##
##       Chen Lana                      ##
##       Gbaguidi Bryan                 ##
##       Tchana Watat Emmanuelle        ##
##       Bertaina--David Sacha          ##
##       Projet : Transverse            ##
##########################################
import pygame
import sys


# sprites
player_img = pygame.image.load("images&otherFiles/placeHolderPlayer.png")
enemy_img = pygame.image.load("images&otherFiles/placeHolderOther.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # ça créer un utre objet pour le sprite à venir
        self.image = player_img
        self.rect = self.image.get_rect()   # le rectangle du sprite (sa hitbox)
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT - 150
        self.vel_x = 0
        self.vel_y = 0  # la velocité en y
        self.on_ground = False

    def update(self, keys):
        dx = 0
        dy = 0

        if keys[pygame.K_LEFT] and self.on_ground:
            dx = -5
        if keys[pygame.K_RIGHT] and self.on_ground:
            dx = 5

        # saut
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -25
            self.on_ground = False

        # gravité
        self.vel_y += 0.8
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # collisions
        if self.rect.bottom + dy >= SCREEN_HEIGHT - 50:
            dy = SCREEN_HEIGHT - 50 - self.rect.bottom
            self.on_ground = True
            self.vel_y = 0

        # mouvements
        self.rect.x += dx
        self.rect.y += dy

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = enemy_img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += self.move_direction * 2
        self.move_counter += 1
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1


player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

enemies = pygame.sprite.Group()
for i in range(3):
    enemy = Enemy(300 + i * 150, SCREEN_HEIGHT - 150  )
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
        time.sleep(2)
        running = False

    screen.fill(GREEN)
    player_group.draw(screen)
    enemies.draw(screen)
    pygame.display.flip()

pygame.quit()
sys.exit()
