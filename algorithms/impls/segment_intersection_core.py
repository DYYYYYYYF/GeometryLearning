from geometry import *
from typing import Optional

# @params seg1: 待求解线段1
# @params seg2: 待求解线段2
# @return1 bool: 是否有焦点
# @return2 Point: 如果存在交点则返回交点，否则返回None
def segment_intersection_impl(seg1: Segment, seg2: Segment) -> tuple[bool, Optional[Point]]:
    # 辅助方法
    def cross(o, a, b):
        return (a.x - o.x)*(b.y - o.y) - (a.y - o.y)*(b.x - o.x)

    def on_segment(p1, p2, q):
        return (min(p1.x, p2.x) <= q.x <= max(p1.x, p2.x) and
                min(p1.y, p2.y) <= q.y <= max(p1.y, p2.y))

    # 算法实现
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


