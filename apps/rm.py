import os
import sys
import shutil

def run():
    if len(sys.argv) < 4:
        print("\033[1;31mUsage: rm <file_or_folder>\033[0m")
        return

    target = sys.argv[3]

    if not os.path.exists(target):
        print(f"\033[1;31mError: '{target}' not found.\033[0m")
        return

    try:
        if os.path.isfile(target):
            os.remove(target)
            print(f"\033[1;32mFile '{target}' removed.\033[0m")
        elif os.path.isdir(target):
            confirm = input(f"Are you sure you want to delete folder '{target}' and ALL its content? (y/n): ")
            if confirm.lower() == 'y':
                shutil.rmtree(target) # Удаляет папку со всем содержимым
                print(f"\033[1;32mDirectory '{target}' removed.\033[0m")
    except Exception as e:
        print(f"\033[1;31mError: {e}\033[0m")

if __name__ == "__main__":
    run()