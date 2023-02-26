import pygame
import random

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

        self.initial_angles = [
            random.randint(0, 45),
            random.randint(135, 225),
            random.randint(315, 360)

        ]
        self.direction = random.choice(self.initial_angles)
        self.velocity = BALL_VELOCITY


    def update_coord(self, vx, vy):
        self.x += vx
        self.y += vy
        self.center = (self.x, self.y)


    def paddle_bounce(self, pad_cpy, pad_h, s_pos):
        max_angle = 45

        pady_bally_dist = abs(self.y - pad_cpy) # distance of pad center and ball center
        half_pad_h = pad_h / 2 # half the height of the pad
        angle_multiplier = pady_bally_dist / half_pad_h

        # new angle will depend on the distance of the ball to the center. range is 0 to 45 degrees
        
        new_angle = round(angle_multiplier * max_angle, 4)
        if self.y < pad_cpy:
            new_angle = -new_angle + 360

        if s_pos == 'r':
            new_angle = (angle_multiplier * max_angle) + (angle_multiplier * max_angle + 180)
        
            if self.y > pad_cpy:
                new_angle = -new_angle +360

        self.direction = new_angle



    def wall_bounce(self):
        self.direction = -self.direction
        self.direction += 360
    

    def ball_reset(self, surface, x_pos, y_pos):
        self.__init__(x_pos, y_pos)
        self.draw(surface)


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