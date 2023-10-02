from objects.character  import Character
from objects.bullet     import Bullet
from objects.player     import Player
import settings
import pygame
import random
import math

class Enemy(Character):
    def __init__(self):
        image = pygame.Surface((32, 32))
        image.fill((0, 255, 0))
        super().__init__(image, settings.WALK_SPEED_ENEMY)  # Set enemy-specific speed and cooldown

        self.rect.x         = random.randint(0, settings.WIDTH - self.rect.width)
        self.rect.y         = random.randint(0, settings.HEIGHT - self.rect.height)
        self.lives          = random.randint(settings.ENEMY_LIVES_START, settings.ENEMY_LIVES_END)
        self.shoot_cooldown = random.randint(settings.ENEMY_SHOOT_START, settings.ENEMY_SHOOT_END)
        self.player         = Player()

    def update(self):
        if self.shoot_cooldown <= 0:
            self.shoot()

        self.shoot_cooldown -= 1

        return super().update()
    
    def shoot(self):
        player_center_x, player_center_y = self.player.rect.center
        enemy_center_x, enemy_center_y = self.rect.center

        angle = math.atan2(player_center_y - enemy_center_y, player_center_x - enemy_center_x)

        self.velocity_x = math.cos(angle) * settings.BULLET_SPEED
        self.velocity_y = math.sin(angle) * settings.BULLET_SPEED
        
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.velocity_x, self.velocity_y, (255, 255, 0))
        self.bullets.add(bullet)

        self.shoot_cooldown = random.randint(settings.ENEMY_SHOOT_START, settings.ENEMY_SHOOT_END)

    def setPlayer(self, player):
        self.player = player
