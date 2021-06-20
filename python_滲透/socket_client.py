import pickle
from io import BytesIO
from socket import *

def Clinet_PIC(ip,port,obj):
    try:
        msg=pickle.dumps(obj)
        send_message=BytesIO(msg)
        send_message_fragment=send_message.read(1024)
    except TypeError:
        send_message=obj
        send_message_fragment=send_message.read(1024)

    socket_obj=socket(AF_INET,SOCK_STREAM)
    socket_obj.connect((ip,port))

    while send_message_fragment:
        socket_obj.send(send_message_fragment)
        send_message_fragment=send_message.read(1024)
    socket_obj.close()

if __name__ =='__main__'
    dict_={'key1':'welcome to test','key1':[1,2,3,4,5]}
    Clinet_PIC('192.168.0.19',6666,dict_)