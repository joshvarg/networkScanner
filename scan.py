from tokenize import String
import netifaces as nf
import scapy.all as scapy
import socket as s

def subnet2CIDR(subnet, cidr):
  classSplit = subnet.split('.')
  for i in classSplit:
    class2Binary = format(int(i), 'b')
    cidr += class2Binary.count('1')

  cidr = str(cidr)
  return cidr

hostaddr = s.gethostbyname(s.gethostname())
if(hostaddr == '127.0.0.1'):
  x = s.socket(s.AF_INET, s.SOCK_DGRAM)
  x.connect(("8.8.8.8", 80))
  hostaddr = x.getsockname()[0]
  x.close()

wifiaddrs = nf.ifaddresses('en0')
netmask = wifiaddrs[nf.AF_INET][0]['netmask']
print(netmask, hostaddr)
cidr = 0

hostaddr = hostaddr + '/' + subnet2CIDR(netmask, cidr)
print(hostaddr)

arp = scapy.ARP(pdst=hostaddr)
arp.show()