"""
multiprocessing 多进程
"""
# 进程池
from multiprocessing import Pool,Queue, Process
import os, time, random, subprocess


def execute_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# 测试通过进程池执行任务
def test_pool():
    _pool = Pool(4)

    print('start...')
    for i in range(4):
        _pool.apply_async(execute_task, args=(i,))
    print('executing')
    _pool.close()
    _pool.join()

    print('all task completed')

# 测试控制子进程的输入和输出
def test_subprocess():
    print('$ nslookup www.python.org')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)

def test_subprocess2():
    r = subprocess.call(list('/opt/apache-maven-3.8.7/bin/mvn clean package install -Dmaven.test.skip=true -f /home/dyc/Documents/workspace/btcex/bit/pom.xml'.split(' ')))
    print('Exit code:', r)


# 测试进程间通信， 可以通过 Queue Pipes
def queue_add(q:Queue):
    pid = os.getpid()
    for task in 'ABC':
        print(f'process {pid} add task: {task} to the queue.')
        q.put(task)
        time.sleep(random.random())

def queue_poll(q:Queue):
    pid = os.getpid()
    while True:
        task = q.get(True)
        print(f'process {pid} get task: {task} from the queue.')

def test_multi_process_queue():
    q = Queue()
    add_process = Process(target=queue_add, args=(q, ))
    poll_process = Process(target=queue_poll, args=(q, ))

    add_process.start()
    poll_process.start()

    add_process.join()
    poll_process.terminate()

if __name__ == '__main__':
    # 测试通过进程池执行任务
    # test_pool()

    # test_subprocess()
    # test_subprocess2()

    # test_multi_process_queue()
    pass
