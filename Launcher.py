import pygame
import sys
from visualization import *
from algorithms.register import get_algorithm

implemented_algorithms = ["segment_intersection"]

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Compute Geometry Learning")

    current_algorithm = "segment_intersection"

    init_renderer(screen)

    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        clock.tick(60)
        evenets = pygame.event.get()
        for event in evenets:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                    continue

        # 运行当前算法
        implement = get_algorithm(current_algorithm)
        if implement:
            implement["run_algorithm"](evenets)

    pygame.quit()
