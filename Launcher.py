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
from ui import *

WIDTH = 1200
HEIGHT = 800

def algorithm_switch(event) -> str:
    switched_algorithm = 'None'
    if event.key == pygame.K_F1:
        switched_algorithm = "segment_intersection"
        print("switch to segment_intersection algorithm")
    elif event.key == pygame.K_F2:
        switched_algorithm = "convex_generate"
        print("switch to convex_generate algorithm")
    return switched_algorithm



if __name__ == "__main__":
    # pygame
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Compute Geometry Learning")

    current_algorithm = "segment_intersection"

    init_renderer(screen)

    clock = pygame.time.Clock()
    is_running = True
    while is_running:
        delta_time = clock.tick(60) / 1000.0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False
                    continue

                current_algorithm = algorithm_switch(event)

         # 运行当前算法
        implement = get_algorithm(current_algorithm)
        if not implement:
            print("Invalid algorithm impl.")
            continue

        # Events
        implement.handle_events(events)

        # begin
        get_renderer().clear()

        # cmd
        implement.draw()

        # end
        get_renderer().swap()

    pygame.quit()
