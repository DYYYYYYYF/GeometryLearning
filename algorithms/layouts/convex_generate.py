import pygame
from ui import *
from geometry import *
from visualization import *
from typing import Optional, cast
from algorithms.interface.algorithm_base import algorithm_base
from algorithms.impls.convex_core import convex_impl

class algorithm_convex_generate(algorithm_base):
    def __init__(self):
        super().__init__()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if x < self.panel_location[0]:
                self.add_point(Point(x, y))

    def algorithm_impl(self):
        self.points, self.lines = convex_impl(self.points)

    def draw(self):
        super().draw()

        self.algorithm_impl()
        get_renderer().draw_scene(self.lines, self.points)

    _btn : Optional[Button] = None
    def init_ui(self):
        super().init_ui()

        cast(Text, self.label).set_text('convex generate')
        cast(Button, self.reset_btn).set_callback(lambda: self.points.clear())

        # 子类新内容
        self.info_text_1 = Text(0, 40,  ' - click for add point.', 18)
        cast(Panel, self.panel).add_child(self.info_text_1)

