from ...assets.maps.level1_map import *
from ...pygame_code.constants import *
from ...assets.maps.level1_map import *

class level1():
    def __init__(self):
        # Setting the map layout - Contain positional information about elements in the map
        self.map = level1_map

        # Setting the screen sizes - Related to 'constants.py' file
        self.screen_width = SCREEN_WIDTH
        self.tile_size = TILE_SIZE
        self.screen_height = self.tile_size * len(self.map)
        
        # Setting the Background image
        ###################
        ###### TO DO ######
        ###################
        
        # Setting the music/sounds of the level
        ###################
        ###### TO DO ######
        ###################

        