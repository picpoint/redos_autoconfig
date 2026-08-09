import os
import subprocess
import pexpect


def install_printer_func():
    answers = [
        'MFC-L6900\n',
        'y\n',
        'y\n',
        '73\n',
        '192.168.24.33\n',
        'n\n'
    ]
    os.chdir('brother')
    print(os.listdir())
    root_to_file_cmd = "chmod 777 linux-brprinter-installer-2.2.4-1"
    subprocess.run(root_to_file_cmd, shell=True, check=True)
    # run_install_cmd = "./linux-brprinter-installer-2.2.4-1"
    # subprocess.run(run_install_cmd, shell=True, check=True)
    process = subprocess.Popen(
        ['./linux-brprinter-installer-2.2.4-1'],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    output, err = process.communicate(''.join(answers))
    print(output)

    # child = pexpect.spawn('cd brother/')
    # child = pexpect.spawn('./linux-brprinter-installer-2.2.4-1')
    # child.expect("Input model name ->.*:")
    # child.sendline("MFC-L6900")


