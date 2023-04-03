import pygame
from assets.constants.constants import *
from data_objects.levels.solid_tiles import SolidTile
from data_objects.levels.tiles import Tile

class Level():
    def __init__(self, level_data, surface):
        # Setting the map layout - Contains positional information about elements in the map
        self.display_surface = surface
        self.setup_level(level_data)
        
    # Setting the group of tiles
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        for row_indx, row in enumerate(layout):
            for col_indx, cell in enumerate(row):
                if cell == '1' or cell == '0':
                    x = col_indx * TILE_SIZE
                    y = row_indx * TILE_SIZE
                    tile = Tile((x,y), TILE_SIZE)
                    self.tiles.add(tile)
    
    # Draw the tiles
    def run(self):
        self.tiles.update(2)
        self.tiles.draw(self.display_surface)
       

        
