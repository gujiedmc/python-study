"""
在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
"""

def person(name, age, *, city, job):
    print(name, age, city, job)

# TypeError: person() got an unexpected keyword argument 'T'
print(person('zhang', 3, city='sh', job=None, T='fale'))