import pygame
from .base import UIElement

# --- 按钮组件 (继承自 UIElement) ---
class Button(UIElement):
    def __init__(self, x, y, width, height, text, callback=None):
        super().__init__(x, y, width, height)
        self.text = text
        self.callback = callback  # 点击后执行的函数
        self.color = (100, 100, 100)
        self.font = pygame.font.SysFont('Arial', 20)

    def set_callback(self, callback):
        if callback is not None:
            self.callback = callback

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
                if self.callback is not None:
                    self.callback() # 触发回调


