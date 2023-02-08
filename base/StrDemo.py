#!/usr/bin/env python3

# --------------------------定义-------------------------------
a = 'a'
b = "b"
c = """
    支持
    换行
    """


# -------------------------基本方法-----------------------------

# 类型强转
str = str(1)
# 获取长度
assert len('abc') == 3
assert len('中文') == 2






# --------------------------编码------------------------------
"""
    1. python3 默认编码是 Unicode
"""

# ord(char) 函数获取字符的整数表示
assert ord('A') == 65
# chr(int) 函数可以将整数编码转为字符
assert chr(65) == 'A'

# 可以直接通过Unicode编码直接输出字符
assert ord('中') == 20013 == 0x4e2d
assert ord('文') == 25991 == 0x6587
# \u是 Unicode编码， \x是utf-8编码
assert '中文' == '\u4e2d\u6587'

# 字符串和字节数组转换
assert '中文'.encode('utf-8') == b'\xe4\xb8\xad\xe6\x96\x87'
assert b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') == '中文'






# --------------------------格式化------------------------------
"""
    有三种格式化: % 表达式， format() 函数， s-fstring
    1. 格式化类型
        d 表示整数， 
        % 
"""

# %
# format()

# 不指定顺序
assert '{} {}'.format('hello', 'world') == 'hello world'
# 指定顺序
assert '{1} {0} {1}'.format('hello', 'world') == 'world hello world'
# 通过变量
assert '{name}:{age}'.format(name='zhang', age=3) == 'zhang:3'
# 通过字典
_site = {"name": "zhang", "age": 3}
assert '{name}:{age}'.format(**_site) == 'zhang:3'
# 通过list的index
_list = ['zhang', 3]
_list2 = ['li', 4]
assert '{0[0]}:{0[1]},{1[0]}:{1[1]}'.format(_list, _list2) == 'zhang:3,li:4'
# 通过对象
class User(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

user1 = User('zhang', 3)
user2 = User('li', 4)
assert '{0.name}:{0.age},{1.name}:{1.age}'.format(user1, user2) == 'zhang:3,li:4'