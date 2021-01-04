#! /usr/bin/python3.5
import random
print(random.random())

# spam = input("请输入：")
spam = 0
if spam == 1:
    print("Hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings")

for i in range(5):     # range(0,5),range(0,5,1)
    print(i)

print('')

a = 0
while a < 5:
    print(a)
    a = a + 1  # a += 1
