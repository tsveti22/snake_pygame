#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#         Constants for snake.py         #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import pygame
import time

pygame.init()

# COLORS
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

# SIZE CONSTANTS
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
BLOCK_SIZE = 10

# FRAMES PER SECOND
FPS = 10

# Images
body = pygame.image.load('body.png')
apple = pygame.image.load('apple.png')
