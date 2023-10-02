import pygame
import gameLoop

pygame.init()

# Window dimensions
WIDTH, HEIGHT = 800, 600
WINDOW_SIZE = (WIDTH, HEIGHT)

# Create the game window
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Berzek Game")

gameLoop.loop(pygame, screen)