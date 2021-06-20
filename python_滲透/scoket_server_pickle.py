from socket import *
from io import BytesIO
# 序列化py對象文件數據
import pickle


def Server_pic(IP, Port):
    #socket套接字
    socket_obj = socket(AF_INET, SOCK_STREAM)
    #綁定套接字地址
    socket.bind((IP, Port))
    #設置監聽數量
    socket_obj.listen(5)
    #初始化變量
    file_no = 1
    while True:
        #接收TCP，並返回conn,addr   conn新套接字，可以發送和接收win電腦
        connection, address = socket_obj.accept()
        print('server_connected by:', address)
        #預定接收訊息變量
        recieved_message = b''
        #讀win電腦記錄下來數據
        recieved_message_fragment = connection.recv(1024)

        while recieved_message_fragment:
            recieved_message += recieved_message_fragment
            recieved_message_fragment = connection.recv(1024)
        try:
            obj = pickle.load(recieved_message)
            print(obj)
        except EOFError:
            file_name = 'recv_image_' + str(file_no) + '.bmp'
            recv_image = open(file_name, 'wb')
            recv_image.write(recieved_message)
            file_no+=1
            recv_image.close()

        connection.close()


if __name__ == "__main__":
    server_IP = '0.0.0.0'
    server_Port = 6666
    Server_pic(server_IP, server_Port)
