#!/usr/bin/python
'coded by l314ck_h4ck3l2'

import os
import sys
import re
from socket import socket , gethostbyname , gethostbyaddr , AF_INET , SOCK_STREAM


blue   = '\033[34m'
green  = '\033[32m'
red    = '\033[31m'
yellow = '\033[33m'
error  = '\033[91m'
cyan   = '\033[36m'
bold   = "\033[;1m"
reset  = "\033[0;0m"

ip_regex = '^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

def banner():
    print(f"""{blue}
 
     ____             __  _____                                 
    / __ \____  _____/ /_/ ___/_________ _____  ____  ___  _____
   / /_/ / __ \/ ___/ __/\__ \/ ___/ __ `/ __ \/ __ \/ _ \/ ___/
  / ____/ /_/ / /  / /_ ___/ / /__/ /_/ / / / / / / /  __/ /    
 /_/    \____/_/   \__//____/\___/\__,_/_/ /_/_/ /_/\___/_/     
 
 
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~{cyan}
 ~                   Author : l314ck_h4ck3l2                   ~
 ~          github : https://github.com/l314ck-h4ck3l2         ~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

{reset}""")

def port_scanner(range_of_port:list , ip:str):
    if int(range_of_port[0]) < int(range_of_port[1]):
        for port in range(int(range_of_port[0]) , int(range_of_port[1])):
            s = socket(AF_INET , SOCK_STREAM)
            res = s.connect_ex((ip , port))
            if res == 0:
                print(f'{green} [+] Port {port} is open !{reset}')
            else:
                print(f'{red} [+] Port {port} is close !{reset}')
    else:
        print(f'{red} [-] Port Range is Incorrect !{reset}')

def usage():
    print(f'{error} Usage   : python DDos.py [host or ip] [port range]{reset}')
    print(f'{error} Example : python DDos.py 31.13.72.174 80-85{reset}')
    print(f'{error} Example : python DDos.py instagram.com 80-85{reset}')
    print(f'{error} Example : python DDos.py https://www.instagram.com 80-85{reset}')
    sys.exit()

def main():
    os.system('cls' or 'clear')
    banner()
    if len(sys.argv) == 3:
        if (re.search(ip_regex, sys.argv[1])):
            addr = sys.argv[1]
            name = gethostbyaddr(addr)
        elif sys.argv[1].startswith('http://www.'):
            name = sys.argv[1][11:]
            addr = gethostbyname(name)
        elif sys.argv[1].startswith('https://www.'):
            name = sys.argv[1][12:]
            addr = gethostbyname(name)
        else:
            try:
                name = sys.argv[1]
                addr = gethostbyname(name)
            except:
                print(f'{red} [!] Host or Ip is Not True !{reset}')
                sys.exit()
        try:
            range_of_port = sys.argv[2].split('-', 2)
            print(f'{yellow} name : {name}{reset}')
            print(f'{yellow} addr : {addr}{reset}')
            print(f'{yellow} port range : {sys.argv[2]}{reset}')
            print()
            port_scanner(range_of_port, addr)
            print()
        except:
            print(f'{red} [!] Port Range is not True !{reset}')
            sys.exit()
    else:
        usage()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print(f'{red} [-] ^C received . shutting down server !{reset}')
        sys.exit()
