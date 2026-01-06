import pygame

# --- 基础 UI 类 (基类) ---
class UIElement:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, screen):
        pass  # 由子类实现

    def handle_event(self, event):
        pass  # 由子类实现

