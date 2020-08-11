#!/bin/python3

import os
import time

print("************************************")
print("*                                  *")
print("*   Tor Network Service            *")
print("*          v.1                     *")
print("*                                  *")
print("*   Connect Tor Network            *")
print("*       Hide Yourself              *")
print("************************************")

print("\n1-) Open Firefox Using Tor Proxy")
print("2-) TCP Port Scan Using Tor Proxy")
print("3-) UDP Port Scan Using Tor Proxy")


cmd = input("\nOptions: ")

if cmd == "1":
    
    print("\n\033[1;34m[*] \033[0mTor Starting ")
    os.system("service tor start")
    time.sleep(1)
    
    print("\033[1;34m[*] \033[0mTor Started!")
    time.sleep(1)
    
    # Connect proxychain
    print("\033[1;34m[*] \033[0mOpening Firefox\n")
    os.system("proxychains firefox https://google.com/ ")

elif cmd == "2":

    print("\n\033[1;34m[*] \033[0mTor Starting ")
    os.system("service tor start")
    time.sleep(1)
    
    print("\033[1;34m[*] \033[0mTor Started!")
    time.sleep(1)
    
    # Starting Nmap (TCP)
    print("\033[1;34m[*] \033[0mStarting TCP Nmap Scan\n")
    target = input("Enter The domain/ip: ") 
    os.system("proxychains" " nmap " + " -Pn -T4 -sT " + target)

elif cmd == "3":

    print("\n\033[1;34m[*] \033[0mTor Starting ")
    os.system("service tor start")
    time.sleep(1)
    
    print("\033[1;34m[*] \033[0mTor Started!")
    time.sleep(1)
    
    # Starting Nmap (UDP)
    print("\033[1;34m[*] \033[0mStarting TCP Nmap Scan\n")
    target = input("Enter The domain/ip: ") 
    os.system("proxychains" " nmap " + " -Pn -T4 -sU " + target)
