#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#            Functions for snake.py            #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

import pygame
import time
from constants import *
import random

pygame.init()

# OBJECTS

# Create window
gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))

# Font object
font = pygame.font.SysFont(None, 25)

# Create clock
clock = pygame.time.Clock()

# FUNCTION DEFINITIONS

# Eat apple, generate new one and make snake grow
def eatApple(x,y,rand_x,rand_y, length):
    if x == rand_x and y == rand_y:
        rand_x = round(random.randrange(BORDER, FIELD_WIDTH - BLOCK_SIZE)/10.0)*10.0
        rand_y = round(random.randrange(BORDER, FIELD_HEIGHT - BLOCK_SIZE)/10.0)*10.0
        length = length + 1
    result = (rand_x, rand_y, length)
    return result

# Create snake body
def snakeBody(BLOCK_SIZE,snakeList):
    gameDisplay.blit(headimg,(snakeList[-1][0], snakeList[-1][1]))
    for xy in snakeList[:-1]:
        gameDisplay.blit(body, (xy[0], xy[1]))

# Show message on screen
def screenMessage(msg,colour, x,y):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [x, y])

# Obtain image size
def imageSize(image):
    image_width, image_height = (image.get_rect().size)
    return image_width, image_height

# Find where to place image horizontally
def centerImage(image):
    w, h = imageSize(image)
    x_pos = DISPLAY_WIDTH/2 - w/2
    return x_pos

# Main game loop
def gameLoop():
    # EXIT MAIN lOOP
    GAME_EXIT = False
    GAME_OVER = False

    # HEAD OF THE SNAKE
    lead_x = DISPLAY_WIDTH/2
    lead_y = DISPLAY_HEIGHT/2

    # List of snake segments
    snakeList = []
    snakeLength = 1

    # MOTION
    lead_x_change = 0
    lead_y_change = 0

    # Apple location = random
    randAppleX = round(random.randrange(BORDER, FIELD_WIDTH - BLOCK_SIZE)/10.0)*10.0
    randAppleY = round(random.randrange(BORDER, FIELD_HEIGHT - BLOCK_SIZE)/10.0)*10.0


    # Main loop
    while not GAME_EXIT:
        while GAME_OVER == True:
            gameDisplay.fill(white)
            game_over_text = gameDisplay.blit(gameoverimg,(centerImage(gameoverimg),100))
            screenMessage("Press C to play again or Q to quit.", black, 70,200)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        GAME_EXIT = True
                        GAME_OVER = False
                    if event.key == pygame.K_c:
                        gameLoop()
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
        if lead_x > FIELD_WIDTH or lead_x < BORDER or lead_y > FIELD_HEIGHT or lead_y < BORDER:
            GAME_OVER = True

        # Update head position
        lead_x += lead_x_change
        lead_y += lead_y_change

        # Draw background
        gameDisplay.fill(white)
        # Draw boundaries
        top_bound = gameDisplay.blit(horizontal,(0,0))
        bottom_bound = gameDisplay.blit(horizontal,(0,DISPLAY_HEIGHT-BORDER))
        left_bound = gameDisplay.blit(vertical, (0,0))
        right_bound = gameDisplay.blit(vertical, (DISPLAY_WIDTH-BORDER, 0))
        # Draw apple
        gameDisplay.blit(apple, (randAppleX,randAppleY))

        # List of coordinates of snake
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
        # Collision
        if snakeHead in snakeList[:-1]:
            GAME_OVER = True

        # Draw snake
        snakeBody(BLOCK_SIZE, snakeList)
        pygame.display.update()

        # Eat apple
        randAppleX, randAppleY, snakeLength = eatApple(lead_x,lead_y,randAppleX,randAppleY, snakeLength)

        # Score
        score = snakeLength

        clock.tick(FPS)
