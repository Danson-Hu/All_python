#! /usr/bin/python3.5
# 斐波那契数列

# 输出存有n个数的斐波那契数列列表
def fibs(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fibs = [1, 1]
    for i in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs


print(fibs(24))


# 查第a个斐波那契数
def f(a):
    i, j = 1, 1
    for k in range(a - 1):
        i, j = j, i + j
    return i


print(f(4))


# 查第b个斐波那契数,使用递归！！！
def fib(b):
    if b == 1 or b == 2:
        return 1
    return fib(b - 1) + fib(b - 2)


print(fib(10))
