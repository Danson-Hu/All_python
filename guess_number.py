#! /usr/bin/python3.6
import random
"""猜数字"""

number = random.randint(1, 20)
print("猜一个1到20之间的整数，请开始你的表演！")
# print(number)
for i in range(1, 7):
    print("你共有 6 次机会," + "现在是第 " + str(i) + " 次！")
    try:
        guess = int(input('\t'"请输入一个整数："))
    except ValueError:  # 不能为非整数字符串     (xxxError,xxxError)实现抛出多个异常并处理
        print('\t'"请输入数字,消耗一次机会"'\n')
        continue
    if guess < number:
        print('\t'"你猜的数字太小了，再试试！"'\n')
    elif guess > number:
        print('\t'"你猜的数字太大了，再试试！"'\n')
    elif guess == number:
        print("在第 " + str(i) + " 次时你猜对了，答案正是 " + str(number) + " ，恭喜！")
        break

if guess != number and i == 6:
    print("你用光了 " + str(i) + " 次机会也没猜中，正确答案是 " + str(number) + " ，抱歉！")
