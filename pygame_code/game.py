import pygame, sys

# Setup
pygame.init()
screen_width = 1200
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Main game loop
while True:
    # Checking events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill('black')
    
    # Update game objects and perform any game logic


    # Update Screen
    pygame.display.update()
    clock.tick(60)