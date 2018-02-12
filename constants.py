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
DISPLAY_WIDTH = 400
DISPLAY_HEIGHT = 300
BLOCK_SIZE = 10
BORDER = 10
FIELD_WIDTH = DISPLAY_WIDTH - 2*BORDER
FIELD_HEIGHT = DISPLAY_HEIGHT - 2*BORDER

# FRAMES PER SECOND
FPS = 10

# Images
headimg = pygame.image.load('head.png')
body = pygame.image.load('body.png')
apple = pygame.image.load('apple.png')
horizontal = pygame.image.load('horizontal.png')
vertical = pygame.image.load("vertical.png")
gameoverimg = pygame.image.load("game_over.png")
