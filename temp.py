# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 21:51:50 2022

@author: lishiyang
"""

word = '123456789123456789'
n = 4
substrings = [word[i:i + 4] for i in range(0, len(word), 4)]
# 列表的嵌套
# 这里的i是另外定义的一个变量
# 这个for循环是从range构建的列表中取出一个数并赋给i
# word[i:i+n]是对word这个list的切片，从第i个开始，到第i+4个结束（不包含第i+4个）
# 即取第0个到第3个1234、第4个到第7个5678、第8个到第11个9123……
# 但为什么把这4个拼成了一个字符串？

coeffs = []  # 创建一个空列表
for substr in substrings:
    num = 0
    print("substr=", substr)
    for x, char in enumerate(substr):
        print("x=", x)
        print("char=", char)
        num += ord(char) * 100 ** x  # 乘100相当于往前倒了两位
        print("ord=", ord(char))
        print("num=", num)
        # the function of 'ord()': return a ASCII of a parameter
        coeffs.append(num ** (1 / 3.0))
    # the function of 'list.append': add a new object at the end of the list

print(coeffs)
