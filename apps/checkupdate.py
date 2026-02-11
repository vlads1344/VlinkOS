import requests
import os
import sys

CURRENT_VERSION = "0.3"
UPDATE_URL = "http://45.143.138.52/vlinkos" # Папка на сервере

def run():
    print(f"Checking for updates... (Current version: {CURRENT_VERSION})")
    try:
        # 1. Проверяем версию
        response = requests.get(f"{UPDATE_URL}/version.json", timeout=5)
        data = response.json()
        remote_version = data["version"]

        if remote_version > CURRENT_VERSION:
            print(f"\033[1;33mNew version available: {remote_version}\033[0m")
            choice = input("Update now? (y/n): ").lower()
            
            if choice == 'y':
                update_files(data["files"])
        else:
            print("\033[1;32mYour VlinkOS is up to date.\033[0m")
            
    except Exception as e:
        print(f"\033[1;31mUpdate error: {e}\033[0m")

def update_files(file_list):
    """Скачивает и заменяет файлы"""
    print("Downloading files...")
    for file in file_list:
        try:
            r = requests.get(f"{UPDATE_URL}/{file}")
            with open(file, "wb") as f:
                f.write(r.content)
            print(f"  [OK] {file}")
        except:
            print(f"  [FAIL] {file}")
    
    print("\n\033[1;32mUpdate complete! Please run 'rst' to restart.\033[0m")

if __name__ == "__main__":
    run()