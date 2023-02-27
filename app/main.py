import pygame
import sys

from abstracts.constants import (
    SCREEN_WIDTH,
    UPPER_BOUND,
    LOWER_BOUND,
    DEFAULT_FPS,
    SCREEN_SIZE,
    WINDOW_TITLE,
    PLAYER_XPOS,
    PLAYER_YPOS,
    CPU_XPOS,
    CPU_YPOS,
    BALL_INITIALX,
    BALL_INITIALY
)
from objects.paddle import (
    PlayerPongPaddle,
    ComPongPaddle
)
from objects.pong_ball import PongBall
from objects.boundary import BoundaryLine
from abstracts.direction_handler import DirectionHandler
from pygame.locals import *


clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption(WINDOW_TITLE)
screen = pygame.display.set_mode(SCREEN_SIZE)
white_background = pygame.Color(255,255,255,0)


# Objects
player = PlayerPongPaddle(PLAYER_XPOS, PLAYER_YPOS)
cpu = ComPongPaddle(CPU_XPOS, CPU_YPOS)
ball = PongBall(BALL_INITIALX, BALL_INITIALY)
dh = DirectionHandler(ball.velocity)
bl = BoundaryLine(UPPER_BOUND, LOWER_BOUND, SCREEN_WIDTH)


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
    player.movement(player.check_upper_bound(), player.check_lower_bound())
    cpu.draw(screen)
    cpu.movement(ball.y, cpu.check_upper_bound(), cpu.check_lower_bound())
    ball_vx = dh.get_xcomp(ball.direction)
    ball_vy = dh.get_ycomp(ball.direction)
    # print(f"({ball_vx} , {ball_vy}) , angle: {ball.direction}")
    ball.update_coord(ball_vx, ball_vy)
    ball.draw(screen)
    bl.draw(screen)

    # check if the player hits the ball
    if ball.get_left_point() < player.rect.right:

        # check if ball is not above or below the paddle
        if ball.y > player.rect.top and ball.y < player.rect.bottom:
            ball.paddle_bounce(player.rect.centery, player.height, 'l')
        
        elif ball.x < player.rect.left:
            print("CPU SCORES")
            ball.ball_reset(screen, BALL_INITIALX, BALL_INITIALY)

    # check if the cpu hits the ball
    if ball.get_right_point() > cpu.rect.left:

        # check if ball is not above or below the paddle
        if ball.y > cpu.rect.top and ball.y < cpu.rect.bottom:
            ball.paddle_bounce(cpu.rect.centery, cpu.height, 'r')

        elif ball.x > cpu.rect.right:
            print("PLAYER SCORES")
            ball.ball_reset(screen, BALL_INITIALX, BALL_INITIALY)
    
    # check walls
    if ball.get_upper_point() <= UPPER_BOUND or ball.get_lower_point() >= LOWER_BOUND:
        ball.wall_bounce()

    # TODO: REFACTOR MAIN LOOP

    pygame.display.update()
    clock.tick(DEFAULT_FPS) # Maintain 60 frames per second