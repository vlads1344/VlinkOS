import os
import sys

def run():
    if len(sys.argv) < 4: # 1:user, 2:root, 3:filename
        print("\033[1;31mUsage: edit <filename>\033[1;0m")
        return

    filename = sys.argv[3]
    print(f"\033[1;33mEditing {filename}. Type ':q' on a new line to save and exit.\033[0m")
    print("-" * 30)

    content = []
    # Если файл существует, загружаем его
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            content = f.readlines()
            for line in content:
                print(line.strip())

    while True:
        line = input()
        if line == ":q":
            break
        content.append(line + "\n")

    with open(filename, 'w') as f:
        f.writelines(content)
    print(f"\033[1;32mFile '{filename}' saved.\033[0m")

if __name__ == "__main__":
    run()