#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         Constants for snake.py         #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import pygame
import time

pygame.init()

# EXIT MAIN lOOP
GAME_EXIT = False

# COLORS
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# SIZE CONSTANTS
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BLOCK_SIZE = 10

# FRAMES PER SECOND
FPS = 30

# HEAD OF THE SNAKE
lead_x = DISPLAY_WIDTH/2
lead_y = DISPLAY_HEIGHT/2

# MOTION
lead_x_change = 0
lead_y_change = 0
