import os
from colorama import init, Fore
from time import sleep
import csv
import time
import random
import os
import pickle
import sys
scam = '@notoscam'
init()

n = Fore.RESET
lg = Fore.BLUE
r = Fore.RED
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
gr = Fore.GREEN
colors = [lg, r, w, cy, ye, gr]

try:
    import requests
except ImportError:
    print(f'{lg}[i] Installing module - requests...{n}')
    os.system('pip install requests')

def banner():
    import random
    # fancy logo
    b = [
    

   '𝗖𝗛- @𝗞𝗨𝗥𝗗 𝗕𝗢𝗧𝗦  ','𝗕𝗬 - @𝗛𝗔𝗠𝗔_𝗠𝗔𝗤𝗦𝗢𝗢𝗗 ༈༉',

    ]
    for char in b:
        print(f'{random.choice(colors)}{char}{n}')
    print(f'{r}   {r}')
    print(f'{r} Channel: @Kurd_Bots{r}')
    print(f'{cy} Group : @Kurd_botschat{cy}')
    print(f'{r}   {r}')

def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
while True:
    clr()
    banner()
    print(ye+'Datawit kama install bkait:'+n)
    print(cy+'            [1] Setup Script'+n)
    print(cy+'            [2] Daxstn'+n)
    a = int(input('\n zhmaraiak bnwsa: '))
    if a == 1:
    
       print("[+] Installing requierments ...")
       os.system('pip install telethon==1.24.0')
       os.system('pip install colorama==0.4.3')

       print("[+] setup complete !")
       print("[+] Esta atwani tulakan run bkaitl !")
       input(f'\n esta entar dabgra bo daxstn...')
       
    if a == 2:
        clr()
        banner()
        exit()