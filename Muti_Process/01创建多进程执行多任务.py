from multiprocessing.dummy import Process
import time


# 吃饭任务
def eat(name_user):
    for i in range(5):
        print(f"{name_user}吃了{i+1}碗饭")
        time.sleep(0.5)


# 打游戏任务
def play_game():
    for i in range(5):
        print("打打打打游戏喽")
        time.sleep(0.5)


if __name__ == '__main__':
    print("开始执行多任务")
    # 实际上有三个进程运行 主进程+两个子进程
    # 创建一个子进程，每个任务由由一个独立的子进程执行
    p1 = Process(target=eat,name="进程1",kwargs={"name_user":"小明"})
    p2 = Process(target=play_game,name="进程2")

    # 启动子进程
    p1.start()
    p2.start()

    # 主进程自动等待，所有的子进程去执行各自的任务。一直到所有的子进程都结束，主进程才结束