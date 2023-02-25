import pygame

from abstracts.constants import (
    PADDLE_WIDTH,
    PADDLE_HEIGHT,
    UPPER_BOUND,
    LOWER_BOUND
)


class PongPaddle(object):
    """Base class for pong paddles"""
    def __init__(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        self.width = PADDLE_WIDTH
        self.height = PADDLE_HEIGHT
        self.color = pygame.Color(0, 0, 0)
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def draw(self, surface):
        """draw object"""
        pygame.draw.rect(surface, self.color, self.rect)

    def check_upper_bound(self):
        """Checks if the paddle is not above the upper boundaries"""
        if self.rect.top > UPPER_BOUND:
            return True
        return False

    def check_lower_bound(self):
        """Checks if the paddle is not below the lower boundaries"""
        if self.rect.bottom < LOWER_BOUND:
            return True
        return False
    

class ComPongPaddle(PongPaddle):
    """CPU subclass"""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

    def movement(self, ball_ypos, in_upperbound, in_lowerbound):
            if self.rect.centery > ball_ypos and in_upperbound:
                self.rect.move_ip(0, -2)

            if self.rect.centery < ball_ypos and in_lowerbound:
                self.rect.move_ip(0, 2)


class PlayerPongPaddle(PongPaddle):
    """Player subclass"""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
    
    def movement(self, in_upperbound, in_lowerbound):
        key = pygame.key.get_pressed()
        distance = 6
        if key[pygame.K_w] and in_upperbound:
            self.rect.move_ip(0, -distance)

        if key[pygame.K_s] and in_lowerbound:
            self.rect.move_ip(0, distance)