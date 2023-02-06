# 基本函数

# 基础输出
print("hello world")
print("hello", "world")

# 输入
# console_input = input("请输入数据:\n")
# print(console_input)

# 关键字
import keyword

print(keyword.kwlist)

# 命名方式: 字母,数字,下划线, 不能数字开头, 严格区分大小写


# 变量的定义  变量由3部分组成 标识 类型 值
name = "test"
print(id(name))
print(type(name))
print(name)

# 赋值
name = "1"
id1 = id(name)
name = "2"
id2 = id(name)
print(id1, id2)

# 数据类型 int , float, bool, str
# int
i = 1
print(type(i))
# float
f = 1.1
print(type(f))
# bool
b = False
print(type(b))
# str
s = "123"
print(type(s))

# 类型强转

print("int -> str: ", str(1), type(str(1)))
print("str -> int: ", int("1"), type(int("1")))

print("int -> float: ", float(1), type(float(1)))
print("float -> int: ", int(1.1), type(int(1.1)))

print("int -> bool: ", bool(1), type(bool(1)))
print("bool -> int: ", int(False), type(int(False)))
print("bool -> int: ", int(True), type(int(True)))

# 运算符 + - * /(除) //(取模) %(取余) **(幂)
print(1 + 1, "2")
print(2 - 1, "1")
print(3 * 5, "15")
print(4 / 3, "1.3333333333333333")
print(4 // 3, "1")
print(2 ** 3, "8")

# 除法
print(9 / 4, "结果为: 2.25")
print(9 / -4, "结果为: -2.25")
print(-9 / 4, "结果为: -2.25")

# 整除: 带符号向下取整  2.25 -> 2, -2.25 -> 3
print(9 // 4, "结果为: 2")
print(9 // -4, "结果为: -3")
print(-9 // 4, "结果为: -3")

# 取余: 数学上余数只能是正数, 计算机编程中余数和除数符号相同
# 余数和除数符号相同, 先计算商, 然后根据公式 [余数= 被除数 - 商 * 除数] 计算余数
print(9 % 4, "结果为: 1")
print(9 % -4, "结果为: -3")  # 余数 = 9 - (-3) * (-4) = -3
print(-9 % 4, "结果为: 3")  # 余数 = -9 - (-3) * 4 = 3

# 赋值运算符, 顺序从右往左
a = b = c = 30
# 对应位置赋值
a, b, c, d = 1, 2, 3, 4
# +=, -=, *=, /=, //=, %=, **=


# 比较运算符
# >, <, >=, <=, !=,
# == (值比较, 类似java的equals)
# is, is not 比较的是id()计算的值 (地址比较, 类似于java的==)


str1 = "12" + "3"
str2 = "1" + "23"
print(str1 == str2, "True")
print(str1 is str2, "True")

int1 = 500 + 500
int2 = 501 + 499
print(int1 == int2, "True")
print(int1 is int2, "True")

list1 = [1]
list2 = [1]
print(list1 == list2, "True")
print(list1 is list2, "False")
print(list1 is not list2, "True")

# bool运算符
# and, or, not, in, not in
a, b = 1, 2
print(a == 1 and b == 2, "True")
print(a == 1 or b == 3, "True")
print(not a == 2, "True")

print("h" in "hello", "True")
print(1 in [1, 2, 3], "True")

# 位运算符
# &, |, <<, >>,

# 运算符顺序, 同组间从左到右
# [**]   ->   [*,/,//,%]   -> [+,-]   -> [<<,>>]  ->   [&]   ->   [|]   ->   [>,<,>=,<=,==,!=]   ->   [and]  -> [or]  -> [=]


print("-------------------------------bool()--------------------------------------")
# 对象的bool值, bool函数
# 以下对象的bool值为False
f = False
print(type(f), bool(f))
i = 0
print(type(i), bool(i))
n = None
print(type(n), bool(n))
s = ''
print(type(s), bool(s))
li=[]
print(type(li), bool(li))
e=()
print(type(e), bool(e))
d=dict({})
print(type(d), bool(d))
ss=set()
print(type(ss), bool(ss))


print("-------------------------------range()--------------------------------------")
# range 返回的是一个迭代器, 并不是一个真正的列表, 因此只占用 start, stop, step三个数的内存空间
# range(stop) 0到stop , 左闭右开, 步进为1
# range(start, stop) start到stop , 左闭右开, 步进为1
# range(start, stop , step) start到stop , 左闭右开, 步进为step
li = range(1, 11, 2)

print(1 in li)
print(2 not in li)

# 查看返回的结果是一个迭代器,并不是一个真正的列表
print(type(li), "range")
print(type(list(li)), "list")

print(li, "range(1, 11, 2)")
print(list(li), "[1, 3, 5, 7, 9]")
# 进行迭代
for _ in li:
    print(_)

