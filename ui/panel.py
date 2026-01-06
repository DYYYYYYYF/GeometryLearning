import pygame
from .base import UIElement

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
