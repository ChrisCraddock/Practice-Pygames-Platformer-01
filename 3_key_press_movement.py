
import pygame
from sys import exit

#game variables
GAME_WIDTH = 512
GAME_HEIGHT = 512



pygame.init()

window = pygame.display.set_mode((GAME_HEIGHT,GAME_WIDTH))
pygame.display.set_caption("Fuzzy's Window Title") 
clock = pygame.time.Clock() 


player = pygame.Rect(150,150,50,50)

def draw():
    window.fill((20,18,167))
    pygame.draw.rect(window,(2,239,238), player)


while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #1st event
            pygame.quit() 
            exit()
        #keydown = key pressed, keyup = key released
        '''
        if event.type == pygame.KEYDOWN: #2.1 event.
            #if event.key == pygame.K_UP or event.key == pygame.K_w: #keyboard_up arrow or keyboard_w key
            if event.key in (pygame.K_UP, pygame.K_w): #same as above but as tuple and shorter
                player.y -= 5 #player variable moves -5 on the y-axis
            if event.key in (pygame.K_DOWN, pygame.K_s): #same as above but moving down
                player.y += 5 #player variable moves +5 on the y-axis
            if event.key in (pygame.K_LEFT, pygame.K_a): #same as above but moving left
                player.x -= 5 #player variable moves -5 on the x-axis
            if event.key in (pygame.K_RIGHT, pygame.K_d): #same as above but moving right
                player.x += 5 #player variable moves +5 on the x-axis
        '''
    #Hold keys instead of constant pressing
    keys = pygame.key.get_pressed() #2.2 event
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