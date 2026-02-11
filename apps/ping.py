import sys
import platform
import subprocess

def ping(host):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '4', host]
    
    print(f"VlinkOS PING {host} with 32 bytes of data:")
    
    # Запускаем и ловим вывод
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Декодируем из cp866 (для Windows), чтобы убрать кракозябры
    try:
        output = result.stdout.decode('cp866')
        print(output)
    except:
        print(result.stdout.decode('utf-8', errors='ignore'))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        ping(sys.argv[1])
    else:
        print("Usage: ping <hostname/ip>")