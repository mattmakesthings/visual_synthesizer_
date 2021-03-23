import pygame


class Circle(object):
    def __init__(self, x, y, color, size=700, shrink_step=3):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.shrink_step = shrink_step

    def shrink(self, amount=None):
        self.size -= amount if amount else self.shrink_step

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.size
        )


class VariableShrinker:
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        self.current_shrink_step = start

    def shrinker_shape(self, shape):

        if self.current_shrink_step > abs(self.end):
            self.current_shrink_step = abs(self.start)
        if self.current_shrink_step < abs(self.start):
            self.current_shrink_step = abs(self.end)

        self.current_shrink_step += self.step

        shape.shrink_step = self.current_shrink_step
        # shape.shrink_step = shape.size // 100 + shape.shrink_step
        return shape
