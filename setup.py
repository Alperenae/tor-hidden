#!/bin/python3
import os

# COLORS
S = '\033[1;32m[+] \033[0m'
W = '\033[1;33m[!] \033[0m'
ENDC = '\033[0m'

print("\n" + W + "\033[1;35;1mRequired Applications Downloading\n" + ENDC)
 
os.system("apt-get -y install proxychains")
os.system("apt-get -y install tor")
os.system("apt-get -y install nmap")
os.system("rm -rf /etc/proxychains.conf")
os.system("mv proxy.conf /etc/proxychains.conf")

print("\n" + S + "Downloading Done...\n")
