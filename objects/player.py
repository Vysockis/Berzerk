from objects.character import Character
import settings
import pygame

class Player(Character):
    def __init__(self):
        image = pygame.Surface((32, 32))
        image.fill((255, 0, 0))
        super().__init__(image, settings.WALK_SPEED_USER, settings.SHOOT_COOLDOWN)  # Set player-specific speed and cooldown

    def update(self):
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