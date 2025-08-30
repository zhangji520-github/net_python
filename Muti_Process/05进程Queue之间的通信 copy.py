from multiprocessing import Pool,Queue
from multiprocessing.dummy import Process
import time,os
'''
多进程之间无法进行通信！！！
'''


def add_data(q:Queue):
    for i in range(5):
        time.sleep(0.5)
        q.put('产品'+str(i)) # put 进行存
        print("产品"+str(i)+"生产完成")



def read_data(q:Queue):
    count = 0
    while True:
        item = q.get() # 从队列中获取数据  队列为空时会阻塞等待 
        print(f"消费者{os.getpid()}消费了{item}")
        time.sleep(0.5)
        count += 1
        if count >= 5:  # 生产了5个产品后停止消费
            break


if __name__ == '__main__':
    print("开始执行多任务")
    start_time = time.time()

    q = Queue(100) # 创建一个队列对象
    p1 = Process(target=add_data, args=(q,)) # 往队列queue中添加数据
    p2 = Process(target=read_data, args=(q,)) # 从队列queue中读取数据

    p1.start()
    p2.start()
    
    p1.join()  # 等待p1执行完毕
    p2.join()  # 等待p2执行完毕

    print(f"总共耗时{time.time()-start_time}秒")