import pygame

class Spikes:
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.scale = scale
        self.image = pygame.image.load('assets/spikes.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale/2))
        #srink the hitbox and move it down 
        self.hitbox = self.image.get_rect(topleft = (self.x, self.y))

    def render(self):
        return self.image, self.hitbox

    def get_hitbox(self):
        return self.hitbox
    
    def get_image(self):
        return self.image
    
    def get_scale(self):
        return self.scale

    def translate(self, x, y):
        self.x += x
        self.y += y
        self.hitbox = self.image.get_rect(topleft = (self.x, self.y))
