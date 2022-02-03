import netifaces as nf
import scapy.all as scapy
import socket as s

hostaddr = s.gethostbyname(s.gethostname())
if(hostaddr == '127.0.0.1'):
  x = s.socket(s.AF_INET, s.SOCK_DGRAM)
  x.connect(("8.8.8.8", 80))
  hostaddr = x.getsockname()[0]
  x.close()

wifiaddrs = nf.ifaddresses('en0')
netmask = wifiaddrs[nf.AF_INET][0]['netmask']
print(netmask, hostaddr)