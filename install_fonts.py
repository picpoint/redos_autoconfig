import subprocess
# from colorama import init, Fore, Back, Style


def install_fonts_func():
    print(f"[*] START INSTALL FONTS")
    shell_command = "dnf install msttcore-fonts-installer -y"
    subprocess.run(shell_command, shell=True, check=True)
    print(f"[+] INSTALL FONTS SUCCESSFULLY")
    print("===============================")