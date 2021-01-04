#! /usr/bin/python3

def hu(a):
    a.insert(-1, 'and')
    return ', '.join(a)


spam = ['apples', 'bananas', 'tofu', 'cats']
print(hu(spam))


################################################

def comma(spam1):
    n = len(spam1)
    spam1[-1] = 'and' + ' ' + spam1[-1]
    # spam.insert(n-1,'and')
    # 对列表进行循环
    for i in range(n - 1):
        # print函数以逗号结尾
        print(spam1[i], end=', ')
    print(spam1[-1])


spam1 = ['apples', 'bananas', 'tofu', 'kids', 'cats', 'orange', 'bike']
comma(spam1)