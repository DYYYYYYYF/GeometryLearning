from .segment_intersection import algorithm_impl

ALGORITHM_REGISTRY = {
    "segment_intersection": {
        "segments_required": 2,
        "run_algorithm": algorithm_impl,
    },
    # 未来可以添加更多算法，如 "凸包": {"function": convex_hull, ...}
}

def get_algorithm(name):
    return ALGORITHM_REGISTRY.get(name, None)

