def get_point_near_mouse(pos, segments, radius=10):
    mx, my = pos
    for segment in segments:
        for pt in [segment.p1, segment.p2]:
            if abs(mx - pt.x) < radius and abs(my - pt.y) < radius:
                return pt
    return None
