import platform
import os
import sys

# Цвета
C = "\033[1;36m" # Cyan
G = "\033[1;32m" # Green
Y = "\033[1;33m" # Yellow
W = "\033[0m"    # Reset

def run():
    # Собираем данные (аргументы передаются из ядра VlinkOS)
    user = sys.argv[1] if len(sys.argv) > 1 else "user"
    os_name = platform.system()
    node = platform.node()
    arch = platform.machine()
    py_ver = platform.python_version()

    # Используем fr"{}" для корректной работы бэкслешей в ASCII-арте
    logo = [
        fr"{C}  __      ___ _       _ {W}",
        fr"{C}  \ \    / / (_)     | |{W}   USER: {Y}{user}@{node}{W}",
        fr"{C}   \ \  / /| |_ _ __ | |{W}   OS: {Y}VlinkOS v1.0{W}",
        fr"{C}    \ \/ / | | | '_ \| |{W}   KERNEL: {Y}{os_name} {arch}{W}",
        fr"{C}     \  /  | | | | | | |{W}   PYTHON: {Y}{py_ver}{W}",
        fr"{C}      \/   |_|_|_| |_|_|{W}   SHELL: {Y}vlink-sh{W}"
    ]

    print()
    for line in logo:
        print(line)
    print()

if __name__ == "__main__":
    run()