import os
import sys

def run():
    # В ядре мы передаем: 1:user, 2:is_root, 3:filename
    if len(sys.argv) < 4:
        print("\033[1;31mUsage: create <name.ext> or create <folder_name>\033[0m")
        return

    target = sys.argv[3]

    try:
        # Если в имени есть точка, считаем это файлом
        if "." in target:
            if os.path.exists(target):
                print(f"\033[1;33mFile '{target}' already exists.\033[0m")
            else:
                with open(target, 'w') as f:
                    f.write("") # Создаем пустой файл
                print(f"\033[1;32mFile '{target}' created successfully.\033[0m")
        
        # Если точки нет, создаем папку
        else:
            if os.path.exists(target):
                print(f"\033[1;33mDirectory '{target}' already exists.\033[0m")
            else:
                os.makedirs(target)
                print(f"\033[1;32mDirectory '{target}' created successfully.\033[0m")
                
    except Exception as e:
        print(f"\033[1;31mError: {e}\033[0m")

if __name__ == "__main__":
    run()