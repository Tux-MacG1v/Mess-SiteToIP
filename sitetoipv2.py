#!/usr/bin/env python3
import os, requests, sys, time
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor
from socket import gethostbyname

init()
r = Fore.RED + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
oo = Fore.YELLOW + Style.BRIGHT
o = Fore.RESET + Style.RESET_ALL

banner = """
{} ____ ___ _____ _____           _____ ___            ___ ____  
{}/ ___|_ _|_   _| ____|         |_   _/ _ \          |_ _|  _ \ 
{}\___ \| |  | | |  _|    _____    | || | | |  _____   | || |_) |
{} ___) | |  | | | |___  |_____|   | || |_| | |_____|  | ||  __/ 
{}|____/___| |_| |_____|           |_| \___/          |___|_|v2 
                                                               

                     {}CODED BY TUX-MACG1V
              TG:https://t.me/I_am_a_silent_killer
        {}Note : Domaine List Shoud Be Without http:// & /

            """.format(g, r, oo, c, r, g, r, o)


def sitetoip(i):
    try:
        ip = gethostbyname(i)
        print('{}[+] '"{}{} ""{} == ""{}[{}]".format(g, oo, i, o, g, ip))
        open('ips.txt', 'a').write(ip + '\n')
    except:
        print('{}[-] '"{}{}""{} == ""{}[ ERROR ]".format(r, oo, i, o, r))

def Main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner)

    lists = input('\n{}[+] {}Website List{} > {}'.format(o, g, o, g))
    thread = input('{}[+] {}Thread{} > {}'.format(o, g, o, r))
    print('')
    try:
        domain = lists.replace('"','')
        process = open(domain, 'r').read().splitlines()
        with ThreadPoolExecutor(max_workers=int(thread)) as e:
            [e.submit(sitetoip, i) for i in process]
    except:
          print('{}[!] {}Incorrect'.format(o, r))
        
if __name__ == '__main__':
    Main()
