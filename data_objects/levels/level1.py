import pygame
from ...assets.maps.level1_map import *
from ...assets.constants.constants import *
from solid_tiles import SolidTile

class Level1():
    def __init__(self):
        # Setting the map layout - Contain positional information about elements in the map
        self.map = level1_map

        # Setting the screen sizes - Related to 'constants.py' file
        self.screen_width = SCREEN_WIDTH
        self.size = TILE_SIZE
        self.screen_height = self.tile_size * len(self.map)
        
        # Setting the Background image
        ###################
        ###### TO DO ######
        ###################
        
        # Setting the music/sounds of the level
        ###################
        ###### TO DO ######
        ###################

        # Setting the group of solid_tiles
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if j == '0':
                    self.solid_tiles = pygame.sprite.Group(SolidTile((i+1, j+1) * self.size + 1, self.size))
