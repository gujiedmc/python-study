#!/usr/bin/env python3

# list 列表
_list = list[1, 'ha', True, [1, 2, 3]]

"""
列表
特点: 
    有序, 可重复, 可以随时添加和删除其中的元素, 类型可混用的集合
实例方法: 
    - 创建
    - 遍历 
    - 获取元素[index]
    - 查看元素是否存在 in / not in,
    - 获取元素位置 list.index(obj, start, end) 
    - 切片[start:stop:step]
    - 排序 sort
包方法:
    - 长度 len
    - 排序 sorted
"""

# ---------------------------list 常见的创建方法-----------------------------
li = [1, 2, 3]

# 由其他数据结构转换
li = list([1, 2, 3])
li = list((1, 2, 3))
li = list(range(3))
li = [i for i in range(10)]

li = [0] + li + [2]
