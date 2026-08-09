import subprocess


def reboot_system_func():
    print(f"[+] START REBOOT SYSTEM")
    shell_command = "reboot"
    subprocess.run(shell_command, shell=True, check=True)
    print("===============================")