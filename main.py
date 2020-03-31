#imports all the modules that we will need
import math
from subprocess import call
import sys
from sys import platform
import asyncio
import requests
import asyncio
from termcolor import colored
from colorama import init
import re

sviews = 0

#Makes this work for windows
init()

#Sets console title
sys.stdout.write("\x1b]2;NameMC ViewBot by Aldas\x07")

#clears terminal by using command in the shell
def clear():
    if platform not in ('win32', 'cygwin'):
        command = 'clear'
    else:
        command = 'cls'
    try:
        call(command, shell=True)
    except OSError as e:
        pass

#function to view profiles
async def view(username, number=None, proxies=None, headers=None, timeout=None):
    if number == None:
        r = requests.get(f"https://namemc.com/profile/{username}", headers=headers, proxies={"http": proxy,"https": proxyif }, timeout=timeout)
        return r.status_code
    else:
        r = requests.get(f"https://namemc.com/profile/{username}.{number}", headers=headers, proxies=proxies, timeout=timeout)
        return r.status_code

#prints the banner
print(colored('''
_  _                __  __     __   ___              ___      _   
| \| |__ _ _ __  ___|  \/  |__  \ \ / (_)_____ __ __ | _ ) ___| |_ 
| .` / _` | '  \/ -_) |\/| / _|  \ V /| / -_) V  V / | _ \/ _ \  _|
|_|\_\__,_|_|_|_\___|_|  |_\__|   \_/ |_\___|\_/\_/  |___/\___/\__|
                        By Aldas | Version 1.0
''', "magenta"))

#makes an loop
name_input = True
while name_input:
    #tries to execute this username input code
    try:
        #username input
        username = input(f"[{colored('*', 'red')}] Username: ")
        #if user presses enter
        if username == "":
            continue
        #if user enters anything else
        else:
            pass

        #prints text to let users know that its not really needed
        print(colored("Press enter for 1 (default) as user number", "magenta"))
        #user number input
        usernumber = input(f"[{colored('+', 'green')}] User number incase needed: ")
        #if user presses enter (skips)
        if usernumber == "":
            usernameid = None
            name_input = False
        #if user enters anything else
        else:
            name_input = False

    # if you press ctrl + c
    except KeyboardInterrupt:
        print(colored("Bye!", "green"))
        exit()

    # if any other error occurs
    except Exception as e:
        print(f"{e}\n{colored('Error has occured! ^')}")

runnin = True
while runnin:
    try:
        #defines proxy
        with open("proxies.txt") as f:
            for i in f.readlines():
                proxy = i.rstrip()
                proxies = {
                    "http": proxy,
                }
                print(proxy)
                headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                           "Accept-Encoding": "gzip, deflate, br",
                           "Accept-Language": "en-US,en;q=0.5",
                           "Cache-Control": "max-age=0",
                           "Connection": "keep-alive",
                           "DNT": 1,
                           "Host": "namemc.com",
                           "Referer": f"https://namemc.com/search?q={username}",
                           "TE": "Trailers",
                           "Upgrade-Insecure-Requests": 1,
                           "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:73.0) Gecko/20100101 Firefox/73.0",
                           }
                #sends a reuqest
                req = asyncio.run(view(username=username, number=usernumber, proxies=proxy, headers={'User-Agent': ua.random}, timeout=10))
                #if we get 200 as a status code (success)
                if req == 200:
                    sviews += 1
                    print(colored(f"[{sviews} views sent]", "magenta") + " " + colored('Successfully sent a view', 'green'))
                #if 404 error occurs (page not found error)
                elif req == 404:
                    print(colored("No such a profile", "red"))
                    exit()
                #if request status code is something else
                else:
                    print(colored(f"Sent a request and got status code of {req}", "magenta"))
                    continue

    # if you press ctrl + c
    except KeyboardInterrupt:
        print(colored("Bye!", "green"))
        exit()

    # if any other error occurs
    except Exception as e:
        print(f"{e}\n{colored('Error has occured! ^')}")
