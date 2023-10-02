import pygame
import settings
import math
from objects.bullet import Bullet

class Character(pygame.sprite.Sprite):
    def __init__(self, image, speed, shoot_cooldown):
        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH // 2, settings.HEIGHT // 2)

        self.speed          = speed
        self.shoot_cooldown = shoot_cooldown
        self.bullets        = pygame.sprite.Group()
        self.lives          = 1

    def update(self):
        if self.shoot_cooldown >= 0:
            self.shoot_cooldown -= 1

    def shoot(self):
        if self.shoot_cooldown < 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)

            velocity_x = math.cos(angle) * settings.BULLET_SPEED
            velocity_y = math.sin(angle) * settings.BULLET_SPEED

            bullet = Bullet(self.rect.centerx, self.rect.centery, velocity_x, velocity_y)
            self.bullets.add(bullet)

            self.shoot_cooldown = settings.SHOOT_COOLDOWN

    def getBulletsSprite(self):
        return self.bullets
    
    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.kill()

    def get_lives(self):
        return self.lives
