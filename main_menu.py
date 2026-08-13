import subprocess
import os
import pexpect
import sys


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


def install_fonts_func():
    print(f"[*] START INSTALL FONTS")
    shell_command = "dnf install msttcore-fonts-installer -y"
    subprocess.run(shell_command, shell=True, check=True)
    print(f"[+] INSTALL FONTS SUCCESSFULLY")
    print("===============================")


def drweb_add_repo_func():
    print(f"[*] START DR WEB ADD REPO")
    os.chdir("/etc/yum.repos.d")
    repo_data = """
[drweb] 
name=DrWeb - 11.1
baseurl=https://repo.drweb.com/drweb/linux/11.1/$basearch/
gpgcheck=1
enabled=1
gpgkey=https://repo.drweb.com/drweb/drweb.key
    """

    with open("drweb.repo", "w+") as f:
        f.write(repo_data)
    print(f"[+] DR WEB ADD REPO SUCCESSFULLY")
    print("===============================")


def add_system_account_func():
    print(f"[*] START CHANGE SYSTEM ACCOUNT")
    os.chdir("/var/lib/AccountsService/users")
    data = "[User]\nSession=\nSystemAccount=true\n"

    with open('redadmin', 'w+') as f:
        f.write(data)

    print(f"[+] CHANGE SYSTEM ACCOUNT SUCCESSFULLY")
    print("===============================")


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


def join_to_domain_func():          
    hostname = os.uname().nodename        
    child = pexpect.spawn('join-to-domain', encoding='utf-8', timeout=30)
    child.expect(r'Укажите\s*\(1,\s*2\s*или\s*3\)\s*: ')
    child.sendline('1')    
    child.expect(r'Для\s*подтверждения\s*нажмите\s*ENTER\s*или\s*введите\s*имя\s*домена\s*вручную:\s*')
    child.sendline('')
    child.expect(r'Имя\s*ПК:\s*')
    child.sendline(hostname)
    child.interact()


def reboot_system_func():
    print(f"[+] START REBOOT SYSTEM")
    shell_command = "reboot"
    subprocess.run(shell_command, shell=True, check=True)
    print("===============================")


def main():
    print()
    print("="*50)
    print("***** ВЫБЕРИТЕ ОДИН ИЗ ПУНКТОВ МЕНЮ *****")
    print("="*50)

    print("1) Обновление системы")
    print("2) Изменить права SELinux=permissive")
    print("3) Добавить пользователя redadmin в root группу")
    print("4) Установка шрифтов")
    print("5) Добавить репозиторий Dr.Web")
    print("6) Убрать пользователя redadmin из списка начального экрана")
    print("7) Ввести в домен")
    print("8) Перезагрузить систему")
    print("9) Выполнить все пункты по очереди")    
    print("   |-> Внимание после выбора этого пункта будет произведена автоматическая перезагрузка компьютера")
    print("10) Выход")
    print()

    try:
        item = int(input("Выберите пункт меню: "))

        if item == 1:
            update_system_func()
        elif item == 2:
            selinux_true_func()
        elif item == 3:
            add_to_root_func()
        elif item == 4:
            install_fonts_func()
        elif item == 5:
            drweb_add_repo_func()
        elif item == 6:
            add_system_account_func()
        elif item == 7:
            join_to_domain_func()
        elif item == 8:
            reboot_system_func()
        elif item == 9:
            update_system_func()
            selinux_true_func()
            add_to_root_func()
            install_fonts_func()
            drweb_add_repo_func()
            add_system_account_func()
            update_system_func()
            join_to_domain_func()
            reboot_system_func()
        elif item == 10:
            print("Завершение работы программы ...")
            sys.exit()
        else:
            print("Неправильный выбор ... :-( ")
    except ValueError as err:
        print(f"!!! НЕПРАВИЛЬНЫЙ ФОРМАТ ВВОДА !!! -> {err}")
        print("Завершение работы программы ...")


if __name__ == "__main__":
    main()