
import pygame
from sys import exit


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