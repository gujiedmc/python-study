"""
异步并发

  await 必须是在 async function 中使用
  async function 返回的是一个 coroutine
  asyncio.run 方法内部会将 coroutine 通过 asyncio.create_task() -> BaseEventLoop.create_task() 创建一个task, 并且会等待这个task执行结束

  核心思想是EventLoop执行task。
  当EventLoop执行一个task的时候，执行权需要task显式的释放给EventLoop，释放方式有2种，
  一种是方法执行结束return, 另一种是await另外一个task。

  可以await的类型有3种(awaitable)，task，future
      coroutine(async function返回的对象就是协程对象)， await 一个 coroutine的时候会等待这个task执行结束
      task，通过 asyncio.create_task将coroutine封装成为一个task， await 一个 task的时候，并不会等待这个task执行
"""
import asyncio
import time


async def just_asyncio(i = 1):
    print('hello: %s' % time.strftime('%X'))
    await asyncio.sleep(i)
    print('world: %s' % time.strftime('%X'))
    return i

def test_just_asyncio():
    # async function 返回的是一个 coroutine
    assert type(just_asyncio()).__name__ == 'coroutine'
def test_run_coroutine():
    # asyncio.run 方法内部会将 coroutine 通过 asyncio.create_task() -> BaseEventLoop.create_task() 创建一个task
    return asyncio.run(just_asyncio())
async def test_create_task():
    task = asyncio.create_task(just_asyncio())
    # 执行并等待执行结果
    return asyncio.run(asyncio.create_task(just_asyncio()))

async def test_multi_task():
    """
    await 一个 coroutine的时候会等待这个task执行结束， 所以执行总耗时是3s
    """
    await just_asyncio(1)
    await just_asyncio(2)

    print('--------------------------------------')
    """
    await 一个 task的时候，并不会等待这个task执行， 所以执行总耗时是2s
    """
    task1 = asyncio.create_task(just_asyncio(1))
    task2 = asyncio.create_task(just_asyncio(2))

    await task1
    await task2

    return task1.result(), task2.result()

async def cancel_task(task:asyncio.Task):
    task.cancel()
async def test_task_cancellation():
    """
    测试取消task
    :return:
    """
    try:
        task1 = asyncio.create_task(just_asyncio(10))
        task2 = asyncio.create_task(cancel_task(task1))
        await task1
        await task2
    except asyncio.CancelledError as e:
        pass
    else:
        raise Exception('catch CancelledError fail')

async def add_group_task(group, cor):
    group.create_task(cor)

async def test_task_group():
    """
    async with 语句会等待 组内所有的task执行完毕，在执行结束之前，仍然可以添加task。
    一旦有一个task执行中抛出非CancelledError的报错，组内其他未执行的task会抛出CancelledError， 外部正在执行该执行 async with 的task也会报错。
    所有task执行结束后， 如果task_group中有非CancelledError报错，则会将异常信息封装在ExceptionGroup中
    """
    async with asyncio.TaskGroup() as tg, asyncio.TaskGroup() as tg2:
        tg.create_task(just_asyncio(1))
        tg.create_task(just_asyncio(2))
        # 如果这里设置为4， 则总耗时为4， 如果设置为1， 则总耗时为2
        # tg.create_task(add_group_task(tg, just_asyncio(4)))
        tg.create_task(add_group_task(tg, just_asyncio(2)))



if __name__ == '__main__':
    # test_just_asyncio()
    # test_run_coroutine()
    # asyncio.run(test_create_task())
    # print(asyncio.run(test_multi_task()))
    # asyncio.run(test_task_cancellation())
    asyncio.run(test_task_group())
    pass