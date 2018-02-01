#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#            Functions for snake.py            #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import pygame
import time
from constants import *

pygame.init()

# OBJECTS

# Create window
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

# Font object
font = pygame.font.SysFont(None, 25)

# FUNCTION DEFINITIONS

# Show message on screen
def screenMessage(msg,colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2])
