"""
函数式编程
map,reduce,filter

"""
from functools import reduce


def addOne(x):
    return x + 1


mapResult = map(addOne, list(range(10)))
assert type(mapResult) == map
assert list(mapResult) == list(range(1, 11))

mapResult = map(lambda x: x + 1, list(range(10)))
assert type(mapResult) == map
assert list(mapResult) == list(range(1, 11))

# 转换成字符串
assert list(map(str, list(range(1, 4)))) == ['1', '2', '3']


# reduce

def mySum(x, y):
    return x + y


# reduce 求和
reduceResult = reduce(mySum, list(range(1, 11)))
assert type(reduceResult) == int
assert reduceResult == sum(list(range(1, 11)))
# 改为 lambda
reduce(lambda x, y: x + y, list(range(1, 11)))
assert type(reduceResult) == int
assert reduceResult == sum(list(range(1, 11)))


# reduce 字符串拼接
def strConcat(s1, s2):
    return '{},{}'.format(s1, s2)


reduceResult = reduce(strConcat, list(range(1, 11)))
assert type(reduceResult) == str
assert reduceResult == '1,2,3,4,5,6,7,8,9,10'

reduceResult = reduce(lambda s1, s2: '{},{}'.format(s1, s2), list(range(1, 11)))
assert type(reduceResult) == str
assert reduceResult == '1,2,3,4,5,6,7,8,9,10'

# map 和 reduce 一起用
s = '1,2,3,4,5,6,7,8,9,10'
assert reduce(lambda x, y: x + y, map(int, s.split(","))) == 55

# filter
assert type(filter(lambda x: x % 2 == 0, list(range(1, 11)))) == filter
assert list(filter(lambda x: x % 2 == 0, list(range(1, 11)))) == [2, 4, 6, 8, 10]
