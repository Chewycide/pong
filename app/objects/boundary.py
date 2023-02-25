import pygame

class BoundaryLine(object):
    """Draws the game's boundary line"""
    def __init__(self, ub, lb, width):
        """
            params:
            ub = Upper boundary y coordinate
            lb = Lower boundary y coordinate
            width = Game screen width
        """
        self.ub_start = (0, ub)
        self.ub_end = (width, ub)
        self.lb_start = (0, lb)
        self.lb_end = (width,lb)
        self.ml_start = (width/2, ub)
        self.ml_end = (width/2, lb)
        
        self.color = pygame.Color(0, 0, 0)

    def draw(self, surface):
        pygame.draw.line(surface, self.color, self.ub_start, self.ub_end)
        pygame.draw.line(surface, self.color, self.lb_start, self.lb_end)
        pygame.draw.line(surface, self.color, self.ml_start, self.ml_end)
