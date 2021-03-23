import pygame
import random

from .shapes import Circle, VariableShrinker

clock = pygame.time.Clock()
shrinker = VariableShrinker(
    start=10,
    end=1,
    step=-1,
)


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
                size=random.randint(200, 1000)
            )
            circle_list.append(
                shrinker.shrinker_shape(new_circle)
            )

        screen.screen.fill(fading_colors.fade())
        for place, circle in enumerate(circle_list):
            if circle.size < 1:
                circle_list.pop(place)
            else:
                circle.draw(screen=screen.screen)
            circle.shrink()

        pygame.display.flip()
        clock.tick(30)
