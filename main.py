import pygame, sys
from pygame.locals import *
from player import Player
from enemy import Enemy
from shot import Shot

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((800,600))
pygame.mouse.set_visible(0)

player = Player(screen)
enemy = Enemy(screen)
enemies = []
enemies.append(enemy)
shots = []
shotCooldown = 0
playerSprite=pygame.sprite.Group(player)
allEnemies=pygame.sprite.Group(enemies)
movement = 1
while True:
    dt = clock.tick(60)
    background=pygame.Surface(screen.get_size())
    background=background.convert()
    background.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[K_LEFT]:
        player.moveVertically(-10)
    if keys_pressed[K_RIGHT]:
        player.moveVertically(10)
    if keys_pressed[K_SPACE]:
        if shotCooldown <= 0:
            shots.append(Shot(screen, player))
            shotCooldown = 500 # adds a half second cooldown

    shotCooldown -= dt
    allShots=pygame.sprite.Group(shots)
    for shot in shots:
        if shot.update() or pygame.sprite.spritecollide(shot,allEnemies,True):
            shots.remove(shot)

    if enemy.getCoordinates()[0] > screen.get_width() - 50:
        movement = -1
    elif enemy.getCoordinates()[0] < 50:
        movement = 1
    else:
        movement = movement
    enemy.moveVertically(movement)

    allEnemies.clear(screen,background)
    allShots.clear(screen,background)
    playerSprite.clear(screen,background)
    allEnemies.update()
    playerSprite.update()
    allEnemies.draw(screen)
    allShots.draw(screen)
    playerSprite.draw(screen)
    pygame.display.update()
    if not len(allEnemies):
        print("you won")
        sys.exit()