import os
# from colorama import init, Fore, Back, Style

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