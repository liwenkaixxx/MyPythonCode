#coding:utf-8
#快速排序

import DataForSort

def quick_sort(lists,left,right):
    print(lists)
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    print(lists)
    quick_sort(lists,low,left-1)
    quick_sort(lists,left+1,high)
    return lists

quick_sort(DataForSort.lists,0,len(DataForSort.lists)-1)
