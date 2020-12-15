from os import system, name  
from time import sleep
from datetime import datetime 
import platform
import subprocess
import socket, threading

def rundown(status,process,website):
	if status=="start":
		if process=="-w":
			print("Target IP:",socket.gethostbyname(website))
			print("PING REQUEST\n")
			print(ping(website))
			print(process)
			print(website)
		else:
			print("Invalid "+process+" Rundown Identifier.")

def ping(host):
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    return subprocess.call(command) == 0
    

def TCP_connect(ip, port_number, delay, output):
    TCPsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    TCPsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    TCPsock.settimeout(delay)
    try:
        TCPsock.connect((ip, port_number))
        output[port_number] = 'Listening'
    except:
        output[port_number] = ''
def scan_ports(host_ip, delay):

    threads = []        
    output = {}         
    for i in range(10000):
        t = threading.Thread(target=TCP_connect, args=(host_ip, i, delay, output))
        threads.append(t)

    for i in range(10000):
        threads[i].start()
    for i in range(10000):
        threads[i].join()
    for i in range(10000):
        if output[i] == 'Listening':
            print(str(i) + ': ' + output[i])
            
def findport(target,idelay):
    target = socket.gethostbyname(target)  	
    print("-" * 50)
    print("Scanning Target: " + target)
    print("-" * 50)	
    host_ip = target
    delay = int(idelay)   
    scan_ports(host_ip, delay)   
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'              
                
def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
         
def banner():
	print(bcolors.OKCYAN+bcolors.BOLD+"  ____             _ _  ____ _                 _")
	print(" |  _ \\  _____   _(_) |/ ___| | ___  _   _  __| |")
	print(" | | | |/ _ \\ \\ / / | | |   | |/ _ \\| | | |/ _` |")
	print(" | |_| |  __/\\ V /| | | |___| | (_) | |_| | (_| |")
	print(" |____/ \\___| \\_/ |_|_|\\____|_|\\___/ \\__,_|\\__,_|"+bcolors.ENDC)
	print("\n ================================================\n") 

banner()
func_dict = {'banner':banner,'clear':clear,'ping':ping,'rundown':rundown,'findport':findport}
while True:
	try:
		command = input("\n>>>").split()
		func_dict[command[0]](*command[1:])
	except:
		print(bcolors.WARNING+"Something has wrong"+bcolors.ENDC)