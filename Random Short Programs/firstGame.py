#first real activity with pygame. Moving a red box around a black screen
import pygame

#initializes pygame
pygame.init()

#sets the size of the window
win = pygame.display.set_mode((640, 480))

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
        x -= vel
    if keys[pygame.K_RIGHT]:
        x+= vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
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