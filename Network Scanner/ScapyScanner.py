import logging

from scapy.layers.inet import TCP
from scapy.layers.inet import IP
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *

if len(sys.arg) != 4:
    print("Usage : %s target startpoint endport" % (sys.argv[0]))
    sys.exit(0)

target = str(sys.argv[1])
startport = int(sys.argv[2])
endport = int(sys.argv[3])
print("Scanning " + target + " for open TCP ports\n")

if startport == endport:
    endport += 1

for x in range(startport, endport):
    packet = IP(dst=target) / TCP(dport=x, flags='5')
    response = sr1(packet, timeout=0.5, verbose=0)
    if response.haslayer(IP) and response.getlayer(TCP).flag == 0x12:
        print("Port" + str(x) + "is open!")
    sr(IP(dst=target) / TCP(dport=response.sport, flag='R'), timeout=0.5, verbose=0)

print("Scan complete\n")

