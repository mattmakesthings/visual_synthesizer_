import pygame

class Movement:
    def __init__(self, x_step, y_step):
        self.x_step = x_step
        self.y_step = y_step

    def step(self):
        return self.x_step, self.y_step


class Circle(object):
    def __init__(
            self,
            x,
            y,
            color,
            size=700,
            shrink_step=3,
            movement=None,
            fade_step=0
    ):
        self.x = x
        self.y = y
        self.color = color
        self.size = size
        self.shrink_step = shrink_step
        self.movement = movement if movement else Movement(0, 0)
        self.fade_step = fade_step

    def shrink(self, amount=None):
        self.size -= amount if amount else self.shrink_step
        # self.color=

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.color,
            (self.x, self.y),
            self.size
        )

    def move(self, movement=None):
        if movement:
            x_move, y_move = movement.step()
        else:
            x_move, y_move = self.movement.step()

        self.x += x_move
        self.y += y_move

    def fade(self, fade_step=None):
        if not fade_step:
            fade_step = self.fade_step

        if self.color.a - fade_step < 0:
            self.color.a = 0
            return

        self.color.a -= fade_step
