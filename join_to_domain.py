import os
import pexpect


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

