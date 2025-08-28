from socket import socket as Socket, AF_INET, SOCK_DGRAM
# 实现 客户端和服务端的即使聊天

# 创建一个UDP的socket
server_socket = Socket(AF_INET, SOCK_DGRAM)

# 绑定地址 服务器注意如果是 IP:127.0.0.1的话，只能客户端本机访问 
# 如果希望局域网外部的电脑与当前服务端通信，绑定 IPV4 地址
# IP:'',表示服务器绑定到所有的IP地址 允许所有IP地址访问
server_socket.bind(('', 6666))
# server_socket.bind(("192.168.217.231", 6666))       # 一般6000以上的端口号不会被占用

# 循环接收数据
while True:
    # 接收客户端的数据 1kb  recvfrom是阻塞方法，直到接收到数据或者超时才会返回
    print("开始阻塞")
    msg, addr = server_socket.recvfrom(1024) # msg:接收到的数据 addr:发送方的地址 源地址的IP和端口号
    if msg.decode('utf-8') == 'exit' or msg.decode('utf-8') == 'quit':
        break

    print(f"收到来自IP:{addr[0]},端口号{addr[1]}的消息:{msg.decode('utf-8')}")

    # 回复消息到客户端
    send_msg = input("服务端发送:")
    # 注意发送到智能是字节数据，所以需要对字符串进行编码
    if send_msg == 'exit' or send_msg == 'quit':
        server_socket.sendto(send_msg.encode('utf-8'), addr) # 发送数据到指定的地址
        break
    server_socket.sendto(send_msg.encode('utf-8'), addr) # 发送数据到指定的地址
    
# 关闭套接字
server_socket.close()