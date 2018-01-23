#coding:utf-8

def maxSum(listofnums):
    maxsum = 0
    maxtmp = 0

    for i in range(len(listofnums)):
        if maxtmp <= 0:
