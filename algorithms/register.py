from .segment_intersection import algorithm_segment_intersection
from .convex_generate import algorithm_convex_generate

algorithm_segment_intersection_instance = None
algorithm_convex_generate_instance = None

def get_algorithm(name):
    global algorithm_segment_intersection_instance, algorithm_convex_generate_instance

    if (name == 'convex_generate'):
        if algorithm_convex_generate_instance is None:
            algorithm_convex_generate_instance = algorithm_convex_generate()
        return algorithm_convex_generate_instance
    elif (name == 'segment_intersection'):
        if algorithm_segment_intersection_instance is None:
            algorithm_segment_intersection_instance = algorithm_segment_intersection()
        return algorithm_segment_intersection_instance

