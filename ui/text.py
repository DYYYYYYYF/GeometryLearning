import pygame
from .base import UIElement

# --- 文本组件 ---
class Text(UIElement):
    def __init__(self, x, y, text, font_size=24, color=(255, 255, 255), auto_wrap=False, max_width=None):
        super().__init__(x, y, 0, 0)
        self.text = text
        self.color = color
        self.auto_wrap = auto_wrap      # 是否自动换行
        self.max_width = max_width      # 自动换行的最大宽度

        try:
            # Arial (Win), Helvetica (Mac), DejaVu Sans (Linux), Sans (通用)
            self.font = pygame.font.SysFont(['arial', 'helvetica', 'dejavusans', 'sans'], font_size)
        except FileNotFoundError:
            print('can not find font, use system default font.')
            self.font = pygame.font.SysFont(None, font_size)

    def set_text(self, t):
        self.text = t
        self._update_metrics()

    # 设置是否自动换行
    def set_wrap(self, auto_wrap, max_width = None):
        self.auto_wrap = auto_wrap
        self.max_width = max_width
        self._update_metrics()

    def set_color(self, c):
        self.color = c

    def draw(self, screen):
       # 文本拆分
        lines = str(self.text).split('\n')
        # 获取当前字体的行间距（两行基线之间的距离）
        line_height = self.font.get_linesize()
        # 逐行渲染并绘制
        for i, line in enumerate(lines):
            if line == "": # 处理连续换行的情况
                continue
                
            # 渲染当前行文本
            text_surface = self.font.render(line, True, self.color)
            
            # 计算当前行在屏幕上的垂直位置
            # y 轴位置 = 初始 y + 行号 * 行高
            draw_y = self.rect.y + (i * line_height)
            
            screen.blit(text_surface, (self.rect.x, draw_y))


    # 根据文本内容和换行设置，更新self.rect
    def _update_metrics(self):
        if not self.text:
            self.rect.width, self.rect.height = 0, 0
            return

        lines = str(self.text).split('\n')
        line_height = self.font.get_linesize()
        
        max_w = 0
        total_h = 0

        # 基础的 \n 换行后的宽高计算
        for line in lines:
            line_w, _ = self.font.size(line)
            max_w = max(max_w, line_w)
            total_h += line_height
        
        # 更新基类 rect 的尺寸
        self.rect.width = max_w
        self.rect.height = total_h

