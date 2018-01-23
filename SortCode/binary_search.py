#coding:utf-8
#二分查找

def binary_serach(find,lists):
    low = 0
    high = len(lists)

    if find > lists[high-1]:
        return -1
    elif find <lists[low]:
        return -1

    while low <= high:
        mid = (low + high)/2
        if  lists[mid] == find:
            return mid
        elif lists[mid] > find:
            high = mid - 1
        elif lists[mid] < find:
            low = mid + 1

    return -1
