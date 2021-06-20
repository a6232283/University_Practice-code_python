from scapy.all import *
pkt=Ether()/IP()/TCP()
ls(pkt)

#16進制
print(raw(pkt))
print(hexdump(pkt))

#不超過一行摘要
print(pkt.summary())

#數據包詳細情形
print(pkt.show())

#保存數據包
wrpcap('test.cap',pkt)

#讀
pkts=rdpcap('test.cap')
pkts.show()