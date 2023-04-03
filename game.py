import pygame, sys
from assets.constants.constants import *
from assets.maps.level1 import level1_map
from data_objects.levels.level import Level
from data_objects.levels.solid_tiles import SolidTile
from data_objects.levels.tiles import Tile

# Setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
level = Level(level1_map, screen)

# Main game loop
while True:
    # Checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update game objects and perform any game logic
    screen.fill('black')
    level.run()

    # Update Screen
    pygame.display.update()
    clock.tick(60)