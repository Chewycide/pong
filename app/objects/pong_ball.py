import pygame
import random

from abstracts.direction_handler import DirectionHandler
from abstracts.constants import (
    BALL_SPEED,
    INITIAL_DIRECTIONS
)


class PongBall(object):
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.center = (self.x, self.y)

        self.radius = 8
        self.color = pygame.Color(0, 0, 0)

        self.direction = random.choice(INITIAL_DIRECTIONS)
        self.direction_handler = DirectionHandler(BALL_SPEED)

        
    

    def move_forward(self):
        sx = self.direction_handler.get_xcomp(self.direction)
        sy = self.direction_handler.get_ycomp(self.direction)
        self.x += sx
        self.y += sy
        self.center = (self.x, self.y)

    
    def wall_bounce(self):
        self.direction += -180
        self.move_forward()


    def paddle_bounce(self):
        self.direction -= 180.0
        self.move_forward()


    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.center, self.radius)


    def get_left_point(self):
        return self.x - self.radius


    def get_right_point(self):
        return self.x + self.radius


    def get_upper_point(self):
        return self.y - self.radius


    def get_lower_point(self):
        return self.y + self.radius