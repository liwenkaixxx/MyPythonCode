#coding:utf-8
#冒泡排序

import DataForSort


def bubble_sort(lists):
    count = len(lists)
    for i in range(count):
        for j in range(i+1,count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
                print(DataForSort.lists)
    return lists

bubble_sort(DataForSort.lists)
