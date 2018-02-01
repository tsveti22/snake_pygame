#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#               A pygame version of The Snake                  #
#                Following the tutorials by:                   #
#   https://www.youtube.com/channel/UCJbPGzawDH1njbqV-D5HqKw   #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import pygame
import time
from functions import *
from constants import *

# Initialise pygame
pygame.init()

# Create title
pygame.display.set_caption("The Snake")

# Update (flip) display
pygame.display.update()

clock = pygame.time.Clock()

# Main loop
while not GAME_EXIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_EXIT = True
        if event.type == pygame.KEYDOWN:
            # Handle arrow keys
            if event.key == pygame.K_LEFT:
                lead_x_change = -BLOCK_SIZE
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = BLOCK_SIZE
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -BLOCK_SIZE
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = BLOCK_SIZE
                lead_x_change = 0

    # Set boundaries
    if lead_x > DISPLAY_WIDTH or lead_x < 0 or lead_y > DISPLAY_HEIGHT or lead_y < 0:
        GAME_EXIT = True

    # Update head position
    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y, BLOCK_SIZE,BLOCK_SIZE])
    pygame.display.update()

    clock.tick(FPS)

# Print message to screen
screenMessage("You died.", red)
pygame.display.update()
time.sleep(2)

# Uninitialise and quit pygame
pygame.quit()
quit()
