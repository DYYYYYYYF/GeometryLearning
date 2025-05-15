import pygame
import sys
from geometry.primitives import Point, Segment
from algorithms.register import get_algorithm
from visualization.renderer import draw_scene
from visualization.interaction import get_point_near_mouse

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Compute Geometry Learning")

    # 初始两个线段
    segments = [
        Segment(Point(100, 100), Point(300, 300)),
        Segment(Point(100, 300), Point(300, 100))
    ]

    current_algorithm = "segment_intersection"
    dragging_point = None
    clock = pygame.time.Clock()

    is_running = True
    while is_running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                    continue
            elif event.type == pygame.MOUSEBUTTONDOWN:
                dragging_point = get_point_near_mouse(event.pos, segments)
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_point = None
            elif event.type == pygame.MOUSEMOTION and dragging_point:
                dragging_point.x, dragging_point.y = event.pos

        # 运行当前算法
        result = get_algorithm(current_algorithm)
        intersection = None
        if result and len(segments) >= result["segments_required"]:
            ok, pt = result["function"](segments[0], segments[1])
            if ok and pt: intersection = pt

        draw_scene(screen, segments, intersection)

    pygame.quit()
