from visualization import *
from geometry.primitives import Point, Segment
from typing import Optional, cast
from ui.GUI import Panel

class algorithm_base:
    def __init__(self):
        self.points = []
        self.lines = []
        self.panel : Optional[Panel] = None

        self.panel_size = [0.2, 1.0]    # Penel占比
        self.panel_location = []

        self.init_ui()

    def add_point(self, point: Point):
        self.points.append(point)

    def add_segment(self, segment: Segment):
        self.lines.append(segment)

    # 具体算法实现
    def algorithm_impl(self):
        pass

    # 处理事件
    def handle_events(self, events):
        pass

    # 处理绘制
    def draw(self):
        self.draw_ui()

    def init_ui(self):
        screen_width, screen_height = get_renderer().get_screen().get_size()

        self.panel_size = [screen_width * 0.2, screen_height * 1.0]
        self.panel_location = [screen_width - self.panel_size[0], screen_height - self.panel_size[1]]
        self.panel = Panel(self.panel_location[0], self.panel_location[1], self.panel_size[0], self.panel_size[1])

    # 绘制UI
    def draw_ui(self):
        get_renderer().draw_ui(cast(Panel, [self.panel]))

