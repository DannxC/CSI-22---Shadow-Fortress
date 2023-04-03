import pygame, sys
from assets.constants.constants import *
from data_objects.levels.solid_tiles import SolidTile

# Setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
test_tile = pygame.sprite.Group(SolidTile((100, 100), 200))

# Main game loop
while True:
    # Checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update game objects and perform any game logic
    # Update Map Level:
    screen.fill('black')
    test_tile.draw(screen)

    # Update Screen
    pygame.display.update()
    clock.tick(60)