from multiprocessing import Pool
from multiprocessing.dummy import Process
import time
'''
多进程之间无法进行通信！！！
'''

my_list = []
def add_data(name):
    for i in range(5):
        my_list.append(i)
        print(f"{name}添加了{i}到列表中")
        time.sleep(0.5)



def read_data():
    print(my_list)



if __name__ == '__main__':
    print("开始执行多任务")
    start_time = time.time()
    process_pool = Pool(2) # 创建一个进程池，最大进程数为2

    process_pool.apply(add_data, args=('张吉',)) # 向进程池中添加新的进程执行任务  此时依然是同步执行
    process_pool.apply(read_data) # 向进程池中添加任务

    process_pool.close() # 关闭进程池，表示不再接受新的任务
    process_pool.join() # 一般都要加上 主进程阻塞，等待所有子进程执行完所有任务  等待所有子进程执行完毕后再继续往下执行


    print(f"总共耗时{time.time()-start_time}秒")