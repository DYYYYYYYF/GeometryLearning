import pygame
from ui import *
from visualization import *
from typing import Optional, cast
from geometry.primitives import Point, Segment
from visualization.interaction import get_point_near_mouse
from algorithms.interface.algorithm_base import algorithm_base
from algorithms.impls.segment_intersection_core import segment_intersection_impl

class algorithm_segment_intersection(algorithm_base):
    _dragging_point = None

    def __init__(self):
        super().__init__()

        # 初始两个线段
        self.lines = [
            Segment(Point(200, 200), Point(700, 600)),
            Segment(Point(200, 600), Point(700, 200))
        ]

        cast(Text, self.label).set_text('Segment intersection')

        # 文本
        self.info_text_1 = Text(0, 40,  ' - drag segment end point.', 18)
        cast(Panel, self.panel).add_child(self.info_text_1)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self._dragging_point = get_point_near_mouse(event.pos, self.lines)
        if event.type == pygame.MOUSEBUTTONUP:
            self._dragging_point = None
        if event.type == pygame.MOUSEMOTION and self._dragging_point:
            self._dragging_point.x, self._dragging_point.y = event.pos

    def algorithm_impl(self):
        # 重置交点
        self.points = []

        ok, pt = segment_intersection_impl(self.lines[0], self.lines[1])
        if ok and pt: self.points.append(pt)

    def draw(self):
        # 运行算法
        self.algorithm_impl()
        # 绘制图像
        get_renderer().draw_scene(self.lines, self.points)

        # UI
        super().draw()

