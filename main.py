import pygame
import time
import player
import bag
import world
import interface

pygame.init()
pygame.mixer.init()

FPS = 60
WIN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
HEIGHT = WIN.get_height()
WIDTH = WIN.get_width()

pygame.display.set_caption("Shadow Fortress")

def display_fps(clock):
    # display fps at the top of the screen
    font = pygame.font.Font('fonts/dogicapixelbold.ttf', int(WIDTH/70))
    text = font.render("FPS: " + str(int(clock.get_fps())), 1, (255,255,255))
    WIN.blit(text, (WIDTH * 9/10, HEIGHT/20))

def display_hitbox(hitbox):
    for hb in hitbox:
        pygame.draw.rect(WIN, (255,0,0), hb, 2)
    pygame.draw.rect(WIN, (0,0,255), hitbox[1], 2)

def render_player(player1, ground, spikes, keys_pressed, release_up_key, release_space_key, frame, game_world, margin_horizontal, margin_vertical, hit_timer, hit_timer_max):
    player_hitbox, player_image = player1.render_player(ground, spikes, keys_pressed, release_up_key, release_space_key, frame)
    # check if player get hit and if he is, start counting the time
    
    game_state = "run"
    if player1.get_get_hit():
        hit_timer = time.time()

        player1.health -= 10  # You can set the damage value as per your game requirements
        if player1.health <= 0:
            player1.health = 0

        # Handle player death or game over logic here
        if player1.health == 0:
            game_state = "dead"

        player1.set_get_hit(False)
    
    # if the time is smaller than 1 second, gigle the player
    if time.time() - hit_timer < hit_timer_max:
        player1.set_invencible(True)
        if frame % 4 == 0:
            #make player opacity change
            player_image.set_alpha(40)
        elif(frame % 4 == 2):
            # game_world.translate(-10, 0)
            # player_hitbox.x -= 10
            player_image.set_alpha(255)
    else:
        player_image.set_alpha(255)
        player1.set_invencible(False)

    #make camera follow player
    follow_x_n, follow_x_p, follow_y_n, follow_y_p = game_world.follow()
    if(player_hitbox.x < margin_horizontal and follow_x_n):
        game_world.translate(margin_horizontal - player_hitbox.x, 0)
        player_hitbox.x = margin_horizontal
    elif(player_hitbox.x > WIDTH - margin_horizontal and follow_x_p):
        game_world.translate(WIDTH - margin_horizontal - player_hitbox.x, 0)
        player_hitbox.x = WIDTH - margin_horizontal
    if(player_hitbox.y < margin_vertical and follow_y_n):
        game_world.translate(0, margin_vertical - player_hitbox.y)
        player_hitbox.y = margin_vertical
    elif(player_hitbox.y > HEIGHT - margin_vertical and follow_y_p):
        game_world.translate(0, HEIGHT - margin_vertical - player_hitbox.y)
        player_hitbox.y = HEIGHT - margin_vertical

    game_world.check_room(player1)

    WIN.blit(player_image, player_hitbox)

    return player_hitbox, hit_timer, game_state

import pygame

def render_health_bar(screen, health, max_health, x, y, width, height, colors):
    colors = {
        'border': (255, 255, 255),
        'background': (128, 0, 0),
        'health': (255, 0, 0),
        'health_gradient_end': (192, 0, 0),
        'health_gradient_start': (255, 0, 0),
        'text': (255, 255, 255)
    }

    # Calculate health ratio and width
    health_ratio = health / max_health
    health_width = int(health_ratio * width)
    
    # Define border and background rects
    border_rect = pygame.Rect(x, y, width, height)
    background_rect = pygame.Rect(x + 2, y + 2, width - 4, height - 4)
    
    # Draw border and background
    pygame.draw.rect(screen, colors['border'], border_rect)
    pygame.draw.rect(screen, colors['background'], background_rect)
    
    # Draw health gradient
    if health_ratio > 0:
        health_gradient = pygame.Surface((health_width, height))
        health_gradient.fill(colors['health_gradient_end'])
        pygame.draw.rect(health_gradient, colors['health_gradient_start'], pygame.Rect(0, 0, health_width, height), border_radius=int(height / 2))
        screen.blit(health_gradient, (x + 2, y + 2))
    
    # Draw health value
    font = pygame.font.Font('fonts/dogicapixelbold.ttf', int(height * 0.8))
    health_text = font.render(str(int(health)), True, colors['text'])
    text_x = x + (width - health_text.get_width()) / 2
    text_y = y + (height - health_text.get_height()) / 2
    screen.blit(health_text, (text_x, text_y))


def render_bag(screen, bag, x, y, width, height):
    bag.check_and_remove_empty_items()

    font = pygame.font.Font('fonts/dogicapixelbold.ttf', int(height / 2))
    square_size = int(width / 1.2)
    border_width = 3

    background_color = (139, 69, 19)
    background_margin = 10
    background_width = len(bag.items) * width + background_margin * 2
    background_height = height + background_margin * 2
    background_rect = pygame.Rect(x - background_margin, y - background_margin, background_width, background_height)
    pygame.draw.rect(screen, background_color, background_rect)
    pygame.draw.rect(screen, (255, 255, 255), background_rect, border_width)

    for i, item in enumerate(bag.items):
        item_rect = pygame.Rect(x + (i * width), y, square_size, square_size)
        pygame.draw.rect(screen, (255, 255, 255), item_rect, border_width)

        # Make the square background black if an item is present
        if item is not None:
            pygame.draw.rect(screen, (0, 0, 0), item_rect.inflate(-border_width, -border_width))

            # Scale the item icon to fit in the square and display it
            item_icon = pygame.transform.scale(item.icon, (square_size, square_size))
            screen.blit(item_icon, (x + (i * width), y))

            # Display item's quantity
            item_name_font = pygame.font.Font(None, int(height / 4))
            item_quantity_text = item_name_font.render(str("x" + str(item.quantity)), True, (255, 255, 255))
            item_quantity_text_x = x + (i * width) + (square_size - item_quantity_text.get_width()) / 2
            item_quantity_text_y = y + 4.3 * square_size / 4
            screen.blit(item_quantity_text, (item_quantity_text_x, item_quantity_text_y))

        else:
            # Display the number if there's no item in the slot
            item_text = font.render(str(i + 1), True, (255, 255, 255))
            item_text_x = x + (i * width) + (square_size - item_text.get_width()) / 2
            item_text_y = y + (square_size - item_text.get_height()) / 2
            screen.blit(item_text, (item_text_x, item_text_y))

def render_death_screen(screen, width = WIDTH, height = HEIGHT):
    # Create a new surface with a semi-transparent black color
    darken_surface = pygame.Surface((width, height))
    darken_surface.fill((0, 0, 0, 128))
    
    # Blit the darken surface onto the screen surface
    screen.blit(darken_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

    font_large = pygame.font.Font('fonts/dogicapixelbold.ttf', int(height / 4))
    font_small = pygame.font.Font('fonts/dogicapixelbold.ttf', int(height / 10))
    
    text_large = font_large.render('YOU DIED', True, (255, 255, 255))
    text_large_x = (width - text_large.get_width()) / 2
    text_large_y = (height - text_large.get_height()) / 2 - 250

    text_small = font_small.render('Press any key to quit', True, (255, 255, 255))
    text_small_x = (width - text_small.get_width()) / 2
    text_small_y = (height - text_small.get_height()) / 2 + 250

    credit_font = pygame.font.Font('fonts/dogicapixelbold.ttf', int(height / 35))
    credit_text = credit_font.render('GAME MADE BY: Daniel Cavassani, Marcel Versiani, Rafael Otero', True, (255, 255, 255))
    credit_text_x = (width - credit_text.get_width()) / 2
    credit_text_y = height - credit_text.get_height() - 20

    screen.blit(text_large, (text_large_x, text_large_y))
    screen.blit(text_small, (text_small_x, text_small_y))
    screen.blit(credit_text, (credit_text_x, credit_text_y))




def main():

    game_state = "init"

    game_room = "init"

    disp_hitbox = False

    # margin of camera to player
    margin_vertical = int(HEIGHT/4)
    margin_horizontal = int(WIDTH/4)

    #init the player
    player_scale = int(WIDTH/16)
    player1 = player.Player(x = margin_horizontal, y= WIDTH/2, scale = player_scale)
    release_up_key = False
    release_down_key = False
    release_space_key = False
    frame = 0
    hit_timer = 0
    hit_timer_max = 1

    #init the player's bag
    player1_bag = bag.Bag()

    #init health bar
    health_bar_colors = {'border': (255, 255, 255), 'health': (255, 0, 0), 'background': (128, 128, 128)}

    #starting with 10 potions
    health_potion = bag.HealthPotion(quantity = 5)
    player1_bag.add_item(health_potion, 0)

    #make the level
    blocks_scale = int(WIDTH/30)
    game_world = world.Level(fase = 1, blocks_scale=blocks_scale, WHIDTH=WIDTH, HEIGHT=HEIGHT)
    game_world.set_level(player1)

    # init the interfaces
    initial_menu = interface.InitialScreen(WIDTH, HEIGHT)
    menu = interface.Menu(WIDTH, HEIGHT)

    #init the sounds
    general_volume = 0.7
    playing_music = False
    #playing_SEF = False
    cathedral = pygame.mixer.Sound('musics/cathedral.mp3')
    epic = pygame.mixer.Sound('musics/gamerun2.mp3')
    entrance = pygame.mixer.Sound('musics/entrance.aiff')
    timer_music = 0
    #timer_SEF = 0
    current_music = epic

    
    #RUN THE GAME
    clock = pygame.time.Clock()
    run = True
    while run:
        frame += 1
        clock.tick(FPS)

        if game_state == "run":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        player1.set_sword(not player1.get_sword())
                    if event.key == pygame.K_d:
                        player1.set_shield(not player1.get_shield())
                    if event.key == pygame.K_h:
                        disp_hitbox = not disp_hitbox
                    if event.key == pygame.K_j:
                        player1.set_can_double_jump(not player1.get_can_double_jump())
                    if event.key == pygame.K_k:
                        player1.set_can_dash(not player1.get_can_dash())
                    #reset player position to test
                    if event.key == pygame.K_r:
                        game_world.go_to_room(0,0,player1)
                    if event.key == pygame.K_ESCAPE:
                        game_state = "menu"
                    if event.key == pygame.K_i:
                        player1.set_get_hit(True)
                    #bag usage
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5]:
                        index = int(event.unicode) - 1
                        item = player1_bag.get_item(index)
                        if item is not None and item.name == "Health Potion":
                            if player1.health < 100:
                                player1_bag.items[index].use()
                                player1.health += 10
                                if player1.health >= 100:
                                    player1.health = 100
                        else:
                            print(f"Item {index + 1} is empty")
                
            keys_pressed = pygame.key.get_pressed()

            game_world.render_level(WIN)
            ground, spikes = game_world.get_hitboxes()
            hitboxes = game_world.hitboxes()

            player_hitbox, hit_timer, game_state = render_player(player1, ground, spikes, keys_pressed, release_up_key, release_space_key, frame, game_world, margin_horizontal, margin_vertical, hit_timer, hit_timer_max)
            
            # Render health bar
            render_health_bar(WIN, player1.get_health(), 100, 10, 10, 600, 60, health_bar_colors)

            # Rende player's bag
            bag_x = int(WIDTH / 2 - (5 * 65) / 2)  # Assuming 5 items with 65 width each
            bag_y = 10
            render_bag(WIN, player1_bag, bag_x, bag_y, 65, 65)

            # display hitbox
            if(disp_hitbox):
                hitbox = []
                hitbox.append(player_hitbox)
                hitbox.extend(hitboxes)
                display_hitbox(hitbox)

        elif game_state == "dead":
            render_death_screen(WIN)
            pygame.time.delay(1000)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    run = False

        elif game_state == "init":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if(initial_menu.get_actual_button() == 'Exit'):
                            run = False
                        else:
                            game_state = "run"
                            game_room = "entrance"
                            pygame.mixer.Sound.fadeout(current_music, 100)
                            #entrance.set_volume(0.4*general_volume)
                            #pygame.mixer.Sound.play(entrance)
                            epic.set_volume(general_volume)
                            pygame.mixer.Sound.play(epic)
            
            keys_pressed = pygame.key.get_pressed()

            initial_menu.render(WIN, keys_pressed, release_up_key, release_down_key)

        elif game_state == "menu":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_state = "run"
                    if event.key == pygame.K_RETURN:
                        choice = menu.get_choice()
                        print(choice)
                        if choice == 'Resume':
                            game_state = "run"
                        elif choice == 'Exit':
                            run = False
                if(menu.exit(event)):
                    run = False
            #create menu
            keys_pressed = pygame.key.get_pressed()
            menu.render(WIN, keys_pressed, general_volume, release_up_key, release_down_key)

            if game_state == "run":
                menu.set_display(False)

        # make the mixer play the music
        if(game_room == 'init'):
            
            if not playing_music:
                cathedral.set_volume(general_volume)
                pygame.mixer.Sound.play(cathedral)
                current_music = cathedral
                timer_music = time.time()
                playing_music = True
            
            if time.time() - timer_music > current_music.get_length():
                playing_music = False

        keys_pressed = pygame.key.get_pressed()
        
        if not keys_pressed[pygame.K_UP]:
            release_up_key = True
        else:
            release_up_key = False

        if not keys_pressed[pygame.K_SPACE]:
            release_space_key = True
        else:
            release_space_key = False

        if not keys_pressed[pygame.K_DOWN]:
            release_down_key = True
        else:
            release_down_key = False

        display_fps(clock)
        
        pygame.display.update()        

    pygame.quit()

if __name__ == "__main__":
    main()      