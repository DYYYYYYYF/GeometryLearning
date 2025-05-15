def convex_hull(points):
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

