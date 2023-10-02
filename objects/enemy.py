from objects.character import Character
import settings
import pygame
import random

class Enemy(Character):
    def __init__(self):
        image = pygame.Surface((32, 32))
        image.fill((0, 255, 0))
        super().__init__(image, settings.WALK_SPEED_ENEMY, settings.SHOOT_COOLDOWN)  # Set enemy-specific speed and cooldown

        self.rect.x = random.randint(0, settings.WIDTH - self.rect.width)
        self.rect.y = random.randint(0, settings.HEIGHT - self.rect.height)
        self.lives  = random.randint(settings.ENEMY_LIVES_START, settings.ENEMY_LIVES_END)