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

    def get_screen(self):
        return self.screen

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

    def draw_rect(self, x, y, width, height, color=(255, 200, 0), filled=True):
        width_val = 0 if filled else 2
        pygame.draw.rect(self.screen, color, (int(x), int(y), int(width), int(height)), width_val)

    def draw_grid(self, cols, rows, grid_size, color=(220, 220, 220)):
        screen_h = self.screen.get_height()
        grid_area_w = cols * grid_size
        # 绘制竖线
        for x in range(cols + 1):
            pygame.draw.line(self.screen, color, (x * grid_size, 0), (x * grid_size, screen_h), 1)
        # 绘制横线
        for y in range(rows + 1):
            pygame.draw.line(self.screen, color, (0, y * grid_size), (grid_area_w, y * grid_size), 1)

    def draw_scene(self, segments=None, points=None):
        if segments:
            for seg in segments:
                self.draw_segment(seg)
        if points:
            for p in points:
                self.draw_point(p, color=(0, 200, 0))

    def draw_ui(self, elements):
        for e in elements:
            e.draw(self.screen)


    def swap(self):
        pygame.display.flip()

_renderer_instance = None

def init_renderer(screen):
    global _renderer_instance
    _renderer_instance = Renderer(screen)

def get_renderer():
    if _renderer_instance is None:
        raise RuntimeError("Renderer 未初始化，请先在 main 中调用 init_renderer(screen)")
    return _renderer_instance
