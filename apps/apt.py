import sys
import requests
import os

SERVER_REPO = "http://45.143.138.52/vlinkos/repo"

def run():
    if len(sys.argv) < 5: # sudo + apt + install + package
        print("Usage: apt install <package>")
        return

    action = sys.argv[3] # install
    package = sys.argv[4] # например, minesweeper
    is_root = sys.argv[2] == "True"

    if not is_root:
        print("\033[1;31mE: Could not open lock file - open (13: Permission denied)\033[0m")
        return

    if action == "install":
        print(f"Reading package lists... Done")
        print(f"Building dependency tree... Done")
        print(f"The following NEW packages will be installed: {package}")
        
        try:
            # Скачиваем игру/программу с сервера
            r = requests.get(f"{SERVER_REPO}/{package}.py")
            if r.status_code == 200:
                with open(f"apps/{package}.py", "wb") as f:
                    f.write(r.content)
                print(f"\033[1;32mGet:1 {SERVER_REPO} {package} [OK]\033[0m")
                print(f"Fetched {len(r.content)} B. Successfully installed.")
            else:
                print(f"\033[1;31mE: Unable to locate package {package}\033[0m")
        except Exception as e:
            print(f"Connection failed: {e}")

if __name__ == "__main__":
    run()