import pygame
import time


# make player class

class Player():

    # constructor

    def __init__(self, ratio=16/25, x=0, y=0, scale=100, sword=False, shield=False, health=100, state='walk', index = 0, vertical_aceleration = 0, vertical_speed = 0, horizontal_aceleration = 0, horizontal_speed = 5):
        self.ratio = ratio
        self.x = x
        self.y = y
        self.scale = scale
        self.sword = sword
        self.shield = shield
        self.health = health
        self.state = state
        self.index = index
        self.vertical_aceleration = vertical_aceleration
        self.vertical_speed = vertical_speed
        self.horizontal_aceleration = horizontal_aceleration
        self.horizontal_speed = horizontal_speed
        self.player_crouch = self.init_player_crouch()
        #self.player_crouch_sword = self.init_player_crouch_sword()
        #self.player_crouch_shield = self.init_player_crouch_shield()
        #self.player_crouch_sword_shield = self.init_player_crouch_sword_shield()
        self.player_walk = self.init_player_walk()
        #self.player_walk_sword = self.init_player_walk_sword()
        #self.player_walk_shield = self.init_player_walk_shield()
        #self.player_walk_sword_shield = self.init_player_walk_sword_shield()
        self.player_jump = self.init_player_jump()
        #self.player_jump_sword = self.init_player_jump_sword()
        #self.player_jump_shield = self.init_player_jump_shield()
        #self.player_jump_sword_shield = self.init_player_jump_sword_shield()
        self.player_hitbox = self.init_player_hitbox()
        self.player_image = []
        self.last_move = 'right'
        self.dash = False
        self.can_dash = True
        self.can_double_jump = True
        self.dashed = False
        self.crouch = False
        self.crouched = False
        self.get_hit = False
        self.invencible = False

    #getters

    def get_ratio(self):
        return self.ratio
    
    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def get_scale(self):
        return self.scale
    
    def get_sword(self):
        return self.sword
    
    def get_shield(self):
        return self.shield
    
    def get_health(self):
        return self.health

    def get_state(self):
        return self.state
    
    def get_index(self):
        return self.index
    
    def get_vertical_aceleration(self):
        return self.vertical_aceleration

    def get_vertical_speed(self):
        return self.vertical_speed
    
    def get_horizontal_aceleration(self):
        return self.horizontal_aceleration
    
    def get_horizontal_speed(self):
        return self.horizontal_speed

    def get_player_crouch(self):
        return self.player_crouch
    
    def get_player_crouch_sword(self):
        return self.player_crouch_sword
    
    def get_player_crouch_shield(self):
        return self.player_crouch_shield
    
    def get_player_walk(self):
        return self.player_walk
    
    def get_player_walk_sword(self):
        return self.player_walk_sword
    
    def get_player_walk_shield(self):
        return self.player_walk_shield
    
    def get_player_walk_sword_shield(self):
        return self.player_walk_sword_shield
    
    def get_player_jump(self):
        return self.player_jump

    def get_player_jump_sword(self):
        return self.player_jump_sword
    
    def get_player_jump_shield(self):
        return self.player_jump_shield
    
    def get_player_jump_sword_shield(self):
        return self.player_jump_sword_shield
    
    def get_player_hitbox(self):
        return self.player_hitbox

    def get_player_image(self):
        return self.player_image

    def get_can_dash(self):
        return self.can_dash
    
    def get_can_double_jump(self):
        return self.can_double_jump
    
    def get_get_hit(self):
        return self.get_hit

    def get_position(self):
        return self.player_hitbox.x, self.player_hitbox.y

    #setters

    def set_sword(self, sword):
        self.sword = sword
    
    def set_shield(self, shield):
        self.shield = shield

    def init_player_hitbox(self):
        self.player_hitbox = pygame.Rect(self.x, self.y, self.scale*self.ratio, self.scale)
        return self.player_hitbox
    
    def set_can_dash(self, can_dash):
        self.can_dash = can_dash
    
    def set_can_double_jump(self, can_double_jump):
        self.can_double_jump = can_double_jump
    
    def set_get_hit(self, get_hit):
        self.get_hit = get_hit
    
    def set_invencible(self, invencible):
        self.invencible = invencible

    #methods

    def init_player_crouch(self):
        player_crouch_0 = pygame.image.load('assets/player_crouch_0.png').convert_alpha()
        #scale
        player_crouch_0 = pygame.transform.scale(player_crouch_0, (self.scale*self.ratio, self.scale*self.ratio))
        return player_crouch_0
    
    '''def init_player_crouch_sword(self):
        player_crouch_sword_0 = pygame.image.load('assets/player_crouch_sword_0.png').convert_alpha()
        #scale
        player_crouch_sword_0 = pygame.transform.scale(player_crouch_sword_0, (self.scale*self.ratio, self.scale*self.ratio))
        return player_crouch_sword_0
    
    def init_player_crouch_shield(self):
        player_crouch_shield_0 = pygame.image.load('assets/player_crouch_shield_0.png').convert_alpha()
        #scale
        player_crouch_shield_0 = pygame.transform.scale(player_crouch_shield_0, (self.scale*self.ratio, self.scale*self.ratio))
        return player_crouch_shield_0
    
    def init_player_crouch_sword_shield(self):
        player_crouch_sword_shield_0 = pygame.image.load('assets/player_crouch_sword_shield_0.png').convert_alpha()
        #scale
        player_crouch_sword_shield_0 = pygame.transform.scale(player_crouch_sword_shield_0, (self.scale*self.ratio, self.scale*self.ratio))
        return player_crouch_sword_shield_0'''

    def init_player_walk(self):
        
        player_walk_0 = pygame.image.load('assets/player_walk_0.png').convert_alpha()
        player_walk_1 = pygame.image.load('assets/player_walk_1.png').convert_alpha()
        player_walk_2 = pygame.image.load('assets/player_walk_2.png').convert_alpha()
        player_walk_3 = pygame.image.load('assets/player_walk_3.png').convert_alpha()
        player_walk = [player_walk_0, player_walk_1, player_walk_2, player_walk_3]
        # scale player
        for i in range(len(player_walk)):
            player_walk[i] = pygame.transform.scale(player_walk[i], (self.scale*self.ratio, self.scale))
        return player_walk

    '''def init_player_walk_sword(self):
        player_walk_sword_0 = pygame.image.load('assets/player_walk_sword_0.png').convert_alpha()
        player_walk_sword_1 = pygame.image.load('assets/player_walk_sword_1.png').convert_alpha()
        player_walk_sword_2 = pygame.image.load('assets/player_walk_sword_2.png').convert_alpha()
        player_walk_sword_3 = pygame.image.load('assets/player_walk_sword_3.png').convert_alpha()
        player_walk_sword_4 = pygame.image.load('assets/player_walk_sword_4.png').convert_alpha()
        player_walk_sword_5 = pygame.image.load('assets/player_walk_sword_5.png').convert_alpha()
        player_walk_sword_6 = pygame.image.load('assets/player_walk_sword_6.png').convert_alpha()
        player_walk_sword_7 = pygame.image.load('assets/player_walk_sword_7.png').convert_alpha()
        player_walk_sword_8 = pygame.image.load('assets/player_walk_sword_8.png').convert_alpha()
        player_walk_sword = [player_walk_sword_0, player_walk_sword_1, player_walk_sword_2, player_walk_sword_3, player_walk_sword_4, player_walk_sword_5, player_walk_sword_6, player_walk_sword_7, player_walk_sword_8]
        # scale player
        for i in range(len(player_walk_sword)):
            player_walk_sword[i] = pygame.transform.scale(player_walk_sword[i], (self.scale*self.ratio, self.scale))
        return player_walk_sword

    def init_player_walk_shield(self):
        player_walk_shield_0 = pygame.image.load('assets/player_walk_shield_0.png').convert_alpha()
        player_walk_shield_1 = pygame.image.load('assets/player_walk_shield_1.png').convert_alpha()
        player_walk_shield_2 = pygame.image.load('assets/player_walk_shield_2.png').convert_alpha()
        player_walk_shield_3 = pygame.image.load('assets/player_walk_shield_3.png').convert_alpha()
        player_walk_shield_4 = pygame.image.load('assets/player_walk_shield_4.png').convert_alpha()
        player_walk_shield_5 = pygame.image.load('assets/player_walk_shield_5.png').convert_alpha()
        player_walk_shield_6 = pygame.image.load('assets/player_walk_shield_6.png').convert_alpha()
        player_walk_shield_7 = pygame.image.load('assets/player_walk_shield_7.png').convert_alpha()
        player_walk_shield_8 = pygame.image.load('assets/player_walk_shield_8.png').convert_alpha()
        player_walk_shield = [player_walk_shield_0, player_walk_shield_1, player_walk_shield_2, player_walk_shield_3, player_walk_shield_4, player_walk_shield_5, player_walk_shield_6, player_walk_shield_7, player_walk_shield_8]
        # scale player
        for i in range(len(player_walk_shield)):
            player_walk_shield[i] = pygame.transform.scale(player_walk_shield[i], (self.scale*self.ratio, self.scale))
        return player_walk_shield

    def init_player_walk_sword_shield(self):
        player_walk_sword_shield_0 = pygame.image.load('assets/player_walk_sword_shield_0.png').convert_alpha()
        player_walk_sword_shield_1 = pygame.image.load('assets/player_walk_sword_shield_1.png').convert_alpha()
        player_walk_sword_shield_2 = pygame.image.load('assets/player_walk_sword_shield_2.png').convert_alpha()
        player_walk_sword_shield_3 = pygame.image.load('assets/player_walk_sword_shield_3.png').convert_alpha()
        player_walk_sword_shield_4 = pygame.image.load('assets/player_walk_sword_shield_4.png').convert_alpha()
        player_walk_sword_shield_5 = pygame.image.load('assets/player_walk_sword_shield_5.png').convert_alpha()
        player_walk_sword_shield_6 = pygame.image.load('assets/player_walk_sword_shield_6.png').convert_alpha()
        player_walk_sword_shield_7 = pygame.image.load('assets/player_walk_sword_shield_7.png').convert_alpha()
        player_walk_sword_shield_8 = pygame.image.load('assets/player_walk_sword_shield_8.png').convert_alpha()
        player_walk_sword_shield = [player_walk_sword_shield_0, player_walk_sword_shield_1, player_walk_sword_shield_2, player_walk_sword_shield_3, player_walk_sword_shield_4, player_walk_sword_shield_5, player_walk_sword_shield_6, player_walk_sword_shield_7, player_walk_sword_shield_8]
        # scale player
        for i in range(len(player_walk_sword_shield)):
            player_walk_sword_shield[i] = pygame.transform.scale(player_walk_sword_shield[i], (self.scale*self.ratio, self.scale))
        return player_walk_sword_shield

    def init_player_jump_sword(self):
        player_jump_sword_0 = pygame.image.load('assets/player_jump_sword_0.png').convert_alpha()
        #sclae player
        player_jump_sword_0 = pygame.transform.scale(player_jump_sword_0, (self.scale*self.ratio, self.scale))
        return player_jump_sword_0

    def init_player_jump_shield(self):
        player_jump_shield_0 = pygame.image.load('assets/player_jump_shield_0.png').convert_alpha()
        #sclae player
        player_jump_shield_0 = pygame.transform.scale(player_jump_shield_0, (self.scale*self.ratio, self.scale))
        return player_jump_shield_0

    def init_player_jump_sword_shield(self):
        player_jump_sword_shield_0 = pygame.image.load('assets/player_jump_sword_shield_0.png').convert_alpha()
        #sclae player
        player_jump_sword_shield_0 = pygame.transform.scale(player_jump_sword_shield_0, (self.scale*self.ratio, self.scale))
        return player_jump_sword_shield_0'''

    def init_player_jump(self):
        player_jump_0 = pygame.image.load('assets/player_jump_0.png').convert_alpha()
        player_jump_1 = pygame.image.load('assets/player_jump_1.png').convert_alpha()
        player_jump_2 = pygame.image.load('assets/player_jump_2.png').convert_alpha()
        player_jump_3 = pygame.image.load('assets/player_jump_3.png').convert_alpha()
        player_jump = [player_jump_0, player_jump_1, player_jump_2, player_jump_3]
        #sclae player
        for i in range(len(player_jump)):
            player_jump[i] = pygame.transform.scale(player_jump[i], (self.scale*self.ratio, self.scale))
        return player_jump
        

    def handle_player_colision(self, hitboxes):
        colision_tolerance = 30
        horizontal_colision = 'none'
        horizontal_colisor = None
        vertical_colision = 'none'
        vertical_colisor = None
        for i in range(len(hitboxes)):
            if(self.player_hitbox.colliderect(hitboxes[i][0])):
                if(self.player_hitbox.bottom > hitboxes[i][0].top and self.player_hitbox.bottom < hitboxes[i][0].bottom and hitboxes[i][1] == True):
                    #check if is close to the top of the hitbox
                    if(self.player_hitbox.bottom - hitboxes[i][0].top < colision_tolerance):
                        vertical_colision = 'top'
                        vertical_colisor = hitboxes[i][0]
                        continue
                elif(self.player_hitbox.top < hitboxes[i][0].bottom and self.player_hitbox.top > hitboxes[i][0].top and hitboxes[i][2] == True):
                    #check if is close to the bottom of the hitbox
                    if(hitboxes[i][0].bottom - self.player_hitbox.top < colision_tolerance):
                        vertical_colision = 'bottom'
                        vertical_colisor = hitboxes[i][0]
                        continue

                if(self.player_hitbox.right > hitboxes[i][0].left and self.player_hitbox.right < hitboxes[i][0].right):
                    horizontal_colision = 'left'
                    horizontal_colisor = hitboxes[i][0]
                elif(self.player_hitbox.left < hitboxes[i][0].right and self.player_hitbox.left > hitboxes[i][0].left):
                    horizontal_colision = 'right'
                    horizontal_colisor = hitboxes[i][0]

        return horizontal_colision, horizontal_colisor, vertical_colision, vertical_colisor

    def handle_player_movement(self, keys_pressed, relase_up_key, release_space_key):
        JUMP_VEL = 18
        VEL_MAX = 15
        VEL = 7

        self.crouch = False
        
        if keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_UP]:
            if not self.dash: self.horizontal_speed = -VEL
            self.last_move = "left"
            if(self.state == "walk"):
                self.vertical_speed = -JUMP_VEL
                self.state = "jump"
            elif(self.state == "jump" and relase_up_key and self.can_double_jump):
                self.vertical_speed = -JUMP_VEL
                self.state = "jump2"
        elif keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_DOWN]:
            self.last_move = "left"
            self.crouch = True
            if not self.dash: self.horizontal_speed = -VEL/2
        elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_UP]:
            if not self.dash: self.horizontal_speed = VEL
            self.last_move = "right"
            if(self.state == "walk"):
                self.vertical_speed -= JUMP_VEL
                self.state = "jump"
            elif(self.state == "jump" and relase_up_key and self.can_double_jump):
                self.vertical_speed = -JUMP_VEL
                self.state = "jump2"
        elif keys_pressed[pygame.K_RIGHT] and keys_pressed[pygame.K_DOWN]:
            self.last_move = "right"
            self.crouch = True
            if not self.dash: self.horizontal_speed = VEL/2
        elif keys_pressed[pygame.K_LEFT] and keys_pressed[pygame.K_RIGHT]:
            self.index = 0
            if not self.dash: self.horizontal_speed = 0
        elif keys_pressed[pygame.K_UP] and keys_pressed[pygame.K_DOWN]:
            self.crouch = True
            self.index = 0
            if not self.dash: self.horizontal_speed = 0 
        elif keys_pressed[pygame.K_LEFT]:
            self.last_move = "left"
            if not self.dash: self.horizontal_speed = -VEL
        elif keys_pressed[pygame.K_RIGHT]:
            self.last_move = "right"
            if not self.dash: self.horizontal_speed = VEL
        elif keys_pressed[pygame.K_UP]:
            if(self.state == "walk"):
                self.vertical_speed = -JUMP_VEL
                self.state = "jump"
            elif(self.state == "jump" and relase_up_key and self.can_double_jump):
                self.vertical_speed = -JUMP_VEL
                self.state = "jump2"   
        elif keys_pressed[pygame.K_DOWN]:
            self.index = 0
            self.crouch = True
            if not self.dash: self.horizontal_speed = 0   
        else:
            self.index = 0
            if not self.dash: self.horizontal_speed = 0
        
        if(self.state == "walk"):
            self.dashed = False

        if((keys_pressed[pygame.K_SPACE] and release_space_key and self.dashed == False and self.can_dash == True) or (self.get_hit and self.dashed == False)):
            self.dash = True
            self.dashed = True
            if(self.get_hit):
                if(self.last_move == "left"):
                    self.horizontal_speed = +1.5*VEL
                    self.horizontal_aceleration = -0.5
                    self.vertical_speed = -JUMP_VEL/2
                    self.vertical_aceleration = 0.5
                    self.state = "jump"
                elif(self.last_move == "right"):
                    self.horizontal_speed = -1.5*VEL
                    self.horizontal_aceleration = +0.5
                    self.vertical_speed = -JUMP_VEL/2
                    self.vertical_aceleration = 0.5
                    self.state = "jump"
            else:
                if(self.last_move == "left"):
                    self.horizontal_speed = -4*VEL
                    self.horizontal_aceleration = 1
                    self.vertical_speed = 0
                    self.vertical_aceleration = 0
                elif(self.last_move == "right"):
                    self.horizontal_speed = 4*VEL
                    self.vertical_speed = 0
                    self.vertical_aceleration = 0
                    self.horizontal_aceleration = -1
        
        if(self.dash):
            if(self.horizontal_speed <= 10 and self.horizontal_speed >= -10):
                if(self.last_move == "left"):
                    self.horizontal_speed = -VEL
                else:
                    self.horizontal_speed = VEL
                self.horizontal_aceleration = 0
                self.dash = False

        if(self.vertical_speed > VEL_MAX):
            self.vertical_speed = VEL_MAX

    def render_player(self, floor_hitbox, spikes_hitbox, keys_pressed, relase_up_key, release_space_key, frame):
        ACELERATION = 1
        #FRAME COUNT    
        if frame % 8 == 0:
            self.index += 1
            if self.index >= len(self.player_walk):
                self.index = 0
        
        #PLAYER MOVEMENT]
        for spike in spikes_hitbox:
            if self.player_hitbox.colliderect(spike) and self.invencible == False:
                self.get_hit = True

        self.handle_player_movement(keys_pressed, relase_up_key, release_space_key)

        #PLAYER KINEMATICS
        
        self.horizontal_speed += self.horizontal_aceleration
        self.player_hitbox.left += self.horizontal_speed
        self.x = self.player_hitbox.left
        self.vertical_speed += self.vertical_aceleration
        self.player_hitbox.top += self.vertical_speed
        self.y = self.player_hitbox.top

        #PLAYER COLLISION
        horizontal_colision, horizontal_colisor, vertical_colision, vertical_colisor = self.handle_player_colision(floor_hitbox)
        
        if vertical_colision == 'top':
            self.vertical_speed = 0
            self.vertical_aceleration = 0
            self.state = "walk"
            self.player_hitbox.bottom = vertical_colisor.top+1
        elif vertical_colision == 'bottom':
            self.vertical_aceleration = ACELERATION
            self.vertical_speed = 0
            self.player_hitbox.top = vertical_colisor.bottom
        
        if horizontal_colision == 'left':
            self.player_hitbox.right = horizontal_colisor.left
            self.horizontal_speed = 0
        elif horizontal_colision == 'right':
            self.player_hitbox.left = horizontal_colisor.right
            self.horizontal_speed = 0
        
        if vertical_colision == 'none' and self.dash == False:
            self.vertical_aceleration = ACELERATION
            if(self.state == "walk"):
                self.state = "jump"


        #print(self.state,self.x,self.y ,vertical_colision, horizontal_colision, self.horizontal_speed, self.horizontal_aceleration, self.vertical_speed, self.vertical_aceleration)
        
        #PLAYER ANIMATION

        if(self.state == "jump" or self.state == "jump2"):
            if(self.last_move == "right"):
                if(self.sword and not self.shield):
                    self.player_image = self.player_jump_sword
                elif(not self.sword and self.shield):
                    self.player_image = self.player_jump_shield
                elif(self.sword and self.shield):
                    self.player_image = self.player_jump_sword_shield
                else:
                    self.player_image = self.player_jump[self.index]
            else:
                if(self.sword and not self.shield):
                    self.player_image = pygame.transform.flip(self.player_jump_sword, True, False)
                elif(not self.sword and self.shield):
                    self.player_image = pygame.transform.flip(self.player_jump_shield, True, False)
                elif(self.sword and self.shield):
                    self.player_image = pygame.transform.flip(self.player_jump_sword_shield, True, False)
                else:
                    self.player_image = pygame.transform.flip(self.player_jump[self.index], True, False)
        elif(self.state == "walk" and self.crouch == False):
            if(self.last_move == "right"):
                if(self.sword and not self.shield):
                    self.player_image = self.player_walk_sword[self.index]
                elif(not self.sword and self.shield):
                    self.player_image = self.player_walk_shield[self.index]
                elif(self.sword and self.shield):
                    self.player_image = self.player_walk_sword_shield[self.index]
                else:
                    self.player_image = self.player_walk[self.index]
            else:
                if(self.sword and not self.shield):
                    self.player_image = pygame.transform.flip(self.player_walk_sword[self.index], True, False)
                elif(not self.sword and self.shield):
                    self.player_image = pygame.transform.flip(self.player_walk_shield[self.index], True, False)
                elif(self.sword and self.shield):
                    self.player_image = pygame.transform.flip(self.player_walk_sword_shield[self.index], True, False)
                else:
                    self.player_image = pygame.transform.flip(self.player_walk[self.index], True, False)
        else:
            if(self.last_move == "right"):
                if(self.sword and not self.shield):
                    self.player_image = self.player_crouch_sword
                elif(not self.sword and self.shield):
                    self.player_image = self.player_crouch_shield
                elif(self.sword and self.shield):
                    self.player_image = self.player_crouch_sword_shield
                else:
                    self.player_image = self.player_crouch
            else:
                if(self.sword and not self.shield):
                    self.player_image = pygame.transform.flip(self.player_crouch_sword, True, False)
                elif(not self.sword and self.shield):
                    self.player_image = pygame.transform.flip(self.player_crouch_shield, True, False)
                elif(self.sword and self.shield):
                    self.player_image = pygame.transform.flip(self.player_crouch_sword_shield, True, False)
                else:
                    self.player_image = pygame.transform.flip(self.player_crouch, True, False)
                
            if(self.crouch == True and self.crouched == False):
                # short hitbox when crouching
                self.player_hitbox.height = self.scale*self.ratio
                #translate hitbox to the bottom
                self.player_hitbox.top = self.player_hitbox.top + self.scale*(1-self.ratio)+1
                self.crouched = True
        
        if(self.crouch == False and self.crouched == True):
            self.player_hitbox.height = self.scale
            self.player_hitbox.top = self.player_hitbox.top - self.scale*(1-self.ratio)
            self.crouched = False

        #print(self.get_hit)

        return self.player_hitbox, self.player_image

    # reset player position to the start
    def reset_player(self, pos):
        self.player_hitbox.left = pos[0]
        self.player_hitbox.top = pos[1]
        self.horizontal_speed = 0
        self.vertical_speed = 0
        self.horizontal_aceleration = 0
        self.vertical_aceleration = 0
        self.dash = False
        self.dashed = False
        self.last_move = "right"
        self.state = "walk"