from geometry import *

# @param triangle_points: 传入三角形顶点位置(A, B, C)
# @return set: 被覆盖的区域坐标集合set((x, y))
def rasterization_impl(triangle_points:list['Point']) -> set:
    # return barycentric_coordinates_impl(triangle_points)
    return line_sweep_impl(triangle_points)

def barycentric_coordinates_impl(triangle_points:list['Point']) -> set:
    """
    使用重心坐标法实现三角形光栅化填充
    """
    filled_pixels = set()

    if len(triangle_points) < 3:
        return filled_pixels

    # 1. 获取三角形的三个顶点坐标 (网格坐标)
    A = triangle_points[0]
    B = triangle_points[1]
    C = triangle_points[2]

    # 2. 计算三角形的包围盒 (Bounding Box)，缩小遍历范围
    min_x = int(min(A.x, B.x, C.x))
    max_x = int(max(A.x, B.x, C.x))
    min_y = int(min(A.y, B.y, C.y))
    max_y = int(max(A.y, B.y, C.y))

    # 定义叉积函数，用于判断点在向量哪一侧
    def cross_product(p1, p2, p3):
        return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)

    # 3. 遍历包围盒内的每一个像素格
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            # 取像素中心点进行判断
            P = Point(x, y)
            
            # 计算三个边的定向面积（叉积）
            # 注意：顺序需一致（如全顺时针或全逆时针）
            w0 = cross_product(B, C, P)
            w1 = cross_product(C, A, P)
            w2 = cross_product(A, B, P)

            # 4. 判断点是否在三角形内
            # 如果三个叉积符号相同，则点在内部
            if (w0 >= 0 and w1 >= 0 and w2 >= 0) or (w0 <= 0 and w1 <= 0 and w2 <= 0):
                filled_pixels.add((x, y))

    return filled_pixels


"""
基于扫描线切分（平底/平顶）的光栅化算法
"""
def line_sweep_impl(triangle_points) -> set:
    filled_pixels = set()
    if len(triangle_points) < 3:
        return filled_pixels

    # 1. 将顶点按 y 坐标从小到大排序
    pts = sorted(triangle_points, key=lambda p: p.y)
    p1, p2, p3 = pts

    # 2. 判断并切分三角形
    if p2.y == p3.y:
        # 本身就是平底三角形
        filled_pixels = fill_flat_bottom(p1, p2, p3)
    elif p1.y == p2.y:
        # 本身就是平顶三角形
        filled_pixels = fill_flat_top(p1, p2, p3)
    else:
        # 通用三角形：寻找中间点 p4，将其切分为平底和平顶
        # 利用相似三角形比例计算 p4 的 x 坐标
        alpha = (p2.y - p1.y) / (p3.y - p1.y)
        p4_x = p1.x + alpha * (p3.x - p1.x)
        p4 = Point(p4_x, p2.y)
        
        b_filled_pixels = fill_flat_bottom(p1, p2, p4)
        u_filled_pixels  = fill_flat_top(p2, p4, p3)

        filled_pixels.update(b_filled_pixels)
        filled_pixels.update(u_filled_pixels)

    return filled_pixels

"""绘制平底三角形 (v1 是顶点, v2-v3 是底边)"""
def fill_flat_bottom(v1, v2, v3) -> set:
    filled_pixels = set()

    # 确定底边的左右顺序
    left_v, right_v = (v2, v3) if v2.x < v3.x else (v3, v2)
    
    # 计算左右两条边的斜率倒数 (dx/dy)，避免每行重复除法
    height = v2.y - v1.y
    if height == 0: return filled_pixels
    
    inv_m1 = (left_v.x - v1.x) / height
    inv_m2 = (right_v.x - v1.x) / height
    
    # 逐行扫描
    cur_x1 = v1.x
    cur_x2 = v1.x
    
    # 使用 int(y) 确保网格对齐
    for y in range(int(v1.y), int(v2.y)):
        # 填充当前行：从左 x 到右 x
        for x in range(int(cur_x1), int(cur_x2) + 1):
            filled_pixels.add((x, y))
        cur_x1 += inv_m1
        cur_x2 += inv_m2

    return filled_pixels

"""绘制平顶三角形 (v1-v2 是顶边, v3 是顶点)"""
def fill_flat_top(v1, v2, v3) -> set:
    filled_pixels = set()
    left_v, right_v = (v1, v2) if v1.x < v2.x else (v2, v1)
    
    height = v3.y - v1.y
    if height == 0: return filled_pixels
    
    inv_m1 = (v3.x - left_v.x) / height
    inv_m2 = (v3.x - right_v.x) / height
    
    cur_x1 = left_v.x
    cur_x2 = right_v.x
    
    for y in range(int(v1.y), int(v3.y) + 1):
        for x in range(int(cur_x1), int(cur_x2) + 1):
            filled_pixels.add((x, y))
        cur_x1 += inv_m1
        cur_x2 += inv_m2

    return filled_pixels


