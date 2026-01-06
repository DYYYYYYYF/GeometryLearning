import pygame
from visualization import *
from .interface.algorithm_base import algorithm_base
from geometry.primitives import Point, Segment
from ui import *
from typing import Optional, cast

class algorithm_convex_generate(algorithm_base):
    def __init__(self):
        super().__init__()

    def convex_generate(self):
        if len(self.points) <= 1:
            return self.points
        self.points = sorted(self.points, key=lambda p: (p.x, p.y))

        def cross(o, a, b):
            return (a.x - o.x)*(b.y - o.y) - (a.y - o.y)*(b.x - o.x)

        lower = []
        for p in self.points:
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
                lower.pop()
            lower.append(p)

        upper = []
        for p in reversed(self.points):
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
                upper.pop()
            upper.append(p)

        return lower[:-1] + upper[:-1]

    def generate_edges(self):
        segments = []
        if (len(self.points) < 2):
            return segments
        
        for p1, p2 in zip(self.points, self.points[1:]):
            segments.append(Segment(p1, p2))
        
        segments.append(Segment(self.points[0], self.points[-1]))
        return segments
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x < self.panel_location[0]:
                self.add_point(Point(x, y))

    def algorithm_impl(self):
        self.points = self.convex_generate()
        self.lines = self.generate_edges()


    def draw(self):
        super().draw()

        self.algorithm_impl()
        get_renderer().draw_scene(self.lines, self.points)

    _btn : Optional[Button] = None
    def init_ui(self):
        super().init_ui()

        cast(Text, self.label).set_text('convex generate')
        cast(Button, self.reset_btn).set_callback(lambda: self.points.clear())

