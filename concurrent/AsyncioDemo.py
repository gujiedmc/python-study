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


async def just_asyncio(i = 1, error=False, cancelled_error=False):
    print('hello: %s' % time.strftime('%X'))
    await asyncio.sleep(i)
    print('world: %s' % time.strftime('%X'))
    if cancelled_error:
        raise asyncio.CancelledError('raise cancelled_error error!')
    if error:
        raise RuntimeError('raise error!')
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

async def test_gather_multi_task():
    """
    测试通过gather并发执行多个task，传入的列表是awaitable对象， 如果是coroutine会被自动转成Future
    gather的结果会按照入参集合的顺序返回一个列表
    有一个return_exceptions的入参， 默认为False，如果有一个task出现异常，会导致其他task执行cancelled，
    如果为True， 则不会中断其他task， 而是在返回的列表中放入Exception信息
    :return:
    """
    # 共耗时3s
    # L = await asyncio.gather(just_asyncio(1),just_asyncio(2), just_asyncio(3))

    # 不会抛出异常， 返回结果为 [1, RuntimeError('raise error!'), 3]
    # L = await asyncio.gather(just_asyncio(1), asyncio.create_task(just_asyncio(2, True)),
    #                          just_asyncio(3), return_exceptions=True)

    # 会抛出 RuntimeError: raise error!, task1执行结束， task2 抛出一场，task3被终端
    L = await asyncio.gather(just_asyncio(1), asyncio.create_task(just_asyncio(2, True)),
                             just_asyncio(3), return_exceptions=False)
    print(type(L), L)


"""
测试超时
asyncio.timeout
"""

async def test_delay():

    await just_asyncio(1)
    # 会抛出TimeoutError
    try:
        async with asyncio.timeout(1):
            await just_asyncio(2)
    except TimeoutError as e:
        pass
    else:
        raise AssertionError('catch TimeoutError fail')

    pass

async def test_delay_new():
    """
    3.11 新功能, 通过asyncio.timeout返回的上下文管理器可以在运行时指定超时时间
    """
    try:
        async with asyncio.timeout(1) as cm:
            # 返回当前deadline, 基于loop.time()的结束时间，如果没设置则返回None
            print(cm.when() - asyncio.get_running_loop().time())
            # 返回当前是否过期 True/False
            print(cm.expired())
            # 动态设置超时时间为1s
            new_deadline = asyncio.get_running_loop().time() + 2
            cm.reschedule(new_deadline)
            # 等待2s，会抛出异常
            await just_asyncio(2)
    except TimeoutError as e:
        pass
    else:
        raise AssertionError('catch TimeoutError fail')

    """
    3.11 新功能, 通过asyncio.timeout_at(when) 方法指定一个基于loop时间的绝对值时间
    """
    try:
        async with asyncio.timeout_at(asyncio.get_running_loop().time() + 2):
            # 等待2s，会抛出异常
            await just_asyncio(2)
    except TimeoutError as e:
        pass
    else:
        raise AssertionError('catch TimeoutError fail')

    """
    3.11 新功能, 通过asyncio.wait_for 指定登台一个awaitable对象指定时间
    当wait_for的task被cancelled后， 会直接抛出TimeoutError
    """
    try:
        # await just_asyncio(2)
        await asyncio.wait_for(just_asyncio(2), 2)
    except TimeoutError as e:
        pass
    else:
        raise AssertionError('catch TimeoutError fail')

async def test_simple_wait():
    """
    简单等待, asyncio.wait()
    return_when 可以设置什么时候返回,
    返回的是完成的task列表,和未完成的task列表
    """
    ls = [asyncio.create_task(just_asyncio(1)), just_asyncio(2)]
    done, pending = await asyncio.wait(ls, timeout=3, return_when=asyncio.tasks.ALL_COMPLETED)
    print(done)
    print(pending)

async def test_task_result_to_gnerator():
    """
    asyncio.as_completed 将执行一堆task执行, 并返回一个结果的迭代器, 按task完成顺序放入迭代器
    """
    ls = [asyncio.create_task(just_asyncio(1)), just_asyncio(2), just_asyncio(3)]
    li = asyncio.as_completed(ls, timeout=2)
    assert type(li).__name__ == 'generator'
    for co in li:
        earliest_result = await co
        print('执行结束, 收到结果: ',earliest_result)
    pass

if __name__ == '__main__':
    # test_just_asyncio()
    # test_run_coroutine()
    # asyncio.run(test_create_task())
    # print(asyncio.run(test_multi_task()))
    # asyncio.run(test_task_cancellation())
    # asyncio.run(test_task_group())
    # asyncio.run(test_gather_multi_task())
    # asyncio.run(test_delay())
    # asyncio.run(test_delay_new())
    # asyncio.run(test_simple_wait())
    asyncio.run(test_task_result_to_gnerator())
    pass