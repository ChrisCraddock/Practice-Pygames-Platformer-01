# video 01
# pip install pygame-ce
import pygame
from sys import exit #import 'exit' from sys module

#Game Variabels
GAME_WIDTH = 512
GAME_HEIGHT = 512


#Create Window
pygame.init() #always needed to initialize pygame
#set_mode() is creating the window
window = pygame.display.set_mode((GAME_HEIGHT,GAME_WIDTH)) #pass tuple. window size in pixels 
pygame.display.set_caption("Fuzzy's Window Title") #Title of the window
clock = pygame.time.Clock() #set refresh/frame rate


while True: #keep window open while pygame is running 
    #pass #just needed to verify game window opens 
    for event in pygame.event.get(): #listens for keyboard/mouse activity 
        if event.type == pygame.QUIT: #if you press the 'x' 
            pygame.quit() #then stop this loop 
            exit() #close window (imported from sys) 



    pygame.display.update() #updates the display by drawing on teh screen. part of while-loop 
    clock.tick(60) #reference 'clock' variable. 60 fps 