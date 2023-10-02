import gameLogic

def loop(pygame, screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Game logic goes here
        gameLogic.logic()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw game objects
        # Replace this with your game's drawing code

        # Update the display
        pygame.display.flip()

    pygame.quit()