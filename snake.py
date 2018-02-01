import pygame

# Initialise pygame
pygame.init()

# Colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)

# Create window and title
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("The Snake")

# Update (flip) display
pygame.display.update()

GAME_EXIT = False
# Head of the snake
lead_x = 300
lead_y = 300
lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

# Main loop
while not GAME_EXIT:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_EXIT = True
        if event.type == pygame.KEYDOWN:
            # Handle arrow keys
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0
    if lead_x > 800 or lead_x < 0 or lead_y > 600 or lead_y < 0:
        GAME_EXIT = True

    # Update head position
    lead_x += lead_x_change
    lead_y += lead_y_change

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y, 10,10])
    pygame.display.update()

    clock.tick(15)

# Uninitialise and quit pyga
pygame.quit()
quit()
