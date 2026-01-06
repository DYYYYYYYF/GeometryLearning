from .layouts.segment_intersection import algorithm_segment_intersection
from .layouts.convex_generate import algorithm_convex_generate
from .layouts.rasterization import algorithm_rasterization

algorithm_segment_intersection_instance = None
algorithm_convex_generate_instance = None
algorithm_rasterization_instance = None

def get_algorithm(name):
    if (name == 'convex_generate'):
        global algorithm_convex_generate_instance
        if algorithm_convex_generate_instance is None:
            algorithm_convex_generate_instance = algorithm_convex_generate()
        return algorithm_convex_generate_instance
    elif (name == 'segment_intersection'):
        global algorithm_segment_intersection_instance
        if algorithm_segment_intersection_instance is None:
            algorithm_segment_intersection_instance = algorithm_segment_intersection()
        return algorithm_segment_intersection_instance
    elif (name == 'rasterization'):
        global algorithm_rasterization_instance
        if algorithm_rasterization_instance is None:
            algorithm_rasterization_instance = algorithm_rasterization()
        return algorithm_rasterization_instance

