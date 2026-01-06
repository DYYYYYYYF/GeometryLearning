import pygame
from .base import UIElement

# --- 文本组件 ---
class Text(UIElement):
    def __init__(self, x, y, text, font_size=24, color=(255, 255, 255)):
        super().__init__(x, y, 0, 0)
        self.text = text
        self.color = color

        try:
            # Arial (Win), Helvetica (Mac), DejaVu Sans (Linux), Sans (通用)
            self.font = pygame.font.SysFont(['arial', 'helvetica', 'dejavusans', 'sans'], font_size)
        except FileNotFoundError:
            print('can not find font, use system default font.')
            self.font = pygame.font.SysFont(None, font_size)

    def set_text(self, t):
        self.text = t

    def set_color(self, c):
        self.color = c

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, self.color)
        screen.blit(text_surface, (self.rect.x, self.rect.y))

