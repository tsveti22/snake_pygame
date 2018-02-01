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

# Create clock
clock = pygame.time.Clock()

# FUNCTION DEFINITIONS

# Show message on screen
def screenMessage(msg,colour):
    screen_text = font.render(msg, True, colour)
    gameDisplay.blit(screen_text, [DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2])

# Main game loop
def gameLoop():
    # EXIT MAIN lOOP
    GAME_EXIT = False
    GAME_OVER = False

    # HEAD OF THE SNAKE
    lead_x = DISPLAY_WIDTH/2
    lead_y = DISPLAY_HEIGHT/2

    # MOTION
    lead_x_change = 0
    lead_y_change = 0

    # Main loop
    while not GAME_EXIT:
        while GAME_OVER == True:
            gameDisplay.fill(white)
            screenMessage("GAME OVER! Press C to play again or Q to quit", red)
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
        if lead_x > DISPLAY_WIDTH or lead_x < 0 or lead_y > DISPLAY_HEIGHT or lead_y < 0:
            GAME_OVER = True

        # Update head position
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, black, [lead_x,lead_y, BLOCK_SIZE,BLOCK_SIZE])
        pygame.display.update()

        clock.tick(FPS)
