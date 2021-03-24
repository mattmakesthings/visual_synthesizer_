import pygame
import random

from .shapes import Circle, Movement
from .actions import VariableShrinker
from .scenes import CircleScene
from color_utils import FadingColors
from colors_constants import pastel_world_colors, pastel_world_colors_darker


clock = pygame.time.Clock()

large_circle_colors = FadingColors(
                    number_of_steps=200,
                    colors=pastel_world_colors_darker
                )

MAX_CIRCLES = 10


class Screen:
    def __init__(self, width=1920, height=1080, full_screen=False):
        self.width = width
        self.height=height
        if full_screen:
            self.screen = pygame.display.set_mode(
                (self.width, self.height),
                pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF
            )

        else:
            self.screen = pygame.display.set_mode(
                (self.width, self.height)
            )


def draw_pygame(
        circle_colors,
        fading_colors,
        screen,
        q,
):
    circle_list = []
    shrinker = VariableShrinker(
        start=1,
        end=6,
        step=1,
    )
    running = True
    while running:
        key = pygame.key.get_pressed()

        if key[pygame.K_q]:
            running = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not q.empty():
            b = q.get()
            new_circle = Circle(
                x=random.randint(0, screen.width),
                y=random.randint(0, screen.height),
                color=random.choice(circle_colors),
                size=random.randint(100, 300),
                movement=Movement(-1, -1),
                fade_step=100
            )
            circle_list.append(
                shrinker.shrinker_shape(new_circle)
            )
            # new_circle = Circle(
            #     x=random.randint(0, screen.width),
            #     y=random.randint(0, screen.height),
            #     color=random.choice(circle_colors),
            #     shrink_step=4,
            #     size=random.randint(500, 700)
            # )
            # circle_list.append(
            #     new_circle
            # )

        large_circle_colors.fade()
        screen.screen.fill(fading_colors.fade())
        for place, circle in enumerate(circle_list):
            if circle.size < 1:
                circle_list.pop(place)
            else:
                circle.draw(screen=screen.screen)
            circle.shrink()
            circle.move()
            circle.fade()

        pygame.display.flip()
        clock.tick(90)
