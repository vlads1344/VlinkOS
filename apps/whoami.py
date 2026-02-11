import sys

# В Linux команда whoami просто говорит имя пользователя
# Но мы сделаем круче - с правами доступа

def run():
    # Мы можем передать имя пользователя как аргумент из ядра
    if len(sys.argv) > 1:
        user = sys.argv[1]
        is_root = "Yes (Superuser)" if sys.argv[2] == "True" else "No (Regular User)"
        
        print(f"Current user: \033[1;32m{user}\033[0m")
        print(f"Root privileges: \033[1;34m{is_root}\033[0m")
    else:
        print("Unknown user")

if __name__ == "__main__":
    run()