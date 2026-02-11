import sys
import subprocess
import requests

SERVER_IP = "45.143.138.52"

def run():
    if len(sys.argv) < 4:
        print("\033[1;31mUsage: sudo <command> <args>\033[0m")
        return

    # Запрашиваем глобальный пароль для подтверждения действия
    pwd = input(f"\033[1;33m[sudo] password for root: \033[0m")
    
    try:
        res = requests.get(f"http://{SERVER_IP}/vlinkos/check_root.php?pass={pwd}", timeout=5)
        if res.text.strip() == "granted":
            # Запускаем команду, которая идет после слова sudo
            cmd_to_run = sys.argv[3]
            args_for_cmd = sys.argv[4:]
            
            # Выполняем команду, передавая ей True в качестве is_root
            current_user = sys.argv[1]
            subprocess.run([sys.executable, f"apps/{cmd_to_run}.py", current_user, "True"] + args_for_cmd)
        else:
            print("\033[1;31mSorry, try again.\033[0m")
    except Exception as e:
        print(f"\033[1;31mConnection error: {e}\033[0m")

if __name__ == "__main__":
    run()