import pygame
import random
import enemies
import player

class Block:
    def __init__(self, x, y, scale):
        self.x = x
        self.y = y
        self.top_hitbox = True
        self.bottom_hitbox = True
        self.scale = scale
        self.image0 = pygame.image.load('assets/block_0.png').convert_alpha()
        self.image0 = pygame.transform.scale(self.image0, (self.scale, self.scale))
        self.image1 = pygame.image.load('assets/block_1.png').convert_alpha()
        self.image1 = pygame.transform.scale(self.image1, (self.scale, self.scale))
        # set image0 if prob < 0.7, else set image1
        prob = random.random()
        if prob <= 0.8:
            self.image = self.image0
        else:
            self.image = self.image1
        self.hitbox = self.image.get_rect(topleft = (self.x, self.y))

    def render_block(self):
        return self.image, self.hitbox

    def get_block_hitbox(self):
        return self.hitbox
    
    def get_block_image(self):
        return self.image
    
    def get_scale(self):
        return self.scale
    
    def get_top_hitbox(self):
        return self.top_hitbox
    
    def get_bottom_hitbox(self):
        return self.bottom_hitbox
    
    def set_top_hitbox(self, top_hitbox):
        self.top_hitbox = top_hitbox
    
    def set_bottom_hitbox(self, bottom_hitbox):
        self.bottom_hitbox = bottom_hitbox

    def translate(self, x, y):
        self.x += x
        self.y += y
        self.hitbox = self.image.get_rect(topleft = (self.x, self.y))

class Background:
    def __init__(self, x, y, w = 1920, h = 1080):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.image.load('assets/background.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.w, self.h))

    def render_background(self):
        return self.image

    def get_background_image(self):
        return self.image

class Room:
    def __init__(self, blocks_position, spikes_position, spawn_positions, blocks_scale, w, h, going_from):
        self.background = Background(x=0, y=0, w=w, h=h)
        self.x = 0
        self.y = 0
        self.w = w
        self.h = h
        self.blocks_scale = blocks_scale
        self.going_from = going_from
        blocks = []
        spikes = []
        spawns = []
        for i in range(len(blocks_position)):
            block = Block(x=blocks_position[i][0]*blocks_scale, y=blocks_position[i][1]*blocks_scale - blocks_scale/2, scale=blocks_scale)
            blocks.append(block)
        for i in range(len(spikes_position)):
            spike = enemies.Spikes(x=spikes_position[i][0]*blocks_scale, y=spikes_position[i][1]*blocks_scale, scale=blocks_scale)
            spikes.append(spike)
        for i in range(len(spawn_positions)):
            spawns.append((spawn_positions[i][0]*blocks_scale, spawn_positions[i][1]*blocks_scale))
        #chech if there is blocks bellow or above and turn on hitbox
        for i in range(len(blocks)):
            for j in range(len(blocks)):
                if i != j:
                    if blocks[i].x == blocks[j].x and blocks[i].y == blocks[j].y + blocks[j].get_scale():
                        blocks[i].set_top_hitbox(False)
                    if blocks[i].x == blocks[j].x and blocks[i].y == blocks[j].y - blocks[j].get_scale():
                        blocks[i].set_bottom_hitbox(False)
        self.block = blocks
        self.spike = spikes
        self.spawns = spawns

    def render(self, WIN):
        WIN.blit(self.background.render_background(), (0, 0))
        for i in range(len(self.block)):
            WIN.blit(self.block[i].render_block()[0], (self.block[i].x, self.block[i].y))
        for i in range(len(self.spike)):
            WIN.blit(self.spike[i].render()[0], (self.spike[i].x, self.spike[i].y))

    def get_hitboxes(self):
        block = []
        spikes = []
        for i in range(len(self.block)):
            block.append((self.block[i].get_block_hitbox(), self.block[i].get_top_hitbox(), self.block[i].get_bottom_hitbox()))
        for i in range(len(self.spike)):
            spikes.append(self.spike[i].get_hitbox())
        return block , spikes

    def hitboxes(self):
        hitboxes = []
        for i in range(len(self.block)):
            hitboxes.append(self.block[i].get_block_hitbox())
        for i in range(len(self.spike)):
            hitboxes.append(self.spike[i].get_hitbox())
        return hitboxes

    def translate(self, x, y):
        self.x += x
        self.y += y
        for i in range(len(self.block)):
            self.block[i].translate(x, y)
        for i in range(len(self.spike)):
            self.spike[i].translate(x, y)
        #translate spawns
        for i in range(len(self.spawns)):
            self.spawns[i] = (self.spawns[i][0] + x, self.spawns[i][1] + y)
    
    def translate_init(self, player1, scale):
                
        if self.going_from == 'left':
            #search for the block with the bigest y value and lower x value
            max_y = 0
            min_x = 100000
            for i in range(len(self.block)):
                if self.block[i].y > max_y:
                    max_y = self.block[i].y
                if self.block[i].x < min_x:
                    min_x = self.block[i].x
                
            # translate the room to the bottom left corner
            for i in range(len(self.block)):
                self.block[i].translate(-min_x, self.h - max_y - scale)
            for i in range(len(self.spike)):
                self.spike[i].translate(-min_x, self.h - max_y - scale)
            for i in range(len(self.spawns)):
                spawni = [self.spawns[i][0], self.spawns[i][1]]
                spawni[1] -= max_y
                spawni[1] += self.h - scale
                spawni[0] -= min_x
                self.spawns[i] = (spawni[0], spawni[1])

            #search for the spawn with the lowest x value
            min_x = 100000
            y = 0
            for i in range(len(self.spawns)):
                if self.spawns[i][0] < min_x:
                    min_x = self.spawns[i][0]
                    y = self.spawns[i][1]
            player1.reset_player([min_x+scale*2, y-int(scale/3)])

        elif self.going_from == 'right':
            #search for the block with the bigger y value and bigger x value
            max_y = 0
            max_x = 0
            for i in range(len(self.block)):
                if self.block[i].y > max_y:
                    max_y = self.block[i].y
                if self.block[i].x > max_x:
                    max_x = self.block[i].x
                
            # translate the room to the bottom right corner
            for i in range(len(self.block)):
                self.block[i].translate(self.w - max_x - scale, self.h - max_y - scale)
            for i in range(len(self.spike)):
                self.spike[i].translate(self.w - max_x - scale, self.h - max_y - scale)
            for i in range(len(self.spawns)):
                spawni = [self.spawns[i][0], self.spawns[i][1]]
                spawni[1] -= max_y
                spawni[1] += self.h - scale
                spawni[0] -= max_x
                spawni[0] += self.w - scale
                self.spawns[i] = (spawni[0], spawni[1])
            
            #search for the spawn with the biggest x value
            max_x = 0
            y = 0
            for i in range(len(self.spawns)):
                if self.spawns[i][0] > max_x:
                    max_x = self.spawns[i][0]
                    y = self.spawns[i][1]
            player1.reset_player([max_x-scale*2, y-int(scale/3)])
        
        elif self.going_from == 'top':
            #search for the block with the smallest y value and lower x value
            min_y = 100000
            min_x = 100000
            for i in range(len(self.block)):
                if self.block[i].y < min_y:
                    min_y = self.block[i].y
                if self.block[i].x < min_x:
                    min_x = self.block[i].x
                
            # translate the room to the top left corner
            for i in range(len(self.block)):
                self.block[i].translate(-min_x, -min_y)
            for i in range(len(self.spike)):
                self.spike[i].translate(-min_x, -min_y)
            for i in range(len(self.spawns)):
                spawni = [self.spawns[i][0], self.spawns[i][1]]
                spawni[1] -= min_y
                spawni[0] -= min_x
                self.spawns[i] = (spawni[0], spawni[1])
            
            #search for the spawn with the lowest y value
            min_y = 100000
            x = 0
            for i in range(len(self.spawns)):
                if self.spawns[i][1] < min_y:
                    min_y = self.spawns[i][1]
                    x = self.spawns[i][0]
            player1.reset_player([x, min_y+int(scale/3)])
        
        elif self.going_from == 'bottom':
            #search for the block with the bigest y value and lower x value
            max_y = 0
            min_x = 100000
            for i in range(len(self.block)):
                if self.block[i].y > max_y:
                    max_y = self.block[i].y
                if self.block[i].x < min_x:
                    min_x = self.block[i].x
                
            # translate the room to the bottom left corner
            for i in range(len(self.block)):
                self.block[i].translate(-min_x, self.h - max_y - scale)
            for i in range(len(self.spike)):
                self.spike[i].translate(-min_x, self.h - max_y - scale)
            for i in range(len(self.spawns)):
                spawni = [self.spawns[i][0], self.spawns[i][1]]
                spawni[1] -= max_y
                spawni[1] += self.h - scale
                spawni[0] -= min_x
                self.spawns[i] = (spawni[0], spawni[1])
            #search for the spawn with the biggest y value
            max_y = 0
            x = 0
            for i in range(len(self.spawns)):
                if self.spawns[i][1] > max_y:
                    max_y = self.spawns[i][1]
                    x = self.spawns[i][0]
            player1.reset_player([x-scale, max_y-scale*3])
       

    def follow(self):
        bigest_x = 0
        bigest_y = 0
        smallest_x = 100000
        smallest_y = 100000
        follow_x_n, follow_x_p, follow_y_n, follow_y_p = False, False, False, False
        for i in range(len(self.block)):
            if self.block[i].x > bigest_x:
                bigest_x = self.block[i].x
            if self.block[i].y > bigest_y:
                bigest_y = self.block[i].y
            if self.block[i].x < smallest_x:
                smallest_x = self.block[i].x
            if self.block[i].y < smallest_y:
                smallest_y = self.block[i].y
        if(bigest_x > self.w-self.blocks_scale):
            follow_x_p = True
        if(smallest_x < 0):
            follow_x_n = True
        if(bigest_y > self.h - self.blocks_scale):
            follow_y_p = True
        if(smallest_y < 0):
            follow_y_n = True
        return follow_x_n, follow_x_p, follow_y_n, follow_y_p


class Level:
    def __init__(self, fase = 1, blocks_scale = 100, WHIDTH=1920, HEIGHT=1080):
        self.fase = fase
        self.background = None
        self.rooms = {}
        self.spikes = {}
        self.spawns = {}
        self.current_room = (0,0)
        self.blocks_scale = blocks_scale
        self.WHIDTH = WHIDTH
        self.HEIGHT = HEIGHT

    def get_fase(self):
        return self.fase
    
    def set_fase(self, fase):
        self.fase = fase

    def set_level(self, player1):
        if self.fase == 1:
            mapnum = '01'
            with open('map_generator/map'+mapnum+'.txt') as f:
                data = f.readlines()
            mapa = []
            for d in data:
                #remove newline
                d = d[:-1]
                d = d.split(',')
                #transform string to int
                if(d[0]!="room" and d[0]!="spikes" and d[0]!="spawn"): d = tuple(map(int, d))
                else : d = (d[0], int(d[1]), int(d[2]))
                mapa.append(d)
            #create a dictionary with the rooms
            rooms = {}
            spikes = {}
            spawn = {}
            is_spike = False
            is_spawn = False
            current_room = (0,0)
            for i in range(len(mapa)):
                if mapa[i][0] == "room":
                    current_room = (mapa[i][1], mapa[i][2])
                    rooms[current_room] = []
                    is_spike = False
                    is_spawn = False
                elif mapa[i][0] == "spikes":
                    spikes[current_room] = []
                    is_spike = True
                    is_spawn = False
                elif mapa[i][0] == "spawn":
                    is_spike = False
                    is_spawn = True
                    spawn[current_room] = []
                else:
                    if is_spike:
                        spikes[current_room].append(mapa[i])
                    elif is_spawn:
                        spawn[current_room].append(mapa[i])
                    else:
                        rooms[current_room].append(mapa[i])
            for room in rooms:
                rooms[room].sort(key=lambda a: a[1], reverse=True)
            for spike in spikes:
                spikes[spike].sort(key=lambda a: a[1], reverse=True)
            for sp in spawn:
                spawn[sp].sort(key=lambda a: a[1], reverse=True)
        self.spawns = spawn
        self.rooms = rooms
        self.spikes = spikes
        self.room = Room(self.rooms[self.current_room], self.spikes[self.current_room],self.spawns[self.current_room], self.blocks_scale, self.WHIDTH, self.HEIGHT, "bottom")
        self.room.translate_init(player1, self.blocks_scale)
        
    def translate(self, x, y):
        self.room.translate(x, y)

    def render_level(self, WIN):
        return self.room.render(WIN)

    def get_hitboxes(self):
        block, spikes = self.room.get_hitboxes()
        return block, spikes
    
    def hitboxes(self):
        hitboxes = self.room.hitboxes()
        return hitboxes
    
    def go_to_room(self, x , y, player1):
        going_from = ''
        if self.current_room[0] < x:
            going_from = 'left'
        elif self.current_room[0] > x:
            going_from = 'right'
        elif self.current_room[1] < y:
            going_from = 'bottom'
        elif self.current_room[1] > y:
            going_from = 'top'
        if(x == 0 and y == 0):
            going_from = 'bottom'
        self.current_room = (x, y)
        self.room = Room(self.rooms[self.current_room], self.spikes[self.current_room],self.spawns[self.current_room], self.blocks_scale, self.WHIDTH, self.HEIGHT, going_from)
        self.room.translate_init(player1, self.blocks_scale)

    def follow(self):
        return self.room.follow()

    def check_room(self, player1):
        if player1.x > self.WHIDTH:
            self.go_to_room(self.current_room[0]+1, self.current_room[1], player1)
        elif player1.x < 0:
            self.go_to_room(self.current_room[0]-1, self.current_room[1], player1)
        elif player1.y > self.HEIGHT:
            self.go_to_room(self.current_room[0], self.current_room[1]-1, player1)
        elif player1.y < 0:
            self.go_to_room(self.current_room[0], self.current_room[1]+1, player1)
