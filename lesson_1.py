# import pygame pack
import pygame
# initialise pygame
pygame.init()
# displaying a window of height 500 and width 400
pygame.display.set_mode((400,500))

#creating a bool which checks if game is running
running = True
# keep game running till running is true
while running:

    # Check for event user pushedany event in quit
    for event in pygame.event.get():
        # if event is of type then
        # set running bool false
        if event.type==pygame.QUIT:
            running = False


