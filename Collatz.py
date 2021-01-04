#! /usr/bin/python3.5
# Collatz(考拉咨)序列，冰雹猜想

def collatz(input_number):
    if input_number % 2 == 0:
        print(input_number // 2)
        return input_number // 2
    elif input_number % 2 == 1:
        print(3 * input_number + 1)
        return 3 * input_number + 1


# 确保输入的值为正整数
while True:
    try:
        input_number = int(input("请输入一个正整数："))  # 输入0或负数会陷入死循环
        if input_number > 0:
            break
    #        else:
    #            continue
    except ValueError:  # 不能为非整数字符串     (xxxError,xxxError)实现抛出多个异常并处理
        print("Error:输入数字,凑弟弟!!!")

while input_number != 1:
    input_number = collatz(input_number)  # 赋上函数返回的新值以继续循环

"""
def collatz(n):
    print(n)
    if n % 2 == 1 and n > 1:
        collatz(3*n + 1)
    elif n % 2 == 0:
        collatz(n // 2)

if __name__ == '__main__':
    n = input('Enter a number: ')
    n = int(n)
    collatz(n)
"""
