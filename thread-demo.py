#!/usr/bin/python3

# thread 多线程demo

import threading #导入线程模块
import time

exit_flag = 0
class myThread (threading.Thread):
    # counter 延时秒数
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self) # 调用父类的构造方法
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):  # 重写run() 线程活动的方法
        print("开始线程：" + self.name)
        # 获取锁 用于线程同步
        threadLock.acquire()

        printTime(self.name, self.counter, 5)

        # 释放锁 开启下一个线程
        threadLock.release()
        print("退出线程：" + self.name)


# myThread 类结束

def printTime(threadName, delay, counter):
    while counter:
        if exit_flag:
            threadName.exit()   # 退出线程
        time.sleep(delay)   # 睡眠一会 方便查看效果
        print("%s: %s" % (threadName, time.ctime()))
        counter -= 1

threadLock = threading.Lock()  # 线程锁 用于线程同步 线程同步后 要么都是1 不会1 2 交叉出现
threads = []

# 创建线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

# 添加到线程列表里
threads.append(thread1)
threads.append(thread2)


# 启动线程
thread1.start()
thread2.start()

# 等待线程终止
thread1.join()
thread2.join()

print("退出主线程")

