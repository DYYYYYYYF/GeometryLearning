import subprocess
import sys
import threading

# 用于安装库的函数
def install(package, event):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    event.set()  # 安装完成后，设置事件标志为已完成

# 检查并安装库的函数
def check_and_install(package):
    try:
        __import__(package)
    except ImportError:
        print(f"库 {package} 未安装，正在安装...")
        install_event = threading.Event()  # 创建一个事件标志
        install_thread = threading.Thread(target=install, args=(package, install_event))
        install_thread.start()
        
        install_event.wait()  # 主线程阻塞，直到安装完成
        print(f"库 {package} 安装完成！")
    else:
        print(f"库 {package} 已安装。")

check_and_install("pygame")

import pygame
import sys
from visualization import *
from algorithms.register import get_algorithm

implemented_algorithms = ["segment_intersection"]

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Compute Geometry Learning")

    current_algorithm = "segment_intersection"

    init_renderer(screen)

    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        clock.tick(60)
        evenets = pygame.event.get()
        for event in evenets:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                    continue
                if event.key == pygame.K_F1:
                    current_algorithm = "segment_intersection"
                    print("switch to segment_intersection algorithm")
                if event.key == pygame.K_F2:
                    current_algorithm = "convex_generate"
                    print("switch to convex_generate algorithm")

        # 运行当前算法
        implement = get_algorithm(current_algorithm)
        if implement:
            implement["algorithm_impl"](evenets)

    pygame.quit()
