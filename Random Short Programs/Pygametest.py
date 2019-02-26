#testing out pygame

import pygame

def main():
    #initialize the pygame module
    pygame.init()
    #create a surface on the screen that has a size of 240x180
    screen = pygame.display.set_mode((640,480))
    #define a variable to control the main loop
    running = True

    #main loop
    while running:
        #event handling, gets all the events from the event queue
        for event in pygame.event.get():
            #only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                #change the value to False to exit the main loop
                running = False
        
main()