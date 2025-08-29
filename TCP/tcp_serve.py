from socket import socket as Socket, AF_INET, SOCK_STREAM

# tcp 服务端 AF_INET:ipv4

# 负责接收客户端的连接请求 
server_socket = Socket(AF_INET, SOCK_STREAM)

server_socket.bind(('', 8000)) # 本地+外网主机都可以访问 3. TCP 服务端程序必须绑定端口号，否则客户端找不到这个 TCP 服务端程序。

server_socket.listen(5)    # 开始监听该端口上的连接请求 服务器 允许最大等待建立的连接数 当 TCP 客户端程序想要和 TCP 服务端程序进行通信的时候必须要先建立连接

# 接受客户端的连接请求 阻塞等待客户端连接，成功后返回一个新 socket（通信 socket） 和客户端地址IP 和端口
socket2, client_addr = server_socket.accept()      # # 如果没有客户端连接，这行代码会一直“卡住” 这就是所谓的阻塞block
print("有客户端连接了！")  # 这句话要等客户端连上才会打印
while True:
    # 接收客户端数据 TCP 用 recv 方法
    msg = socket2.recv(1024).decode('utf-8')
    if msg == 'exit' or msg == 'quit': 
        break

    print(f'来自客户端IP:{client_addr[0]} 端口:{client_addr[1]} 的数据:{msg}')

    # 给客户端发送聊天信息
    send_msg = input("服务器：")
    if send_msg == 'exit' or send_msg == 'quit':
        socket2.send(send_msg.encode('utf-8'))
        break
    socket2.send(send_msg.encode('utf-8'))
    
socket2.close() # 关闭 通信socket
server_socket.close() # 关闭 连接socket