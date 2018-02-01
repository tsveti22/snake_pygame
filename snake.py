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

# Main loop
gameLoop()



# Uninitialise and quit pygame
pygame.quit()
quit()
