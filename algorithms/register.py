from .layouts.segment_intersection import algorithm_segment_intersection
from .layouts.convex_generate import algorithm_convex_generate
from .layouts.rasterization import algorithm_rasterization

_ALGO_CLASSES = {
    'segment_intersection': algorithm_segment_intersection,
    'convex_generate': algorithm_convex_generate,
    'rasterization': algorithm_rasterization,
}

# 实例缓存
_instances = {}

"""
根据名称获取算法单例
"""
def get_algorithm(name):
    # 检查名称是否合法
    if name not in _ALGO_CLASSES:
        print(f"Error: Algorithm {name} not found.")
        return None
    
    # 如果实例不存在，则创建它（懒加载）
    if name not in _instances:
        print(f"Initializing singleton for: {name}")
        # 获取类并实例化
        _instances[name] = _ALGO_CLASSES[name]()
    
    return _instances[name]


