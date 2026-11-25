
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

#images '\\' for Linux '/' for Windows
#load images. folder/name.image
#background_image = pygame.image.load("assets/images/background.png")
background_image = pygame.image.load(os.path.join('assets/images','background.png'))
player_image_right = pygame.image.load(os.path.join('assets/images','megaman-right.png'))
player_image_right = pygame.transform.scale(player_image_right,(PLAYER_WIDTH,PLAYER_HEIGHT))#scale image down

pygame.init()
window = pygame.display.set_mode((GAME_HEIGHT,GAME_WIDTH))
pygame.display.set_caption("Fuzzy's Window Title") 
pygame.display.set_icon(player_image_right) #icon next to title
clock = pygame.time.Clock() 


class Player(pygame.Rect): #class Player(inherit pygame.Rect)
    def __init__(self): #will describe latter
        pygame.Rect.__init__(self, PLAYER_X, PLAYER_Y, PLAYER_WIDTH, PLAYER_HEIGHT)
        self.image = player_image_right

#player = pygame.Rect(150,150,50,50) #Reference class Player instead
player = Player()

#Order matters, top to bottom drawing order, top in the background bottom in the foreground
def draw():
    window.fill((20,18,167))
    window.blit(background_image, (0,80)) #image and x/y position to start from. Dimensions can be found by hovering over the image
    #pygame.draw.rect(window,(2,239,238), player) #now that player has an image, remove
    window.blit(player.image, player)


while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #1st event
            pygame.quit() 
            exit()

    #Hold keys instead of constant pressing
    keys = pygame.key.get_pressed()  #2nd event
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player.y -=5 #y-axis
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player.y +=5 #y-axis
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player.x -=5 #x-axis
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player.x +=5 #x-axis


    draw()
    pygame.display.update()  
    clock.tick(60) 