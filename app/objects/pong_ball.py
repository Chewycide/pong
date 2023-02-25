import pygame
import random

from abstracts.direction_handler import DirectionHandler
from abstracts.constants import (
    BALL_VELOCITY,
    BALL_RADIUS
)


class PongBall(object):
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.center = (self.x, self.y)

        self.radius = BALL_RADIUS
        self.color = pygame.Color(0, 0, 0)

        self.direction = random.randint(1, 360)
        self.velocity = BALL_VELOCITY


    def update_coord(self, vx, vy):
        self.x += vx
        self.y += vy
        self.center = (self.x, self.y)


    def paddle_bounce(self):
        new_direction = 180 - (self.direction * 2)
        self.direction += new_direction

    
    def wall_bounce(self):
        new_direction = (180 - self.direction) * 2
        self.direction += new_direction
    

    def ball_reset(self, surface, x_pos, y_pos):
        self.__init__(x_pos, y_pos)
        self.draw(surface, self.color, self.center, self.radius)


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