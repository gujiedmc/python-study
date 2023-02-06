# 流程控制

print("---------------------------IF-ELSE-----------------------------")
# IF ELSE
# Python严格限制缩进,通过缩进判断语句关系
# pass语句 , 在IF-ELSE 条件下没有具体逻辑时, 可以使用pass标记.
# pass语句 可以在 IF-ELSE语句, for in 语句, 定义的函数体中使用
a, b, c = 1, 2, 3

if a < b:
    print("分支1")
    if b < c:
        print("分支1-1")
    elif b > c:
        print("分支1-2")
    else:
        print("分支1-3")
elif a > b:
    print("分支2")
else:
    pass

# 组合条件, 下面两种效果一致
if a < b and b < c:
    print("a < b 并且 b < c")

if a < b < c:
    print("a < b 并且 b < c")

print("---------------------------三元表达式-----------------------------")
# 三元表达式

maxValue = a if a >= b else b
print(str(a) + "," + str(b) + "中max值为:", maxValue)

print("---------------------------WHILE 循环-----------------------------")
# while-else 当while语句中没有执行break时,会执行else语句中的代码
index = 0
while index < 10:
    index += 1
    # 继续下一个循环
    if index % 2 == 0:
        print(index)
        continue
    # 跳出循环
    if index >= 18:
        break
else:
    # 循环内部代码未执行break, 即没有触发合适的条件
    print("while循环体未执行break")

print("---------------------------FOR 循环-----------------------------")
# for循环, 可以遍历的类型有: list, dict, set, tuple, range, str等等
# for 元素变量名 in 迭代对象变量名
# for-else 当for循环中没有执行break语句, 会执行while体重的语句
li = [0, 1, 2]
for _ in li:
    print(_)
    if _ == 10:
        break
else:
    print("li中没有执行break")

s = "Hello"
for v in s:
    print(v)
