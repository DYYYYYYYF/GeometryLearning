from geometry import *

# @params points: 图形点集
# @return1 list: 返回生成的凸包点集
# @return2 list: 返回生成的凸包边集
def convex_impl(points:list) -> tuple[list, list]:
    points = convex_generate(points)
    segments = generate_edges(points)
    return points, segments


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

