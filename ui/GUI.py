import pygame

# --- 基础 UI 类 (基类) ---
class UIElement:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pass  # 由子类实现

    def handle_event(self, event):
        pass  # 由子类实现

# --- 文本组件 ---
class Text(UIElement):
    def __init__(self, x, y, text, font_size=24, color=(255, 255, 255)):
        super().__init__(x, y, 0, 0)
        self.text = text
        self.color = color

        try:
            self.font = pygame.font.SysFont('Arial', font_size)
        except FileNotFoundError:
            self.font = pygame.font.SysFont(None, font_size)

    def set_text(self, t):
        self.text = t

    def set_color(self, c):
        self.color = c

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.rect.x, self.rect.y))

# --- 按钮组件 (继承自 UIElement) ---
class Button(UIElement):
    def __init__(self, x, y, width, height, text, callback):
        super().__init__(x, y, width, height)
        self.text = text
        self.callback = callback  # 点击后执行的函数
        self.color = (100, 100, 100)
        self.font = pygame.font.SysFont('Arial', 20)

    def draw(self, screen):
        # 绘制按钮矩形
        pygame.draw.rect(screen, self.color, self.rect)
        # 绘制文字居中
        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback() # 触发回调

# 视窗
class Panel(UIElement):
    def __init__(self, x, y, width, height, color=(50, 50, 50)):
        super().__init__(x, y, width, height)
        self.color = color
        self.children = []

    def add_child(self, child):
        # 将子组件的坐标改为相对于 Panel 的坐标
        child.rect.x += self.rect.x
        child.rect.y += self.rect.y
        self.children.append(child)

    def draw(self, screen):
        # 先画背景
        pygame.draw.rect(screen, self.color, self.rect)
        # 再画子组件
        for child in self.children:
            child.draw(screen)

    def handle_event(self, event):
        for child in self.children:
            child.handle_event(event)
