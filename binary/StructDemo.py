"""
1. https://docs.python.org/zh-cn/3/library/struct.html
"""
import struct
from struct import *


intByte = struct.pack(">i", 1)

assert type(intByte) == bytes

# 数字转二进制

# 4位有符号int
assert struct.pack(">i", 1) == b'\x00\x00\x00\x01'
# 8位有符号long
assert struct.pack(">q", 1) == b'\x00\x00\x00\x00\x00\x00\x00\x01'
# 8位 double
assert struct.pack(">d", 1) == b'?\xf0\x00\x00\x00\x00\x00\x00'

# 2个 4位有符号int
assert struct.pack(">ii", 1, 1) == b'\x00\x00\x00\x01\x00\x00\x00\x01'

# 二进制转数字
assert struct.unpack(">i", b'\x00\x00\x00\x01') == (1,)
assert struct.unpack(">ii", b'\x00\x00\x00\x01\x00\x00\x00\x01') == (1, 1)