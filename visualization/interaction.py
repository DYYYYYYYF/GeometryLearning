def get_point_near_mouse(mouse_pos, segments, threshold=10):
    for seg in segments:
        for pt in [seg.p1, seg.p2]:
            if (pt.x - mouse_pos[0])**2 + (pt.y - mouse_pos[1])**2 <= threshold**2:
                return pt
    return None

