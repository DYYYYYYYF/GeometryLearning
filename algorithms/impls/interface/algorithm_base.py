from visualization import *
from geometry.primitives import Point, Segment
from typing import Optional, cast
from ui import * 

class algorithm_base:
    def __init__(self):
        self.points = []
        self.lines = []
        self.panel : Optional[Panel] = None
        self.label : Optional[Text] = None 
        self.reset_btn : Optional[Button] = None

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

    # 处理事件-仅分发
    def handle_events(self, events):
        for event in events:
            self.handle_event(event)

            # 转换_btn为Button类型
            cast(Button, self.reset_btn).handle_event(event)

    # 子类覆写实现不同处理
    def handle_event(self, event):
        pass

    # 处理绘制
    def draw(self):
        self.draw_ui()

    def init_ui(self):
        screen_width, screen_height = get_renderer().get_screen().get_size()

        self.panel_size = [screen_width * 0.2, screen_height * 1.0]
        self.panel_location = [screen_width - self.panel_size[0], screen_height - self.panel_size[1]]
        self.panel = Panel(self.panel_location[0], self.panel_location[1], self.panel_size[0], self.panel_size[1])

        self.label = Text(0, 0, '')
        self.panel.add_child(self.label)

        # 按钮
        btn_width = self.panel_size[0]
        btn_height = 40
        self.reset_btn = Button(0, self.panel_size[1] - btn_height, btn_width, btn_height, "Reset")

        # 绑定
        P = cast(Panel, self.panel)
        P.add_child(self.reset_btn)


    # 绘制UI
    def draw_ui(self):
        get_renderer().draw_ui(cast(Panel, [self.panel]))

