from objects.character  import Character
from objects.bullet     import Bullet
import settings
import pygame
import math

class Player(Character):
    def __init__(self):
        image = pygame.Surface((32, 32))
        image.fill((255, 0, 0))
        super().__init__(image, settings.WALK_SPEED_USER)

        self.shoot_cooldown = settings.SHOOT_COOLDOWN
        self.lives          = settings.USER_LIVES

    def update(self):
        if self.shoot_cooldown >= 0:
            self.shoot_cooldown -= 1

        keys    = pygame.key.get_pressed()
        mouses  = pygame.mouse.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed
        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if mouses[0]:
            self.shoot()

        self.move()
        return super().update()

    def move(self):
        self.rect.x = max(0, min(self.rect.x, settings.WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, settings.HEIGHT - self.rect.height))

    def shoot(self):
        if self.shoot_cooldown < 0:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            angle = math.atan2(mouse_y - self.rect.centery, mouse_x - self.rect.centerx)

            self.velocity_x = math.cos(angle) * settings.BULLET_SPEED
            self.velocity_y = math.sin(angle) * settings.BULLET_SPEED

            bullet = Bullet(self.rect.centerx, self.rect.centery, self.velocity_x, self.velocity_y, (0, 0, 255))
            self.bullets.add(bullet)

            self.shoot_cooldown = settings.SHOOT_COOLDOWN