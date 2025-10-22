import pygame

class Renderer:
    _instance = None

    def __new__(cls, screen=None):
        if screen == None: return cls._instance
        if cls._instance is None:
            if screen is None:
                raise ValueError("第一次创建 Renderer 时必须提供 screen")
            cls._instance = super(Renderer, cls).__new__(cls)
            cls._instance.screen = screen
            cls._instance.background_color = (255, 255, 255)
        return cls._instance

    def __init__(self, screen):
        self.screen = screen
        self.background_color = (255, 255, 255)

    def clear(self):
        self.screen.fill(self.background_color)

    def draw_point(self, point, color=(0, 0, 255), radius=5):
        pygame.draw.circle(self.screen, color, (int(point.x), int(point.y)), radius)

    def draw_segment(self, segment, color=(0, 0, 0), width=2):
        pygame.draw.line(self.screen, color,
                         (int(segment.p1.x), int(segment.p1.y)),
                         (int(segment.p2.x), int(segment.p2.y)), width)

    def draw_polygon(self, points, color=(255, 0, 0), width=2):
        if len(points) >= 2:
            pygame.draw.lines(self.screen, color, True,
                              [(int(p.x), int(p.y)) for p in points], width)

    def draw_scene(self, segments=None, points=None):
        self.clear()
        if segments:
            for seg in segments:
                self.draw_segment(seg)
        if points:
            for p in points:
                self.draw_point(p, color=(0, 200, 0))
        pygame.display.flip()

_renderer_instance = None

def init_renderer(screen):
    global _renderer_instance
    _renderer_instance = Renderer(screen)

def get_renderer():
    if _renderer_instance is None:
        raise RuntimeError("Renderer 未初始化，请先在 main 中调用 init_renderer(screen)")
    return _renderer_instance