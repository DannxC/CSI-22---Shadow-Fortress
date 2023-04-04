import pygame
from assets.constants.constants import *
from data_objects.levels.tiles import Tile
from data_objects.players.player import Player

class Level():
    def __init__(self, level_data, surface):
        # Setting the map layout - Contains positional information about elements in the map
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 1
        
    # Setting the group of tiles
    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_indx, row in enumerate(layout):
            for col_indx, cell in enumerate(row):
                x = col_indx * TILE_SIZE
                y = row_indx * TILE_SIZE
                if cell == '1' or cell == '0':
                    tile = Tile((x,y), TILE_SIZE)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
    
    # Scroll the level tiles
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < SCREEN_WIDTH/5 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        elif player_x > 4*SCREEN_WIDTH/5 and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6

    # Get the horizontal movement collisions
    def collisions_x(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left 

# Get the vertical movement collisions
    def collisions_y(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 

    # Draw the sprites
    def run(self):
        # Level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        # Player
        self.player.update()
        self.collisions_x()
        self.collisions_y()
        self.player.draw(self.display_surface)
       

        
