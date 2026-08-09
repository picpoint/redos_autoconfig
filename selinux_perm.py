import os
# from colorama import init, Fore, Back, Style

def selinux_true_func():
    print(f"[*] START SELINUX")
    os.chdir("/etc/selinux/")    

    with open('config', 'r') as f:
        old_data = f.read()

    new_data = old_data.replace('SELINUX=enforcing', 'SELINUX=permissive')

    with open('config', 'w') as f:
        f.write(new_data)
    print(f"[+] SELINUX SUCCESSFULLY")
    print("===============================")