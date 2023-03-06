"""

"""
import time, threading


def printThread():
    print(threading.current_thread().name, "-执行")

# 创建线程
def test_create_thread():
    n = 0
    while n < 5:
        n += 1
        # 这里传入的是printThread, 不能是printTread() , 否则会变成主线程执行
        t = threading.Thread(target=printThread, name=f"thread-{n}")
        t.start()
        t.join()


# 测试并发问题
class BankCard:
    def __init__(self, balance):
        self.balance = balance

    def add(self, balance):
        self.balance += balance


def add_balance(bc, balance, count):
    for i in range(count):
        bc.add(balance)


def test_multi_thread_error():
    bc = BankCard(0)
    ops_balance = 10
    count = 1000000
    thread_count = 2
    threads = []

    for i in range(thread_count):
        t1 = threading.Thread(target=add_balance, args=(bc, ops_balance, count))
        t1.start()
        threads.append(t1)

    for t in threads:
        t.join()

    print(bc.balance)
    # 可能不一致
    assert bc.balance == ops_balance * count * thread_count

# thread_local
local_thread_context=threading.local()

def print_thread_local():
    print(local_thread_context.name)

def set_thread_local():
    local_thread_context.name = threading.current_thread().name
    print_thread_local()

def test_thread_local():
    t1 = threading.Thread(name="Thread-1", target=set_thread_local)
    t2 = threading.Thread(name="Thread-2", target=set_thread_local)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    # test_thread_local()

    pass
