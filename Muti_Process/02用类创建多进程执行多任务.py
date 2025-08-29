from multiprocessing import Process
import time


class EatProcess(Process):
    """吃饭任务进程类"""

    def __init__(self, name, name_user, **kwargs):
        super().__init__()
        self.name = name
        self.name_user = name_user

    def run(self) -> None:
        for i in range(5):
            print(f"进程{self.name}正在执行。{self.name_user}吃了{i + 1}碗饭")
            time.sleep(0.5)

class PlayGamrProcess(Process) :
    """打游戏任务进程类"""
    def __init__(self, name, **kwargs):
        super().__init__()
        self.name = name
    def run(self) -> None:
        for i in range(5):
            print(f"进程{self.name}正在执行。打打打打游戏喽")
            time.sleep(0.5)


if __name__ == '__main__':
    # 创建一个子进程，每个任务由由一个独立的子进程执行

    p1 = EatProcess(name="吃饭", name_user="小明")
    p2 = PlayGamrProcess(name="游戏")

    # 启动子进程
    p1.start()
    p2.start()