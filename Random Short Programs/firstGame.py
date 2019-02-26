#first real activity with pygame. Moving a red box around a black screen
import pygame

#initializes pygame
pygame.init()

MAX_WIDTH = int(640)
MAX_HEIGHT = int(480)
#sets the size of the window
win = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))

#sets the caption for the window
pygame.display.set_caption("First Game")

#initial coordinates of the shape
x = 50
y = 50
width = 40
height = 60
#the velocity that the shape moves by
vel = 5


#the main loop flag
run = True
#main loops
while run:
    #the time delay between loops, 16ms is 60fps
    pygame.time.delay(16)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #grabs the key press
    keys = pygame.key.get_pressed()

    #basic movement based on key presses
    if keys[pygame.K_LEFT]:
        #does a bounds check to make sure the shape doesn't go off the screen
        if x >= (0 - vel):
            x -= vel
    if keys[pygame.K_RIGHT]:
        #have to take the size of the shape into account for the right and bottom sides for bounds checking
        if x <= ((MAX_WIDTH - width) + vel):
            x += vel
    if keys[pygame.K_UP]:
        if y >= (0 - vel):
            y -= vel
    if keys[pygame.K_DOWN]:
        if y <= ((MAX_HEIGHT - height) + vel):
            y += vel

    #quits the game if you press 'q'
    if keys[pygame.K_q]:
        run = False

    #refills the window in black otherwise you get a trail of rectangles
    win.fill((0, 0, 0))
    #draws the rectangle
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    #updates the display
    pygame.display.update()
#quits
pygame.quit()