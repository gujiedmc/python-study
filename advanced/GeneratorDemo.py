"""  生成器""""""杨辉三角生成器"""def triangles1():    yield [1]    li = [1, 1]    while True:        yield li        left = li[0:-1]        right = li[1:]        li = [1] + [left[i] + right[i] for i in range(len(left))] + [1]def triangles2():    li = [1]    while True:        yield li        newList = [0] + li + [0]        li = [newList[i] + newList[i + 1] for i in range(len(newList) - 1)]def triangles3():    li = [1]    while True:        yield li        li = [1] + [li[i] + li[i + 1] for i in range(len(li) - 1)] + [1]def triangles4():    li = [1]    while True:        yield li        li = [m + n for m, n in zip([0] + li, li + [0])]# 调用生成器start, count = 1, 10for li in triangles4():    if start > count:        break    start += 1    print(li)