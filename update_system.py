import subprocess
import os
# from colorama import init, Fore, Back, Style


def update_system_func():
    print(f"[*] START UPDATE SYSTEM")
    if os.geteuid() != 0:
        print("[-]NEED ROOT RULES!")
        exit(1)
    shell_command = "dnf makecache && dnf upgrade -y"
    print(f"[*] RUN UPDATE SYSTEM {shell_command}")
    subprocess.run(shell_command, shell=True, check=True)
    print(f"[+] UPDATE SYSTEM SUCCESSFULLY")
    print("===============================")