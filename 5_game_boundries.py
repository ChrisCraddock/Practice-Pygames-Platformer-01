
import pygame
from sys import exit
import os

#game variables
GAME_WIDTH = 512
GAME_HEIGHT = 512

PLAYER_X = GAME_WIDTH/2
PLAYER_Y = GAME_HEIGHT/2
PLAYER_WIDTH = 42 #7:8 ratio 210 7x30 7*6
PLAYER_HEIGHT = 48 #7:8 ratio 240 8x30 8*6
'''replaces hardcoding speed in keypress'''
PLAYER_DISTANCE = 5

#Images
#load images. folder/name, image
background_image = pygame.image.load(os.path.join('assets/images','background.png'))
player_image_right = pygame.image.load(os.path.join('assets/images','megaman-right.png'))
player_image_right = pygame.transform.scale(player_image_right,(PLAYER_WIDTH,PLAYER_HEIGHT))


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


player = Player()

#Draw Function
def draw():
    window.fill((20,18,167))
    window.blit(background_image, (0,80))
    window.blit(player.image, player)


while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #1st event
            pygame.quit() 
            exit()

    #Hold keys instead of constant pressing
    keys = pygame.key.get_pressed()  #2nd event
    '''Add game boundries. Max up position is player y value-movement speed or 0'''
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y = max(player.y-PLAYER_DISTANCE,0)


    '''Add game boundries. Max down position is player y value + movement speed, game height - player height'''
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y = min(player.y+PLAYER_DISTANCE,GAME_HEIGHT-player.height)

    '''Add game boundries. Max up position is player x value-movement speed or 0'''
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x = max(player.x-PLAYER_DISTANCE,0)
    '''Add game boundries. Max down position is player x value + movement speed, game width - player width'''
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x = min(player.x+PLAYER_DISTANCE,GAME_WIDTH-player.width)


    draw()
    pygame.display.update()  
    clock.tick(60) 