from update_system import update_system_func
from selinux_perm import selinux_true_func
from add_to_root import add_to_root_func
from install_fonts import install_fonts_func
from reboot import reboot_system_func
from install_printer import install_printer_func
from drweb_add_repo import drweb_add_repo_func
from add_system_account import add_system_account_func
from join_to_domain import join_to_domain_func
# from colorama import init, Fore, Back, Style

update_system_func()
selinux_true_func()
add_to_root_func()
install_fonts_func()
drweb_add_repo_func()
add_system_account_func()
update_system_func()
# install_printer_func()
join_to_domain_func()
reboot_system_func()
