from .segment_intersection import algorithm_impl_segment_intersection
from .convex_hull import algorithm_impl_convex_generate

ALGORITHM_REGISTRY = {
    "segment_intersection": {
        "segments_required": 2,
        "algorithm_impl": algorithm_impl_segment_intersection,
    },
    "convex_generate": {
        "algorithm_impl": algorithm_impl_convex_generate,
    }
    # 未来可以添加更多算法，如 "凸包": {"function": convex_hull, ...}
}

def get_algorithm(name):
    return ALGORITHM_REGISTRY.get(name, None)

