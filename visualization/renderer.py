import pygame

def draw_point(screen, point, color=(0, 0, 255), radius=5):
    pygame.draw.circle(screen, color, (int(point.x), int(point.y)), radius)

def draw_segment(screen, segment, color=(0, 0, 0), width=2):
    pygame.draw.line(screen, color, (segment.p1.x, segment.p1.y), (segment.p2.x, segment.p2.y), width)

def draw_polygon(screen, points, color=(255, 0, 0), width=2):
    if len(points) >= 2:
        pygame.draw.lines(screen, color, True, [(p.x, p.y) for p in points], width)

def draw_scene(screen, segments, points):
    screen.fill((255, 255, 255))
    for seg in segments:
        draw_segment(screen, seg, color=(0, 0, 0))
    if points:
        draw_point(screen, points, color=(0, 200, 0))
    pygame.display.flip()
