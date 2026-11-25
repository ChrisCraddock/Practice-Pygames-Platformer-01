
import pygame
from sys import exit

#game variables
GAME_WIDTH = 512
GAME_HEIGHT = 512



pygame.init()

window = pygame.display.set_mode((GAME_HEIGHT,GAME_WIDTH))
pygame.display.set_caption("Fuzzy's Window Title") 
clock = pygame.time.Clock() 

#right(x), top(y), width, height
player = pygame.Rect(150,150,50,50)#rectangle 150px to the right of origin, 150 down, 50 height/width

#new functuion called draw
def draw():
    #window.fill("blue") #change background color of window. Different colors avail
    #window.fill("#54de9e") #use Hex value for any color you want
    #window.fill((84,222,158)) #use RGB value inside a tuple for any color you want
    window.fill((20,18,167)) #specific blue for this tutorial
    pygame.draw.rect(window,(2,239,238), player) #draw object. Needs window,color,object


while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: #1st event
            pygame.quit() 
            exit() 


    draw() #calls draw function
    pygame.display.update()  
    clock.tick(60) 