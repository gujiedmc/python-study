"""
数据结构:
1. 列表 list 类似java中的数组或者list
2. 字段 dict 类似java中的map
3. 集合 set 类似java中的set
4. 元组 tuple 类似java中的不可变list
"""

print("---------------------------list 列表-----------------------------")
"""
列表
特点: 
    有序, 可重复, 类型可混用
实例方法: 
    - 创建
    - 遍历
    - 获取元素[]
    - 查看元素是否存在 in / not in,
    - 获取元素位置 list.index(obj, start, end) 
    - 切片[start:stop:step]
    - 排序 sort
包方法:
    - 长度 len
    - 排序 sorted
    
"""

print("---------------------------list 实例方法-----------------------------")
# 1. 创建方式有3中, 一种使用[1,2]的形式创建, 另外一种使用list()函数创建, 还有一种特殊的列表生成式
li = [1, 2, 3]
li = list([1, 2, 3])
li = list(range(10))
li = [i for i in range(10)]

# 2. 获取元素
# list有正序索引 0 - 长度-1, 倒序索引: 从-长度 - -1
li = ['a', 'b', 'c']
print(li[0], li[-3], "都是a")

# 获取索引, 如果获取不到会报错
li = ['a', 'b', 'c']
print(li.index('b'))
# ValueError: 'd' is not in list
# print(li.index('d'))
print(li.index('c', 1, 3))

# 可以使用 in 判断是否存在
print('a' in li)
print('d' not in li)

# 3. 切片, 对进行切割, 返回一个新的列表
# [start:stop:step] start 默认值为0, stop默认值为长度, step默认值为1.
# start,stop为左闭右开. 索引可以为负值
# step如果为负值则从右向左切割, 此时start是靠右的索引, end是靠左的索引
li = [1, 2, 3, 4, 5, 6]
print(li[::], "=> [1, 2, 3, 4, 5, 6]")
print(li[0:6:1], "=> [1, 2, 3, 4, 5, 6]")
print(li[2:4:1], "=> [3, 4]")
print(li[::2], "=> [1, 3, 5]")

print(li[0:-1:1], "=> [1, 2, 3, 4, 5]")
print(li[-6:-1:1], "=> [1, 2, 3, 4, 5]")

print(li[::-1], "=> [6, 5, 4, 3, 2, 1]")
print(li[6:-1:-1], "=> [2, 1]")

# 4. 添加
print("list add")
li = [1, 2, 3]
print(li)
li.append(4)
print(li, "=> [1, 2, 3, 4]")
li.extend([5, 6])
print(li, "=> [1, 2, 3, 4, 5, 6]")
# 5. 删除 remove, pop,
print()
print("list remove", "从列表中移除一个元素，如果有重复元素只移第一个元素", "不存在的会报错 ValueError: list.remove(x): x not in list")
li = [1, 2, 3]
print(li)
li.remove(3)
print(li)
# 删除不存在的会报错 ValueError: list.remove(x): x not in list
# li.remove(3)

li = [1, 1, 1]
print(li)
li.remove(1)
print(li, "=> [1, 1]")

print()
print("list pop", "弹出指定index的元素", "如果指定的索引位置不存在，将抛出异常", "如果不指定参数，将删除列表中的最后一个元素")

li = [1, 2, 3]
print(li)
li.pop()
print(li, "=>", "[1, 2]")

li = [1, 2, 3]
print(li)
li.pop(1)
print(li, "=>", "[1, 3]")

li = [1, 2, 3]
print(li)
li.pop(-1)
print(li, "=>", "[1, 2]")

# 6. 修改
print("list modify")
li = [1, 2, 3]
print(li)
li[0] = 2
print(li, "=> [2, 2, 3]")

li = [1, 2, 3]
li[0] = None
print(li, "=> [None, 2, 3]")

# 7. 清空元素
li = [1, 2, 3]
li.clear()

# 8.排序
li = [1, 3, 5, 2, 4]
print(li)
# 顺序
li.sort()
print(li, "=>", "[1, 2, 3, 4, 5]")
# 倒序
li.sort(reverse=True)
print(li, "=>", "[5, 4, 3, 2, 1]")


print("---------------------------list 包方法-----------------------------")
