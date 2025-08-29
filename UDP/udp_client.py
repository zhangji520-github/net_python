from socket import socket as Socket, AF_INET, SOCK_DGRAM
# 实现 客户端和服务端的即使聊天

# 创建一个UDP的socket 
client_socket = Socket(AF_INET, SOCK_DGRAM)

# 客户端的socket不需要bind 所以有操作系统分配一个随机的端口号


while True:
    # 输入要发送的消息 给服务端
    message = input('客户端:请输入要发送的消息:')
    if message == 'exit' or message == 'quit':
        client_socket.sendto(message.encode('utf-8'), ("192.168.217.231", 6666))  # 把退出指令发给服务器 让服务器也知道关闭的时间
        break

    # 发送消息 sendto(data, address) 必须指定目标地址和端口号
    client_socket.sendto(message.encode('utf-8'), ("192.168.217.231", 6666))
    # 接收消息
    msg, address = client_socket.recvfrom(1024)
    if msg.decode('utf-8') == 'exit' or msg.decode('utf-8') == 'quit':
        break
    print(f"收到来自服务端IP:{address[0]},随机端口号{address[1]}的消息:{msg.decode('utf-8')}")

# 关闭套接字
client_socket.close()
