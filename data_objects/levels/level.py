import pygame
from assets.constants.constants import *
from data_objects.levels.tiles import Tile
from data_objects.players.player import Player

class Level():
    def __init__(self, level_data, surface):
        # Setting the map layout - Contains positional information about elements in the map
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0
        
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
    def scroll(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        #player_y = player.rect.centery
        direction_x = player.direction.x
        #direction_y = player.direction.y

        if player_x < SCREEN_WIDTH/5 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        elif player_x > 4*SCREEN_WIDTH/5 and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6

        '''if player_y < SCREEN_HEIGHT/5:
            self.world_shift[1] = player.speed

        elif player_x > 4*SCREEN_HEIGHT/5:
            self.world_shift[1] = - player.speed
        else:  
            self.world_shift[1] = 0'''

    # Get the horizontal movement collisions
    def collisions_x(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
                    
        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

# Get the vertical movement collisions
    def collisions_y(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    player.double_jump = True
                    player.double_jump_delay = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0 
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    # Draw the sprites
    def run(self):
        # Level tiles
        self.scroll()
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        # Player
        self.player.update()
        self.collisions_x()
        self.collisions_y()
        self.player.draw(self.display_surface)
       

        
