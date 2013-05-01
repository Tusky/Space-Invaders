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
enemies = []
enemyPosition = [
    (20,20),(80,20), (140, 20), (200, 20), (260, 20), (320, 20), (380, 20), (440, 20), (500, 20),
    (20,80),(80,80), (140, 80), (200, 80), (260, 80), (320, 80), (380, 80), (440, 80), (500, 80),
    (20,140),(80,140), (140, 140), (200, 140), (260, 140), (320, 140), (380, 140), (440, 140), (500, 140),
    (20,200),(80,200), (140, 200), (200, 200), (260, 200), (320, 200), (380, 200), (440, 200), (500, 200),
    (20,260),(80,260), (140, 260), (200, 260), (260, 260), (320, 260), (380, 260), (440, 260), (500, 260),
]
for pos in enemyPosition:
    enemy = Enemy(screen, pos[0], pos[1])
    enemies.append(enemy)
shots = []
shotCooldown = 0
playerSprite=pygame.sprite.Group(player)
allEnemies=pygame.sprite.Group(enemies)
movement = 1
endcooldown = False
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
        if shot.update():
            shots.remove(shot)
        if pygame.sprite.spritecollide(shot,allEnemies,True):
            shots.remove(shot)
            shot.playExplosion()
    for enemy in enemies:
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
    if endcooldown > 0:
        endcooldown -= dt
    if not len(allEnemies):
        if(endcooldown == False):
            endcooldown = 1000
        if(endcooldown < 0):
            print("you won")
            sys.exit()