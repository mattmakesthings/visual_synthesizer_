from abc import ABC, abstractmethod


class Scene:

    @abstractmethod
    def update_step(self):
        pass


class CircleScene(Scene):
    def __init__(self):
        pass

    def update_step(self):
        pass
