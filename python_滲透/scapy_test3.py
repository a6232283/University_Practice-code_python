from scapy.all import *
# sniff(filter='icmp',prn=lambda x:x.summary())

def packet(pkt):
    print(pkt.summary)

sniff(prn=packet,count=10)