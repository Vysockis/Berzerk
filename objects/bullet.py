import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()

        self.image = pygame.Surface((5, 5))
        self.image.fill((0, 0, 255))  

        self.rect = self.image.get_rect()
        self.rect.midbottom = (x, y)  

        self.velocity_x = velocity_x
        self.velocity_y = velocity_y

    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y

        if self.rect.bottom < 0 or self.rect.top > 600 or self.rect.right < 0 or self.rect.left > 800:
            self.kill()