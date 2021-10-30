# Simple pygame program
# add text to program and convert to flashy words
# Import and Initialize library
import pygame
import random

pygame.init()

# setup display
screen = pygame.display.set_mode((1920, 1080))

# Run game loop
running = True
r, g, b = 0, 0, 0
while running:
    r = random.randint(1, 254)
    b = random.randint(1, 254)
    g = random.randint(1, 254)
    # Did user exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((g, b, r))

    # Draw a solid colour changing circle in the center
    for i in range(10):
        j = random.randrange(1, 1920, 10)
        k = random.randrange(1, 1080, 5)
        pygame.draw.circle(screen, [r, g, b], (j, k), 75)
        pygame.display.flip()

    # Flip the display
    pygame.display.flip()
# Done quit
pygame.quit()
