from multiprocessing import Pool
from multiprocessing.dummy import Process
import time




# 吃饭任务
def eat(name_user1, name_user2):
    for i in range(5):
        print(f"{name_user1}和{name_user2}一起吃了{i+1}碗饭")
        time.sleep(0.5)


# 打游戏任务
def play_game():
    for i in range(5):
        print("打打打打游戏喽")
        time.sleep(0.5)

if __name__ == '__main__':
    print("开始执行多任务")
    start_time = time.time()
    process_pool = Pool(2) # 创建一个进程池，最大进程数为2

    # apply是同步阻塞的函数 
    # process_pool.apply(eat, args=('张吉','琴女')) # 向进程池中添加新的进程执行任务  此时依然是同步执行
    # process_pool.apply(play_game) # 进程池中添加新的进程执行任务

    # apply_async是异步非阻塞的
    process_pool.apply_async(eat, args=('张吉','琴女')) # 向进程池中添加新的进程执行任务  此时依然是同步执行
    process_pool.apply_async(play_game) # 向进程池中添加任务

    process_pool.close() # 关闭进程池，表示不再接受新的任务
    process_pool.join() # 一般都要加上 主进程阻塞，等待所有子进程执行完所有任务  等待所有子进程执行完毕后再继续往下执行
    print(f"总共耗时{time.time()-start_time}秒")