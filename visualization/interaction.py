# 获取当前坐标是否处于某线段端点附近
# @param pos：鼠标位置
# @param segments：线段
# @param radius：阈值，默认为10(pixel)
def get_point_near_mouse(pos, segments, radius=10):
    # 鼠标坐标
    mx, my = pos
    for segment in segments:
        # 线段两端点
        for pt in [segment.p1, segment.p2]:
            if abs(mx - pt.x) < radius and abs(my - pt.y) < radius:
                return pt
    return None
