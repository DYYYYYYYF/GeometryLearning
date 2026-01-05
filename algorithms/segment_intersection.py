import pygame
from typing import Optional
from visualization import *
from .algorithm_base import algorithm_base
from geometry.primitives import Point, Segment
from visualization.interaction import get_point_near_mouse

# 向量叉乘
def cross(o, a, b):
    return (a.x - o.x)*(b.y - o.y) - (a.y - o.y)*(b.x - o.x)

class algorithm_segment_intersection(algorithm_base):
    _dragging_point = None

    def __init__(self):
        super().__init__()

        # 初始两个线段
        self.lines = [
            Segment(Point(100, 100), Point(300, 300)),
            Segment(Point(100, 300), Point(300, 100))
        ]

    def on_segment(self, p1, p2, q):
        return (min(p1.x, p2.x) <= q.x <= max(p1.x, p2.x) and
                min(p1.y, p2.y) <= q.y <= max(p1.y, p2.y))

    def segment_intersection(self, seg1: Segment, seg2: Segment) -> tuple[bool, Optional[Point]]:
        p1, p2, q1, q2 = seg1.p1, seg1.p2, seg2.p1, seg2.p2
        d1 = cross(p1, p2, q1)
        d2 = cross(p1, p2, q2)
        d3 = cross(q1, q2, p1)
        d4 = cross(q1, q2, p2)

        if d1 * d2 < 0 and d3 * d4 < 0:
            denom = (p1.x - p2.x) * (q1.y - q2.y) - (p1.y - p2.y) * (q1.x - q2.x)
            if denom == 0: return True, None
            x = ((p1.x*p2.y - p1.y*p2.x)*(q1.x - q2.x) - (p1.x - p2.x)*(q1.x*q2.y - q1.y*q2.x)) / denom
            y = ((p1.x*p2.y - p1.y*p2.x)*(q1.y - q2.y) - (p1.y - p2.y)*(q1.x*q2.y - q1.y*q2.x)) / denom
            return True, Point(x, y)

        for a, b, c in [(p1, p2, q1), (p1, p2, q2), (q1, q2, p1), (q1, q2, p2)]:
            if cross(a, b, c) == 0 and self.on_segment(a, b, c):
                return True, c

        return False, None

    def handle_events(self, events):
        # 拖拽线段
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._dragging_point = get_point_near_mouse(event.pos, self.lines)
            if event.type == pygame.MOUSEBUTTONUP:
                self._dragging_point = None
            if event.type == pygame.MOUSEMOTION and self._dragging_point:
                self._dragging_point.x, self._dragging_point.y = event.pos

    def algorithm_impl(self):
        # 重置交点
        self.points = []

        ok, pt = self.segment_intersection(self.lines[0], self.lines[1])
        if ok and pt: self.points.append(pt)

    def draw(self):
        # 运行算法
        self.algorithm_impl()
        # 绘制图像
        get_renderer().draw_scene(self.lines, self.points)

        # UI
        super().draw()

