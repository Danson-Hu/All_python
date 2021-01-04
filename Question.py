# 冒泡排序
def bubbleSort(arr):
    for i in range(len(arr)-1, 0, -1):  # i每次遍历需要比较的次数，是逐渐减小的
        for j in range(i):  # j为列表下标
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


li = [54, 26, 93, 17, 77, 31, 44, 55, 20, 26, 5]
print(bubbleSort(li))

# 二分查找


def dichotomySearch(num, myList):
    myList = sorted(myList)
    print('排序后列表', myList)

    first = 0
    last = len(myList) - 1
    while first <= last:
        middle = (first + last) // 2
        if myList[middle] == num:
            return middle
        elif myList[middle] > num:
            last = middle - 1
        elif myList[middle] < num:
            first = middle + 1
    return None


key = 12
list1 = [1, 5, 9, 3, 6, 12, 7, 25, 10]
result = dichotomySearch(key, list1)
if result is not None:
    print('查找的元素是', key, '序号下标为：', result)
else:
    print('未找到该元素')


