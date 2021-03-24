# Shape Actions
import itertools

class VariableShrinker:
    # Class that will give each
    def __init__(self, start, end, step):
        self.start = start
        self.end = end
        self.step = step
        self.current_shrink_step = start
        self.step_picker = itertools.cycle(range(start, end, step))

    def shrinker_shape(self, shape):
        self.current_shrink_step = next(self.step_picker)
        shape.shrink_step = self.current_shrink_step / 10
        # shape.shrink_step = shape.size // 100 + shape.shrink_step
        return shape
