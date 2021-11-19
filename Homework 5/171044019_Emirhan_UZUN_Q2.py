# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 03:04:02 2021

@author: Emirhan UZUN | 171044019
"""


def minSumPath(set):
    totalSum = [None] * len(set)
    path = [[]] * len(set)
    previousPath = [[]] * len(set)
    n = len(set) - 1
    for i in range(len(set[n])):
        totalSum[i] = set[n][i]
        previousPath[i] = [set[n][i]]
    for i in range(len(set) - 2, -1,-1):
        for j in range( len(set[i])):
            if totalSum[j] > totalSum[j + 1]:
                path[j] = previousPath[j + 1] + [set[i][j]]
            else:
                path[j] = previousPath[j] + [set[i][j]]
            previousPath = path
            totalSum[j] = set[i][j] + min(totalSum[j], totalSum[j + 1])
    return totalSum[0], path[0]

set = [[ 2 ], 
    	[5, 4 ], 
    	[1, 4, 7 ],
        [8,6,9,6]] 
print('Minimum path value and path : ')
print(minSumPath(set)) 