import pexpect
import re


def install_printer_func():
            
    child = pexpect.spawn('bash linux-brprinter-installer-2.2.4-1', encoding='utf-8', echo=False)
    # child.logfile = sys.stdout
    child.expect('Input model name ->')
    child.sendline('MFC-L6900')

    child.expect('OK\\? \\[y/N\\] ->')
    child.sendline('y')

    child.expect('Do you agree\\? \\[Y/n\\] ->')
    child.sendline('y')

    child.expect('Will you specify the Device URI\\? \\[Y/n\\] ->')
    child.sendline('y')

    child.expect('Specify IP address.')

    output = child.before
    match = re.search(r'(\d+)\s*\(I\):', output)
    if match:
        option_number = match.group(1)
        child.sendline(option_number)
    else:
        child.sendline('I')

    child.expect('select the number of destination Device URI. ->')
    child.sendline(option_number)

    child.expect('enter IP address ->')
    child.sendline('192.168.24.33')

    child.expect('Test Print\\? \\[y/N\\] ->')
    child.sendline('n')

    child.expect('Do you agree\\? \\[Y/n\\] ->')
    child.sendline('y')

    child.expect('Do you agree\\? \\[Y/n\\] ->')
    child.sendline('y')
