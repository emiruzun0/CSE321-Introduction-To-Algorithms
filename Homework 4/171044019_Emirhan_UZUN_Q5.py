# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:34:01 2021

@author: Emirhan UZUN
"""


def findIndex(arr1, arr2, arr1len, arr2len, target, st1=0, st2=0):
    if (st1 == arr1len):
        return arr2[st2 + target - 1]

    if (st2 == arr2len):
        return arr1[st1 + target - 1]

    if (target == 0 or target > (arr1len - st1) + (arr2len - st2)):
        return -1

    if (target == 1):
        if (arr1[st1] < arr2[st2]):
            return arr1[st1]
        else:
            return arr2[st2]

    curr = int(target / 2)

    if (curr - 1 >= arr1len - st1):
        if (arr1[arr1len - 1] < arr2[st2 + curr - 1]):
            return arr2[st2 + (target - (arr1len - st1) - 1)]
        else:
            return findIndex(arr1, arr2, arr1len, arr2len,
                             target - curr, st1, st2 + curr)

    if (curr - 1 >= arr2len - st2):
        if (arr2[arr2len - 1] < arr1[st1 + curr - 1]):
            return arr1[st1 + (target - (arr2len - st2) - 1)]
        else:
            return findIndex(arr1, arr2, arr1len, arr2len,
                             target - curr, st1 + curr, st2)
    else:
        if (arr1[curr + st1 - 1] < arr2[curr + st2 - 1]):
            return findIndex(arr1, arr2, arr1len, arr2len, target - curr,
                             st1 + curr, st2)
        else:
            return findIndex(arr1, arr2, arr1len, arr2len, target - curr,
                             st1, st2 + curr)


def find(arr1, arr2, target):
    arr1.sort()
    arr2.sort()
    return findIndex(arr1, arr2, len(arr1), len(arr2), target)


arr1 = [8,4,1,6,9]
arr2 = [5,0,7,3,2]
target = 5
print("The {}. element is {}".format(target,find(arr1, arr2, target)));
