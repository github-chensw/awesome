#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#整数（比如 2、4、20 ）有 int 类型，有小数部分的（比如 5.0、1.6 ）有 float 类型。在这个手册的后半部分我们会看到更多的数值类型。
#除法运算 (/) 永远返回浮点数类型。如果要做 floor division 得到一个整数结果（忽略小数部分）你可以使用 // 运算符；如果要计算余数，可以使用 %
print(4/2)
print(17/3)
print(17//3)
print(17%3)

#在Python中，可以使用 ** 运算符来计算乘方
print(5**2)
print(5**3)

#因为 ** 比 - 有更高的优先级, 所以 -3**2 会被解释成 -(3**2) ，因此结果是 -9. 为了避免这个并且得到结果 9, 你可以用这个式子 (-3)**2.
print(-3**2)
print((-3)**2)

#如果你不希望前置了 \ 的字符转义成特殊字符，可以使用 原始字符串 方式，在引号前添加 r 即可:
print('C:\some\name')
print('C:\\some\\name')
print(r'C:\some\name')

##字符串字面值可以跨行连续输入。一种方式是用三重引号："""...""" 或 '''...'''。
##字符串中的回车换行会自动包含到字符串中，如果不想包含，在行尾添加一个 \ 即可。如下例:
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

#字符串可以用 + 进行连接（粘到一起），也可以用 * 进行重复:
print(3 * 'un' + 'ium')

#相邻的两个或多个 字符串字面值 （引号引起来的字符）将会自动连接到一起.
print('Py' 'thon')

#把很长的字符串拆开分别输入的时候尤其有用:
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)

#字符串是可以被 索引 （下标访问）的，第一个字符索引是 0。单个字符并没有特殊的类型，只是一个长度为一的字符串:
word = 'Python'
print(word[0])  # character in position 0
print(word[5])  # character in position 5

#索引也可以用负数，这种会从右边开始数:
print(word[-1])  # last character
print(word[-2])  # second-last character

#注意 -0 和 0 是一样的，所以负数索引从 -1 开始。
print(word[0])
print(word[-0])

#除了索引，字符串还支持切片。索引可以得到单个字符，而切片可以获取子字符串:
print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)

#注意切片的开始总是被包括在结果中，而结束不被包括。这使得 s[:i] + s[i:] 总是等于 s
print(word[:2] + word[2:])
print(word[:4] + word[4:])

#切片的索引有默认值；省略开始索引时默认为0，省略结束索引时默认为到字符串的结束:
print(word[:2])   # character from the beginning to position 2 (excluded)
print(word[4:])   # characters from position 4 (included) to the end
print(word[-2:])  # characters from the second-last (included) to the end

#您也可以这么理解切片：将索引视作指向字符之间 ，第一个字符的左侧标为0，最后一个字符的右侧标为 n ，其中 n 是字符串长度。例如:
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# 0   1   2   3   4   5   6
#-6  -5  -4  -3  -2  -1
#第一行数标注了字符串非负的索引的位置，第二行标注了对应的负的索引。
#那么从 i 到 j 的切片就包括了标有 i 和 j 的位置之间的所有字符。

#对于使用非负索引的切片，如果索引不越界，那么得到的切片长度就是起止索引之差。例如， word[1:3] 的长度为2
#但是，切片中的越界索引会被自动处理:
print(word[4:40])
print(word[40:])

#Python 中的字符串不能被修改，它们是 immutable 的。因此，向字符串的某个索引位置赋值会产生一个错误:
#word[0] = 'J'
#TypeError: 'str' object does not support item assignment

#内建函数 len() 返回一个字符串的长度:
s = '1234567890'
print(len(s))

#thon 中可以通过组合一些值得到多种 复合 数据类型。其中最常用的 列表 ，可以通过方括号括起、逗号分隔的一组值得到。
# 一个 列表 可以包含不同类型的元素，但通常使用时各个元素类型相同:
print('lists--------------------------------------')
squares = [1, 4, 9, 16, 25]
print(squares)

#Like strings (and all other built-in sequence type), lists can be indexed and sliced:
print(squares[0])  # indexing returns the item
print(squares[-1])
print(squares[-3:])  # slicing returns a new list

#All slice operations return a new list containing the requested elements.
#This means that the following slice returns a new (shallow) copy of the list:
print(squares[:])

#列表同样支持拼接操作:
print(squares + [36, 49, 64, 81, 100])

#与 immutable 的字符串不同, 列表是一个 mutable 类型，就是说，它自己的内容可以改变:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
cubes[3] = 64  # replace the wrong value
print(cubes)

#你也可以在列表结尾，通过 append() 方法 添加新元素 (我们会在后面解释更多关于方法的内容):
cubes.append(6**3)
cubes.append(7**3)
print(cubes)

#给切片赋值也是可以的，这样甚至可以改变列表大小，或者把列表整个清空:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E'] # replace some values
print(letters)
letters[2:5] = [] # now remove them
print(letters)
letters[:] = [] # clear the list by replacing all the elements with an empty list
print(letters)

#内置函数 len() 也可以作用到列表上:
print(len(letters))

#也可以嵌套列表 (创建包含其他列表的列表), 比如说:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x)
print(x[0])

a, b = 0, 1
a, b = b, a+b
print(a,b)