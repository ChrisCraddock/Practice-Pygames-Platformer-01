
import pygame
from sys import exit
import os

#game variables
'''Added'''
TILE_SIZE = 32
GAME_WIDTH = 512
GAME_HEIGHT = 512

PLAYER_X = GAME_WIDTH/2
PLAYER_Y = GAME_HEIGHT/2
PLAYER_WIDTH = 42 #7:8 ratio 210 7x30 7*6
PLAYER_HEIGHT = 48 #7:8 ratio 240 8x30 8*6
#scaling for images not matching default image
PLAYER_JUMP_WIDTH = 52
PLAYER_JUMP_HEIGHT = 60

PLAYER_DISTANCE = 5 #movement speed
PLAYER_VELOCITY_Y = -11 #for jumping. large negative # = higher jump
PLAYER_VELOCITY_X = 5
FRICTION = 0.4
GRAVITY = 0.5
'''Removed'''
#FLOOR_Y = GAME_HEIGHT * 3/4

#Images
#Function to scale images when loaded
def load_image(image_name,scale=None): #not all images will need scaling
    image = pygame.image.load(os.path.join('assets/images',image_name)) #image_name = param in load_image and is file path
    if scale != None:
        image = pygame.transform.scale(image, scale) #reference image variable above and scale param
    return image

background_image = load_image('background.png')
player_image_right = load_image('megaman-right.png',(PLAYER_WIDTH,PLAYER_HEIGHT))

player_image_left = load_image('megaman-left.png',(PLAYER_WIDTH,PLAYER_HEIGHT))
player_image_jump_right = load_image('megaman-right-jump.png',(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player_image_jump_left = load_image('megaman-left-jump.png',(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
'''Added'''
floor_tile_image = load_image('floor-tile.png',(TILE_SIZE, TILE_SIZE))


pygame.init()
window = pygame.display.set_mode((GAME_HEIGHT,GAME_WIDTH))
pygame.display.set_caption("Fuzzy's Window Title") 
pygame.display.set_icon(player_image_right)
clock = pygame.time.Clock() 

#Player Class
class Player(pygame.Rect): #class Player(inherit pygame.Rect)
    def __init__(self): #will describe latter
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_image_right
        self.velocity_x = 0 #add velocity_x and set to 0
        self.velocity_y = 0 #add velocity_y and set to 0
        self.direction = "right" #set default direction to "right"
        self.jumping = False #keep from constant jumping

    
    def update_image(self):
        if self.jumping:
            '''remove'''
            #self.width = PLAYER_JUMP_WIDTH #standerdize collision checking
            #self.height = PLAYER_JUMP_HEIGHT #standerdize collision checking
            if self.direction == "right": #if the .direction above is changed to 'right and jumping'
                self.image = player_image_jump_right
            elif self.direction == "left": #if the .direction above is changed to 'left and jumping'
                self.image = player_image_jump_left
        else:
            '''remove'''
            #self.width = PLAYER_WIDTH #standerdize collision checking
            #self.height = PLAYER_HEIGHT #standerdize collision checking
            if self.direction == "right": #if the .direction above is changed to 'right'
                self.image = player_image_right
            elif self.direction == "left": #if the .direction above is changed to 'left'
                self.image = player_image_left

'''Moved to before game loop'''
#player = Player()
'''Create Class Tile'''
class Tile(pygame.Rect):
    def __init__(self,x, y, image): #create rectangle and save image
        pygame.Rect.__init__(self,x,y, TILE_SIZE, TILE_SIZE)
        self.image = image


'''Added Create_Map function'''
def create_map():
    for i in range(4): #create tile where player is and then shift over 1 | Horizontal tiles
        tile = Tile(player.x + i*TILE_SIZE, player.y + TILE_SIZE*2, floor_tile_image)
        tiles.append(tile) #add tile to tile list

    for i in range(16): #floor tiles
        tile = Tile(i*TILE_SIZE, player.y + TILE_SIZE*5, floor_tile_image)
        tiles.append(tile)

    for i in range(3): #vertical tiles starting 3 from the left | starts 10 tiles down
        tile = Tile(TILE_SIZE*3, (i+10)*TILE_SIZE, floor_tile_image)
        tiles.append(tile)

'''Added'''
def check_tile_collision(): #if player hits a tile, return the tile otherwise do nothing
    for tile in tiles:
        if player.colliderect(tile):
            return tile


def check_tile_collision_x(): #check for collision on x-axis
    tile = check_tile_collision()
    if tile is not None:
        if player.velocity_x < 0: #if less than x, place player to left of tile
            player.x = tile.x + tile.width
        elif player.velocity_x > 0: #if greater than 0, place player to right of tile
            player.x = tile.x - player.width
        player.velocity_x = 0 #stop player from moving after collision

def check_tile_collision_y(): #check for collision on y-axis
    tile = check_tile_collision()
    if tile is not None:
        if player.velocity_y < 0: #if less than y, place player to left of tile
            player.y = tile.y + tile.height
        elif player.velocity_y > 0: #if greater than 0, place player to right of tile
            player.y = tile.y - player.height
            player.jumping = False
        player.velocity_y = 0 #stop player from moving after collision

#Move Function
def move():
    #movement
    if player.direction == "left" and player.velocity_x < 0: #if moving to the left, slow down
        player.velocity_x += FRICTION
    elif player.direction == "right" and player.velocity_x > 0: #if moving to the right, speed up
        player.velocity_x -= FRICTION
    else: #if moving in direction not facing
        player.velocity_x = 0

    #x movement
    player.x += player.velocity_x #.velocity_x is called in class Player
    if player.x < 0:
        player.x = 0
    elif player.x + player.width > GAME_WIDTH: #if player hits wall, stop player
        player.x = GAME_WIDTH - player.width

    check_tile_collision_x() #check for collision on x-axis 1st

    #y movement
    player.velocity_y += GRAVITY #assign gravity to player velocity
    player.y += player.velocity_y #.velocity_y is called in class Player | .y is the top of the image, .height is the bottom of the image

    check_tile_collision_y() #check for collision on y-axis 2nd
    '''Removed'''
#    if player.y + player.height > FLOOR_Y:
#        player.y = FLOOR_Y - player.height  
#        player.jumping = False #Reference key up, if fall back on floor set value to False again

#Draw Function
def draw():
    window.fill((20,18,167))
    window.blit(background_image, (0,80))
    '''added'''
    for tile in tiles:
        window.blit(tile.image, tile)
    player.update_image() #reference Player class -> update_image function. Put BEFORE drawing the player image default
    window.blit(player.image, player)

player = Player()

'''Added'''
#list to store variables
tiles = []
create_map()

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #1st event
            pygame.quit() 
            exit()

    #Hold keys instead of constant pressing
    keys = pygame.key.get_pressed()  #2nd event
    #Boundry: Top
    if (keys[pygame.K_UP] or keys[pygame.K_w] or keys[pygame.K_SPACE]) and not player.jumping: #check to see if player is already jumping
        player.velocity_y = PLAYER_VELOCITY_Y #.velocity_y is called in class Player
        player.jumping = True #reference class Player to change from False to True

    #Boundry: Left
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.velocity_x = -PLAYER_VELOCITY_X
        player.direction = "left" #references .direction in Player class
    #Boundry: Right
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.velocity_x = PLAYER_VELOCITY_X
        player.direction = "right" #references .direction in Player class


    move()
    draw()
    pygame.display.update()  
    clock.tick(60) 