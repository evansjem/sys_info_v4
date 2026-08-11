import platform
import os
import socket

def get_system_info():
    info = {
        "System": platform.system(),
        "Node Name": platform.node(),
        "Release": platform.release(),
        "Version": platform.version(),
        "Machine": platform.machine(),
        "Processor": platform.processor(),
        "CPU Cores": os.cpu_count(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Current User": os.getlogin() if hasattr(os, 'getlogin') else 'N/A',
        "Working Directory": os.getcwd()
    }
    return info

if __name__ == "__main__":
    print("--- System Information ---")
    sys_info = get_system_info()
    for key, value in sys_info.items():
        print(f"{key}: {value}")
