# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 01:57:42 2021

@author: Emirhan UZUN | 171044019
"""

def isSubsetSum(index, equal_zero, lookup_table, pos_sum, neg_sum, notZeroList, subset):
    key = (index, equal_zero)
    result = False
    new_path = subset + [notZeroList[index]]
    if equal_zero < neg_sum or equal_zero > pos_sum:
        result = False
    elif index == 0:
        result = notZeroList[0] == equal_zero
        if result:
            print(new_path)
    elif key in lookup_table and 0 != index:
        result = lookup_table[key]
    else:
        result = notZeroList[index] == equal_zero
        if result:
            print(new_path)
        else:
            result = isSubsetSum(index-1, equal_zero, lookup_table, pos_sum, neg_sum, notZeroList, subset)
            if not result:
                result = isSubsetSum(index-1, equal_zero-notZeroList[index], lookup_table, pos_sum, neg_sum, notZeroList, new_path)
    lookup_table[key] = result
    return result

def isSubsetSumHelper(values, equal_zero=0):
    p = [integer for integer in values if integer > 0]
    n = [integer for integer in values if integer < 0]
    not_zeros = p + n
    pos_sum = sum(p)
    neg_sum = sum(n)
    lookup_table = {}
    subset = []
    return isSubsetSum(len(not_zeros)-1, equal_zero, lookup_table, pos_sum, neg_sum, not_zeros, subset)
values = [2, 3, -5, -8, 6, -1]
equal_zero = 0
result = isSubsetSumHelper(values, equal_zero=equal_zero)
print('The set %s a subset sum of %d.' % ( 'has' if result else 'does not have', equal_zero))
