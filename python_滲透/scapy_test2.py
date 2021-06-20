from scapy.all import *
pkt=IP(src='192.168.0.15',dst='192.168.0.17')/ICMP()
send(pkt)#發送  mac地址sendp

ans,uans=sr(pkt)
ans.summary()

