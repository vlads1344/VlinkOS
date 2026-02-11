import os
import subprocess
import time
import sys
import platform
import ctypes
import json
import requests

# --- Инициализация ANSI цветов для Windows ---
if os.name == 'nt':
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

# --- Константы системы ---
USER_DB = "users.json"
SERVER_IP = "45.143.138.52"
GREEN, BLUE, CYAN, RED, YELLOW, RESET = "\033[1;32m", "\033[1;34m", "\033[1;36m", "\033[1;31m", "\033[1;33m", "\033[0m"

# --- Работа с базой данных пользователей ---
def load_users():
    if not os.path.exists(USER_DB):
        return {}
    try:
        with open(USER_DB, "r") as f:
            content = f.read().strip()
            return json.loads(content) if content else {}
    except Exception:
        return {}

def save_users(users):
    with open(USER_DB, "w") as f:
        json.dump(users, f, indent=4)

# --- Система регистрации и Root-доступа через сервер ---
def setup_wizard():
    print(f"\n{CYAN}=== VlinkOS First-Time Setup ==={RESET}")
    username = input("Enter new username: ").strip()
    password = input("Enter password: ").strip()
    
    is_root = False
    want_root = input("Do you want root privileges? (y/n): ").lower() == 'y'
    
    if want_root:
        root_pass = input("Enter GLOBAL ROOT PASSWORD (from server): ").strip()
        print(f"{YELLOW}Verifying with {SERVER_IP}...{RESET}")
        try:
            url = f"http://{SERVER_IP}/vlinkos/check_root.php?pass={root_pass}"
            response = requests.get(url, timeout=5)
            if response.text.strip() == "granted":
                print(f"{GREEN}Root access granted by server!{RESET}")
                is_root = True
            else:
                print(f"{RED}Invalid Root Password! Creating regular user...{RESET}")
        except Exception as e:
            print(f"{RED}Server connection error. Creating regular user.{RESET}")

    users = {username: {"password": password, "is_root": is_root}}
    save_users(users)
    print(f"{GREEN}Account '{username}' created successfully!{RESET}\n")
    return username, is_root

def login():
    users = load_users()
    if not users:
        return setup_wizard()
    
    print(f"\n{CYAN}--- VlinkOS Login ---{RESET}")
    while True:
        user = input("Username: ").strip()
        if user in users:
            pwd = input("Password: ").strip()
            if users[user]["password"] == pwd:
                return user, users[user]["is_root"]
            else:
                print(f"{RED}Wrong password!{RESET}")
        else:
            print(f"{RED}User not found!{RESET}")

# --- Главный цикл системы ---
def main():
    print(f"{CYAN}--- VlinkOS Kernel v0.4.1 Initializing ---{RESET}")
    time.sleep(0.5)
    
    current_user, is_root = login()
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"\nWelcome to VlinkOS, {GREEN}{current_user}{RESET}!")
    print("Type 'help' to see available commands.")

    while True:
        # Формирование строки пути (Prompt)
        cwd = os.getcwd().replace(os.path.expanduser("~"), "~")
        color = RED if is_root else GREEN
        symbol = "#" if is_root else "$"
        
        prompt = f"{color}{current_user}{RESET}@{CYAN}vlink-pc{RESET}:{BLUE}{cwd}{RESET}{symbol} "
        
        try:
            cmd_input = input(prompt).strip()
        except KeyboardInterrupt:
            print("\nUse 'exit' to logout.")
            continue

        if not cmd_input: continue
            
        parts = cmd_input.split()
        cmd = parts[0].lower()
        args = parts[1:]

        # --- Команда HELP (Таблица) ---
        if cmd == "help":
            print(f"\n{CYAN}VlinkOS - Command Reference{RESET}")
            print(f"{'='*60}")
            print(f"{YELLOW}{'Command':<15} {'Type':<12} {'Description':<30}{RESET}")
            print(f"{'-'*60}")
            
            builtins = [
                ("ls", "Internal", "List directory files"),
                ("cd", "Internal", "Change directory"),
                ("clear", "Internal", "Clear terminal screen"),
                ("rst", "System", "Restart VlinkOS"),
                ("help", "Internal", "Show this help table"),
                ("exit", "System", "Power off / Logout")
            ]
            
            for name, c_type, desc in builtins:
                print(f"{BLUE}{name:<15}{RESET} {GREEN}{c_type:<12}{RESET} {desc:<30}")

            apps_dir = os.path.join(base_dir, "apps")
            if os.path.exists(apps_dir):
                apps = [f.replace('.py', '') for f in os.listdir(apps_dir) if f.endswith('.py')]
                if apps:
                    print(f"{'-'*60}")
                    for app in apps:
                        print(f"{CYAN}{app:<15}{RESET} {YELLOW}{'External':<12}{RESET} {'External Application':<30}")
            
            print(f"{'='*60}\n")

        # --- Другие встроенные команды ---
        elif cmd == "exit":
            print(f"{YELLOW}System halted.{RESET}")
            break
        
        elif cmd == "rst":
            print(f"{YELLOW}Restarting VlinkOS...{RESET}")
            os.execv(sys.executable, [sys.executable] + sys.argv)

        elif cmd == "clear":
            os.system('cls' if os.name == 'nt' else 'clear')

        elif cmd == "ls":
            try:
                for f in os.listdir('.'):
                    c = BLUE if os.path.isdir(f) else RESET
                    print(f"{c}{f}{RESET}", end="  ")
                print()
            except Exception as e:
                print(f"{RED}ls error: {e}{RESET}")

        elif cmd == "cd":
            try:
                os.chdir(args[0] if args else os.path.expanduser("~"))
            except Exception as e:
                print(f"{RED}cd: {e}{RESET}")

        # --- Запуск приложений из /apps ---
        else:
            app_path = os.path.join(base_dir, "apps", f"{cmd}.py")
            if os.path.exists(app_path):
                subprocess.run([sys.executable, app_path, current_user, str(is_root)] + args)
            else:
                print(f"{RED}vlink-sh: {cmd}: command not found{RESET}")

if __name__ == "__main__":
    main()