import pygame

from abstracts.constants import (
    PADDLE_WIDTH,
    PADDLE_HEIGHT
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

    
class ComPongPaddle(PongPaddle):
    """CPU subclass"""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)

    def movement(self, ball_ypos):
        if self.rect.centery > ball_ypos:
            self.rect.move_ip(0, -6)

        if self.rect.centery < ball_ypos:
            self.rect.move_ip(0, 6)


class PlayerPongPaddle(PongPaddle):
    """Player subclass"""
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
    
    def movement(self):
        key = pygame.key.get_pressed()
        distance = 6
        if key[pygame.K_w]:
            self.rect.move_ip(0, -distance)
        if key[pygame.K_s]:
            self.rect.move_ip(0, distance)