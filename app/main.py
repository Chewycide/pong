import pygame
import sys


from pygame.locals import *
from abstracts.constants import (
    DEFAULT_FPS,
    SCREEN_SIZE,
    WINDOW_TITLE,
    PLAYER_XPOS,
    PLAYER_YPOS,
    CPU_XPOS,
    CPU_YPOS
)
from objects.paddle import (
    PlayerPongPaddle,
    ComPongPaddle
)


clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
screen = pygame.display.set_mode(SCREEN_SIZE)
white_background = pygame.Color(255,255,255,0)


# Objects
player = PlayerPongPaddle(PLAYER_XPOS, PLAYER_YPOS)
cpu = ComPongPaddle(CPU_XPOS, CPU_YPOS)

# Main game loop
while True:

    screen.fill(white_background)

    # Event handling
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
                

    # Update objects
    player.draw(screen)
    player.movement()
    cpu.draw(screen)


    pygame.display.update()
    clock.tick(DEFAULT_FPS) # Maintain 60 frames per second