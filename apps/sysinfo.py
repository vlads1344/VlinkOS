import platform
import sys
import os
import psutil # Библиотека для работы с процессами и системными ресурсами
import time

# Цвета для оформления
G = "\033[1;32m" # Green
B = "\033[1;34m" # Blue
Y = "\033[1;33m" # Yellow
R = "\033[1;31m" # Red
W = "\033[0m"    # White

def get_size(bytes):
    """Преобразует байты в читаемый формат (МБ, ГБ)"""
    for unit in ['', 'K', 'M', 'G', 'T']:
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
        bytes /= 1024

def run():
    print(f"{B}--- VlinkOS System Information ---{W}")
    
    # Данные процессора
    print(f"{G}[CPU]{W}")
    print(f"  Processor: {platform.processor()}")
    print(f"  Cores: {psutil.cpu_count(logical=False)} Phys / {psutil.cpu_count(logical=True)} Logic")
    print(f"  Usage: {psutil.cpu_percent()}%")

    # Данные памяти
    print(f"\n{G}[Memory]{W}")
    mem = psutil.virtual_memory()
    print(f"  Total: {get_size(mem.total)}")
    print(f"  Used:  {get_size(mem.used)} ({mem.percent}%)")
    print(f"  Free:  {get_size(mem.available)}")

    # Данные диска
    print(f"\n{G}[Storage]{W}")
    disk = psutil.disk_usage('/')
    print(f"  Total: {get_size(disk.total)}")
    print(f"  Used:  {get_size(disk.used)} ({disk.percent}%)")
    print(f"  Free:  {get_size(disk.free)}")

    # Система
    print(f"\n{G}[OS Platform]{W}")
    print(f"  Node Name: {platform.node()}")
    print(f"  OS: {platform.system()} {platform.release()}")
    print(f"  Python: {sys.version.split()[0]}")

if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(f"{R}Error gathering system info: {e}{W}")