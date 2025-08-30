from multiprocessing import Pool, Process, Pipe
import time, os

'''
使用 Pipe 实现多进程之间的通信
'''


def add_data(send_pipe):
    for i in range(5):
        time.sleep(0.5)
        send_pipe.send("产品"+str(i))
        print("产品"+str(i)+"生产完成")
    send_pipe.close()  # 发送完数据后关闭管道


def read_data(receive_pipe):
    count = 0
    while True:
        try:
            product = receive_pipe.recv()
            print(f"消费者{os.getpid()}消费了{product}")
            time.sleep(0.5)
            count += 1
            if count >= 5:  # 生产了5个产品后停止消费
                break
        except EOFError:
            # 管道已关闭
            break
    receive_pipe.close()


if __name__ == '__main__':
    print("开始执行多任务")
    start_time = time.time()

    # 创建一个管道对象
    send_pipe, receive_pipe = Pipe()

    # 直接创建进程而不是使用进程池
    producer = Process(target=add_data, args=(send_pipe,))
    consumer = Process(target=read_data, args=(receive_pipe,))

    # 启动进程
    producer.start()
    consumer.start()

    # 等待所有进程完成
    producer.join()
    consumer.join()

    print(f"总共耗时{time.time()-start_time}秒")