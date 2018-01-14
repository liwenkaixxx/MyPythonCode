#coding:utf-8

def binary_search(find,list1):
    low = 0
    high = len(list1)

    if find > list2[high - 1]:
        return -1

    elif find < list2[low]:
        return -1

    while low <= high:
        mid = (low + high)/2
        if list1[mid] == find:
            return mid

        #左边
        elif list1[mid] > find:
            high = mid - 1

        #右边
        elif list1[mid] < find:
            low = mid + 1

    #未找到
    return -1

list2 = [1,2,3,4,5,6,7,8,9,34,45,56,67,78]

list2.sort()

print("原有序序列：",list2)
while True:
    try:
        find = int(raw_input("轻输入要查找的数："))
    except:
        print("正整数！")
        continue

    result = binary_search(find, list2)

    if result != -1:
        print "要找的数是：%d位置是：%d" % (find, result)
    else:
        print("？？？？？？？？？")



