import pygame
from visualization import *
from geometry.primitives import Point, Segment

points=[]
def convex_generate(points):
    if len(points) <= 1:
        return points
    points = sorted(points, key=lambda p: (p.x, p.y))

    def cross(o, a, b):
        return (a.x - o.x)*(b.y - o.y) - (a.y - o.y)*(b.x - o.x)

    lower = []
    for p in points:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

def generate_edges(points):
    segments = []
    if (len(points) < 2):
        return segments
    
    for p1, p2 in zip(points, points[1:]):
        segments.append(Segment(p1, p2))
    
    segments.append(Segment(points[0], points[-1]))
    return segments

def algorithm_impl_convex_generate(events):
    global points

    # 自定义点集
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            points.append(Point(x, y))

    points = convex_generate(points)
    segments = generate_edges(points)
    get_renderer().draw_scene(segments, points)