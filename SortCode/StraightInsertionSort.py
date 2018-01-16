#coding:utf-8
#插入排序——直接插入排序——时间复杂度　O(n^2)

import DataForSort

def insert_sort(li):
    count = len(li)
    for i in range(1,count):
        j = i - 1
        key = li[i]
        while j >= 0:
            if key < li[j]:
#               list[j] = key
                li[j+1] = li[j]
                li[j] = key
                print(li)
            j = j-1
    return li

insert_sort(DataForSort.lists)

