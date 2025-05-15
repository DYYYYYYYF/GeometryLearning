import pygame
from visualization import *
from geometry.primitives import Point, Segment
from visualization.interaction import get_point_near_mouse

# 初始两个线段
segments = [
    Segment(Point(100, 100), Point(300, 300)),
    Segment(Point(100, 300), Point(300, 100))
]
dragging_point = None

def cross(o, a, b):
    return (a.x - o.x)*(b.y - o.y) - (a.y - o.y)*(b.x - o.x)

def on_segment(p1, p2, q):
    return (min(p1.x, p2.x) <= q.x <= max(p1.x, p2.x) and
            min(p1.y, p2.y) <= q.y <= max(p1.y, p2.y))

def segment_intersection(seg1: Segment, seg2: Segment):
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
        if cross(a, b, c) == 0 and on_segment(a, b, c):
            return True, c

    return False, None

def algorithm_impl(events):
    global dragging_point
    global segments

    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            dragging_point = get_point_near_mouse(event.pos, segments)
        if event.type == pygame.MOUSEBUTTONUP:
            dragging_point = None
        if event.type == pygame.MOUSEMOTION and dragging_point:
            dragging_point.x, dragging_point.y = event.pos

    intersection = []
    if len(segments) >= 2:
        ok, pt = segment_intersection(segments[0], segments[1])
        if ok and pt: intersection.append(pt)

        renderer = get_renderer()
        renderer.draw_scene(segments, intersection)




