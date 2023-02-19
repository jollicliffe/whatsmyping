from ping3 import ping, verbose_ping
import os
from time import sleep

trend=[]

def check(ping):
    if (ping < 50):
        trend.append("-")
        return "Good"
    elif (ping > 50 and ping < 99):
        trend.append("_")
        return "Playable"
    elif (ping > 100):
        trend.append("|")
        return "Poor"

while True:
    os.system("cls")
    print("Waiting")
    latency = round(ping("google.co.uk")*1000)
    
    os.system("cls")
    print("""


██████╗░██╗███╗░░██╗░██████╗░███████╗██████╗░
██╔══██╗██║████╗░██║██╔════╝░██╔════╝██╔══██╗
██████╔╝██║██╔██╗██║██║░░██╗░█████╗░░██████╔╝
██╔═══╝░██║██║╚████║██║░░╚██╗██╔══╝░░██╔══██╗
██║░░░░░██║██║░╚███║╚██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░╚══════╝╚═╝░░╚═╝


""")
    print("WHATS MY PING! / google.co.uk")
    print("------------ Ping: " + str(latency) + " | state: " + check(latency) + " ------------")
    sep = ""
    print("\nOverall Stats: " + sep.join(trend))
    sleep(2)
    
    
