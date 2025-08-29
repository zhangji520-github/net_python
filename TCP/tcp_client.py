from socket import socket as Socket, AF_INET, SOCK_STREAM

# tcp 服务端 AF_INET:ipv4

server_addr = ('192.168.217.231', 8000)
# client客户端直接负责连接
client_socket = Socket(AF_INET, SOCK_STREAM)

# ''代表本地的所有地址 这里填写服务器的ip 连接上我们的服务端
client_socket.connect(('192.168.217.231', 8000))

while True:
    # 发送数据
    data = input('客户端>>>')
    if data == 'exit'or data == 'quit':
        client_socket.send(data.encode('utf-8'))
        break
        

    client_socket.send(data.encode('utf-8'))

    msg = client_socket.recv(1024).decode('utf-8')

    if msg == 'exit' or msg == 'quit':
        break
    print(f'来自服务段IP:{server_addr[0]} 端口:{server_addr[1]} 的数据:{msg}')

client_socket.close()