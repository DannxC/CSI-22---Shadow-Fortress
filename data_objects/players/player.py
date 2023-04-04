import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

        # Player movement 
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 6
        self.gravity = 0.8
        self.jump_speed = -15
        self.double_jump = False
        self.double_jump_delay = 0

        # Player status
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

    
    def get_input(self):
        keys = pygame.key.get_pressed()
        self.double_jump_delay += 1

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            self.jump()           
           

    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 0:
            self.status = 'fall'
        else: 
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.rect.y += self.direction.y
        self.direction.y += self.gravity

    def jump(self):
        # Jump only if the player stands on ground
        if self.on_ground:
            self.direction.y = self.jump_speed
        # Double jump only after a certain delay and only once in the air
        if self.double_jump and self.double_jump_delay >= 15:
            self.direction.y = self.jump_speed 
            self.double_jump = False

    def update(self):
        self.get_input()
        self.get_status()

