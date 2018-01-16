#coding:utf-8
#选择排序

import DataForSort

def select_sort(lists):
    count = len(lists)
    for i in range(count):
        lists[i] = min(lists[i:])
        print(lists)
    return lists


select_sort(DataForSort.lists)

