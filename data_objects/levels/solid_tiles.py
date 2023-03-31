import pygame

class SolidTile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        
        # Define the image      ->      IMPORT FRMO ASSETS IN FUTURE !!!!!!!!!!
        self.image = pygame.Surface((size, size))
        self.image.fill('grey')

        # Define the rectangle
        self.rect = self.image.get_rect(topleft = position).convert_alpha()