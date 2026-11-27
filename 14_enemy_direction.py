import pygame
from sys import exit
import os

#game variables
TILE_SIZE = 32
GAME_WIDTH = 512
GAME_HEIGHT = 512

PLAYER_X = GAME_WIDTH/2
PLAYER_Y = GAME_HEIGHT/2
PLAYER_WIDTH = 42 #7:8 ratio 210 7x30 7*6
PLAYER_HEIGHT = 48 #7:8 ratio 240 8x30 8*6
PLAYER_JUMP_WIDTH = 52 #used for scaling for images not matching default image
PLAYER_JUMP_HEIGHT = 60 #used for scaling for images not matching default image
PLAYER_DISTANCE = 5 #movement speed

PLAYER_SHOOT_WIDTH = 62 #same as PLAYER_HEIGHT
PLAYER_JUMP_SHOOT_WIDTH = 58 #same as PLAYER_JUMP_HEIGHT
PLAYER_BULLET_WIDTH = 16
PLAYER_BULLET_HEIGHT  = 12
PLAYER_BULLET_VELOCITY_x = 8

GRAVITY = 0.5
FRICTION = 0.4
PLAYER_VELOCITY_X = 5
PLAYER_VELOCITY_Y = -11 #for jumping. large negative # = higher jump

HEALTH_WIDTH = 16
HEALTH_HEIGHT = 4

#enemy variables
METALL_WIDTH = 36 #18:15 18*2
METALL_HEIGHT = 30 #18:15 15*2





#Images
#Function to scale images when loaded
def load_image(image_name,scale=None): #not all images will need scaling
    image = pygame.image.load(os.path.join('assets/images',image_name)) #image_name = param in load_image and is file path
    if scale is not None:
        image = pygame.transform.scale(image, scale) #reference image variable above and scale param
    return image

background_image = load_image('background.png')
player_image_right = load_image('megaman-right.png',(PLAYER_WIDTH,PLAYER_HEIGHT))
player_image_left = load_image('megaman-left.png',(PLAYER_WIDTH,PLAYER_HEIGHT))
player_image_jump_right = load_image('megaman-right-jump.png',(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
player_image_jump_left = load_image('megaman-left-jump.png',(PLAYER_JUMP_WIDTH,PLAYER_JUMP_HEIGHT))
floor_tile_image = load_image('floor-tile.png',(TILE_SIZE, TILE_SIZE))
metall_image_left = load_image('metall-left.png',(METALL_WIDTH,METALL_HEIGHT))
health_image = load_image('health.png', (HEALTH_WIDTH,HEALTH_HEIGHT))
player_image_shoot_right = load_image('megaman-right-shoot.png',(PLAYER_SHOOT_WIDTH,PLAYER_HEIGHT))
player_image_shoot_left = load_image('megaman-left-shoot.png', (PLAYER_SHOOT_WIDTH,PLAYER_HEIGHT))
player_image_jump_shoot_right = load_image('megaman-right-jump-shoot.png',(PLAYER_JUMP_SHOOT_WIDTH, PLAYER_JUMP_HEIGHT))
player_image_jump_shoot_left = load_image('megaman-left-jump-shoot.png',(PLAYER_JUMP_SHOOT_WIDTH, PLAYER_JUMP_HEIGHT))
player_image_bullet = load_image('bullet.png',(PLAYER_BULLET_WIDTH,PLAYER_BULLET_HEIGHT))


pygame.init()
window = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Fuzzy's Window Title") 
pygame.display.set_icon(player_image_right)
clock = pygame.time.Clock()

#Custom event
INVINCIBLE_END = pygame.USEREVENT + 0 #to set invinsible back to True
SHOOTING_END = pygame.USEREVENT + 1 #to set invinsible back to False

'''---------------------------------------Player Class------------------------------------------------------------'''
class Player(pygame.Rect): #class Player(inherit pygame.Rect)

    class Bullet(pygame.Rect):
        def __init__(self):
            if player.direction == 'left':
                pygame.Rect.__init__(self, player.x, player.y + TILE_SIZE/2, PLAYER_BULLET_WIDTH, PLAYER_BULLET_HEIGHT)
                self.velocity_x = - PLAYER_BULLET_VELOCITY_x
            elif player.direction == 'right':
                pygame.Rect.__init__(self, player.x + player.width, player.y + TILE_SIZE/2, PLAYER_BULLET_WIDTH, PLAYER_BULLET_HEIGHT)
                self.velocity_x = PLAYER_BULLET_VELOCITY_x
            self.image = player_image_bullet
            self.used = False #if bullet hits enemy bullet is used

    def __init__(self): #will describe latter
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_image_right
        self.velocity_x = 0 #add velocity_x and set to 0
        self.velocity_y = 0 #add velocity_y and set to 0
        self.direction = "right" #set default direction to "right"
        self.jumping = False #keep from constant jumping
        self.invincible = False #for when collision with ads
        self.max_health = 28 #health
        self.health = self.max_health
        self.shooting = False
        self.bullets = []
    
    def update_image(self):

        if self.jumping and self.shooting:
            if self.direction == "right": #if the .direction above is changed to 'right and jumping'
                self.image = player_image_jump_shoot_right
            elif self.direction == "left": #if the .direction above is changed to 'left and jumping'
                self.image = player_image_jump_shoot_left
        elif self.shooting:
            if self.direction == "right": #if the .direction above is changed to 'right and jumping'
                self.image = player_image_shoot_right
            elif self.direction == "left": #if the .direction above is changed to 'left and jumping'
                self.image = player_image_shoot_left
        elif self.jumping:
            if self.direction == "right": #if the .direction above is changed to 'right and jumping'
                self.image = player_image_jump_right
            elif self.direction == "left": #if the .direction above is changed to 'left and jumping'
                self.image = player_image_jump_left
        else:
            if self.direction == "right": #if the .direction above is changed to 'right'
                self.image = player_image_right
            elif self.direction == "left": #if the .direction above is changed to 'left'
                self.image = player_image_left

    def set_invincible(self, milliseconds=1000): #self, miliseconds(optional)
        self.invincible = True
        pygame.time.set_timer(INVINCIBLE_END, milliseconds, 1)

    def set_shooting(self):
        if not self.shooting:
            self.shooting = True #Listen for key press and change image to shooting
            self.bullets.append(Player.Bullet())
            pygame.time.set_timer(SHOOTING_END, 250, 1) #250 miliseconds 1 time


#Metall class
class Metall(pygame.Rect):
    def __init__(self, x, y):
        pygame.Rect.__init__(self, x, y, METALL_WIDTH, METALL_HEIGHT)
        self.image = metall_image_left
        self.velocity_y = 0
        self.direction = "left"
        self.jumping = False
        self.health = 1
        

#Tile Class
class Tile(pygame.Rect):
    def __init__(self, x, y, image): #create rectangle and save image
        pygame.Rect.__init__(self, x, y, TILE_SIZE, TILE_SIZE)
        self.image = image


'''---------------------------------------Create Map Function------------------------------------------------------------'''
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

    for i in range(3):
        metall = Metall(player.x + TILE_SIZE*(3+i*1.5), TILE_SIZE*6) #3 tiles to the right of the player
        metalls.append(metall)

#Check_Tile_Collision function
def check_tile_collision(character): #if player hits a tile, return the tile otherwise do nothing
    for tile in tiles:
        if character.colliderect(tile):
            return tile
    return None

#Check_Tile_Collision on x-axis
def check_tile_collision_x(character): #check for collision on x-axis
    tile = check_tile_collision(character)
    if tile is not None:
        if character.velocity_x < 0: #going left
            character.x = tile.x + tile.width #right side of tile
        elif character.velocity_x > 0: #going right
            character.x = tile.x - character.width #left side of tile
        character.velocity_x = 0 #stop player from moving after collision

#Check_Tile_Collision on y-axis
def check_tile_collision_y(character): #check for collision on y-axis
    tile = check_tile_collision(character)
    if tile is not None:
        if character.velocity_y < 0: #going up
            character.y = tile.y + tile.height
        elif character.velocity_y > 0: #going down
            character.y = tile.y - character.height #top of tile
            character.jumping = False
        character.velocity_y = 0 #stop player from moving after collision

'''---------------------------------------Move Function------------------------------------------------------------'''
def move(): #movement
    global metalls
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

    check_tile_collision_x(player) #check for collision on x-axis 1st
    
    #player y movement
    player.velocity_y += GRAVITY #assign gravity to player velocity
    player.y += player.velocity_y #.velocity_y is called in class Player | .y is the top of the image, .height is the bottom of the image
    check_tile_collision_y(player) #check for collision on y-axis 2nd

    #bullets
    for bullet in player.bullets:
        bullet.x += bullet.velocity_x
        for metall in metalls:
            if metall.health > 0 and not bullet.used and bullet.colliderect(metall):
                metall.health -= 1
                bullet.used = True
    player.bullets = [bullet for bullet in player.bullets if not bullet.used \
                      and bullet.x + bullet.width > 0 and bullet.x < GAME_WIDTH]#creates new list and copies over existing list to check
    metalls = [metall for metall in metalls if metall.health > 0]
    

    #enemy y movement
    for metall in metalls: #for each metall apply gravity
        metall.velocity_y += GRAVITY
        metall.y += metall.velocity_y
        check_tile_collision_y(metall)

        if not player.invincible and player.colliderect(metall): #subtract health
            print("Collision with Metall")
            player.health -= 1
            player.set_invincible()

'''---------------------------------------Draw Function------------------------------------------------------------'''
def draw():
    window.fill((20, 18, 167))
    window.blit(background_image, (0, 80))

    for tile in tiles:
        window.blit(tile.image, tile)

    player.update_image() #reference Player class -> update_image function. Put BEFORE drawing the player image default
    window.blit(player.image, player)
    for metall in metalls:
        window.blit(metall.image, metall)

    for bullet in player.bullets:
        window.blit(bullet.image, bullet)

    pygame.draw.rect(window, 'black', (TILE_SIZE,TILE_SIZE, HEALTH_WIDTH, HEALTH_HEIGHT*player.max_health)) #Health bar
    for i in range(player.max_health - player.health, player.max_health):
        window.blit(health_image,(TILE_SIZE,TILE_SIZE+i*HEALTH_HEIGHT, HEALTH_WIDTH, HEALTH_HEIGHT))

#start game
player = Player()
metalls = [] #list to store Metalls
tiles = [] #list to store variables
create_map()
'''---------------------------------------Game Loop------------------------------------------------------------'''
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #1st event
            pygame.quit() 
            exit()
        elif event.type == INVINCIBLE_END: #3rd event
            player.invincible = False
        elif event.type == SHOOTING_END:
            player.shooting = False

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
    #Shooting
    if keys[pygame.K_f] or (keys[pygame.K_f] and keys[pygame.K_SPACE]):
        player.set_shooting() #reference set_shooting and set to true

    move()
    draw()
    pygame.display.update()  
    clock.tick(60) 