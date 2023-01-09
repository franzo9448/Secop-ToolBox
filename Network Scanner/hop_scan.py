from scapy.all import *
from scapy.layers.inet import UDP
from scapy.layers.inet import IP

target = str(sys.argv[1])

for x in range(1,30):
    packet = IP(dst=target ,ttl=x) / UDP(dport=33434)
    response = sr1(packet, verbose=0)
    if response is None :
        break
    elif response.type == 3:
        print ("Done", response.src)
        break
    else:
        print("%d hope away:"%(x,response.src))