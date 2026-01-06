import pygame
from ui import *
from visualization import *
from geometry.primitives import Point, Segment
from algorithms.interface.algorithm_base import algorithm_base
from algorithms.impls.rasterization_core import rasterization_impl
from typing import cast

class algorithm_rasterization(algorithm_base):
    def __init__(self, grid_size=20):
        self.grid_size = grid_size
        self.grid_rows = 0
        self.grid_cols = 0
        self.triangle_points = []
        self.filled_pixels = set()
        
        super().__init__()
        if self.label:
            self.set_label("rasterization algorithm")

    def init_ui(self):
        super().init_ui() # 初始化 panel 和 size
        renderer = get_renderer()
        screen_w, screen_h = renderer.get_screen().get_size()
        
        # 排除 UI Panel 宽度
        available_width = screen_w - self.panel_size[0]
        self.grid_cols = int(available_width // self.grid_size)
        self.grid_rows = int(screen_h // self.grid_size)

        # 子类新内容
        self.info_text_1 = Text(0, 40,  ' - click to form a triangle.', 18)
        cast(Panel, self.panel).add_child(self.info_text_1)

        # 绑定callback
        self.set_reset_callback(self.reset)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            # 限制点击区域在网格内
            if mouse_pos[0] < (get_renderer().get_screen().get_width() - self.panel_size[0]):
                # 转换坐标为网格索引
                gx = mouse_pos[0] // self.grid_size
                gy = mouse_pos[1] // self.grid_size
                
                if len(self.triangle_points) < 3:
                    self.triangle_points.append(Point(gx, gy))
                    
                if len(self.triangle_points) == 3:
                    if self.info_text_1: self.info_text_1.set_text(" - Status: Rasterizing...")
                    if self.filled_pixels: self.filled_pixels.clear()
                    self.algorithm_impl()

    def algorithm_impl(self):
        self.filled_pixels = rasterization_impl(self.triangle_points)

        # 更新 UI 信息
        A = self.triangle_points[0]
        B = self.triangle_points[1]
        C = self.triangle_points[2]

        self.info_text_1.set_text(
            f"Vertices: \n({A.x},{A.y}), ({B.x},{B.y}), ({C.x},{C.y})\n"
            f"Pixels Filled: {len(self.filled_pixels or [])}\n"
            "Status: Done"
        )
       
    def draw(self):
        renderer = get_renderer()
        
        # 1. 使用 Renderer 绘制背景网格
        renderer.draw_grid(self.grid_cols, self.grid_rows, self.grid_size)
        
        # 2. 绘制已填充的“像素”
        if self.filled_pixels is None or []:
            return

        for (gx, gy) in self.filled_pixels:
            # 限制在网格边界内
            gx = max(0, min(self.grid_cols - 1, gx))
            gy = max(0, min(self.grid_rows - 1, gy))

            renderer.draw_rect(
                gx * self.grid_size, 
                gy * self.grid_size, 
                self.grid_size, 
                self.grid_size
            )

        # 3. 绘制三角形辅助线 (使用 Point 转换回屏幕坐标)
        if len(self.triangle_points) >= 2:
            # 转换逻辑：网格中心点坐标
            screen_pts = [
                Point(p.x * self.grid_size + self.grid_size/2, 
                      p.y * self.grid_size + self.grid_size/2) 
                for p in self.triangle_points
            ]
            
            if len(screen_pts) == 3:
                renderer.draw_polygon(screen_pts, color=(255, 0, 0)) #
            else:
                # 绘制第一条边
                seg = Segment(screen_pts[0], screen_pts[1]) #
                renderer.draw_segment(seg, color=(255, 0, 0)) #

        # 4. 绘制 UI 面板
        super().draw()

    def reset(self):
        self.triangle_points = []
        if self.filled_pixels: self.filled_pixels.clear()
        if self.info_text_1:
            self.info_text_1.set_text(" - Click 3 points to form a triangle")
