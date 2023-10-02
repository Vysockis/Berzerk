import pygame
import settings
from objects.player import Player
from objects.enemy  import Enemy

pygame.init()

# Create the game window
screen = pygame.display.set_mode(settings.WINDOW_SIZE)
pygame.display.set_caption("Berzek Game")


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

enemies = pygame.sprite.Group()
while len(enemies) < 5:
    enemy = Enemy()
    enemy.setPlayer(player)
    enemies.add(enemy)



clock = pygame.time.Clock() 

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()
    enemies.update()
    player.getBulletsSprite().update()
    for enemy in enemies.sprites():
        enemy.getBulletsSprite().update()

    hits_enemies = pygame.sprite.groupcollide(enemies, player.getBulletsSprite(), False, True)

    for hit in hits_enemies:
        hit.lose_life()
        pass

    for enemy in enemies.sprites():
        hits_player  = pygame.sprite.groupcollide(all_sprites, enemy.getBulletsSprite(), False, True)

        for hit in hits_player:
            hit.lose_life()
            pass

    screen.fill((0, 0, 0))

    all_sprites.draw(screen)
    enemies.draw(screen)
    player.getBulletsSprite().draw(screen)
    for enemy in enemies.sprites():
        enemy.getBulletsSprite().draw(screen)

    pygame.display.flip()

    clock.tick(settings.FPS)

pygame.quit()