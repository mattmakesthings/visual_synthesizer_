import random
import itertools
import pygame


class ColorShifter:
    def __init__(self):
        self.step = 1
        self.col_stepper = [1, 1, 1]

    def shift(self, color):
        new_color = list(color)
        index = random.randint(0, 2)

        if new_color[index] > 254:
            self.col_stepper[index] = -1
        elif new_color[index] < 1:
            self.col_stepper[index] = 1

        new_color[index] += self.col_stepper[index]
        print(new_color)
        return tuple(new_color)


class FadingColors:
    colors = itertools.cycle(['green', 'blue', 'purple', 'pink', 'red', 'orange'])

    base_color = next(colors)
    next_color = next(colors)
    current_color = base_color

    def __init__(self, number_of_steps, colors):
        self.step = 1
        self.number_of_steps = number_of_steps
        self.colors = itertools.cycle(colors)
        self.current_color

    def fade(self):
        self.step += 1
        if self.step < self.number_of_steps:
            # (y-x)/number_of_steps calculates the amount of change per step required to
            # fade one channel of the old color to the new color
            # We multiply it with the current step counter
            self.current_color = [
                x + (((y - x) / self.number_of_steps) * self.step) for x, y in
                zip(pygame.color.Color(self.base_color), pygame.color.Color(self.next_color))
            ]
        else:
            self.step = 1
            self.base_color = self.next_color
            self.next_color = next(self.colors)
            self.current_color = pygame.color.Color(self.base_color)

        return tuple(self.current_color)