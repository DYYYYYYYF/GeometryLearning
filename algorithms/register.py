from .segment_intersection import segment_intersection

ALGORITHM_REGISTRY = {
    "segment_intersection": {
        "segments_required": 2,
        "function": segment_intersection,
    },
    # 未来可以添加更多算法，如 "凸包": {"function": convex_hull, ...}
}

def get_algorithm(name):
    return ALGORITHM_REGISTRY.get(name, None)

