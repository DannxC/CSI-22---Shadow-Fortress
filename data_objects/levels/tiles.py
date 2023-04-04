import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.image.get_rect(topleft = pos)

    # Update the tile position as the level shifts
    def update(self, world_shift):
        self.rect.x += world_shift


class SolidTile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')

        # Define the rectangle
        self.rect = self.image.get_rect(topleft = position)
