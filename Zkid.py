import os

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
#Table of light colors
DL = "\033[1;90m"
RL = "\033[1;91m"
GL = "\033[1;92m"
YL = "\033[1;93m"
BL = "\033[1;94m"
VL = "\033[1;95m"
CL = "\033[1;96m"
WL = "\033[1;97m"
RE = "\033[0m"   # REMOVE
# 1;30m, 1/0 = bold, 30-37 color, 90-97 light color.


print(f"""
{W}
{W}   ▟███████▙{RE}{C}  █▟█  ▟█  ▟█  ▟██████▙
{W}   ▝▝▝▟██▛▘▘{RE}{C}  ██▛▟█▛▘  ██  ██▝▝▝▟█▙
{B}     ▟██▛   {RE}{C}  █████▙   ██  ██   ▟█▛
{B}    ▟██▛    {RE}{C}  ██▛▝██▙  ██  ██   ▟█▛
{R}   ▟███████▙{RE}{C}  ██   ██  ██  ▟██████▛
{R}   ▝▝▝▝▝▝▝▝▘{RE}{C}  ▝▘   ▝▘  ▝▘  ▝▝▝▝▝▝▝
{RE}          {C}TELEGRAM{RE}: {V}cgrokpp{RE}
""")
print(f"""
{R}   [1] DDoS сайта         [2] Пробив никнейма

   [3] Подбор пароля      [4] Взлом роутера

   [0] Выход{RE}
""")
while True:
    select = input(f"{V}Zkid>> {RE}")
    if select == "0":
        exit()
