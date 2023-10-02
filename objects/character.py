import pygame
import settings
import math
from objects.bullet import Bullet

class Character(pygame.sprite.Sprite):
    def __init__(self, image, speed):
        super().__init__()

        self.image = image

        self.rect = self.image.get_rect()
        self.rect.center = (settings.WIDTH // 2, settings.HEIGHT // 2)

        self.speed          = speed
        self.bullets        = pygame.sprite.Group()
        self.lives          = 1
        self.velocity_x     = 0
        self.velocity_y     = 0

    def getBulletsSprite(self):
        return self.bullets
    
    def lose_life(self):
        self.lives -= 1
        if self.lives <= 0:
            self.kill()

    def get_lives(self):
        return self.lives
