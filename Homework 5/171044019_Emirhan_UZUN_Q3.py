# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 03:08:04 2021

@author: Emirhan UZUN
"""


def knapSack(W, weight, val, n): 
    knapSackTable = [[0 for x in range(W + 1)] for x in range(n + 1)] 
  
    # Build table K[][] in bottom up manner 
    for i in range(n + 1): 
        for w in range(W + 1): 
            if i == 0 or w == 0: 
                knapSackTable[i][w] = 0
            elif weight[i-1] <= w: 
                knapSackTable[i][w] = max(val[i-1] 
                          + knapSackTable[i-1][w-weight[i-1]],   
                              knapSackTable[i-1][w]) 
            else: 
                knapSackTable[i][w] = knapSackTable[i-1][w] 
  
    return knapSackTable[n][W] 
  
  
# Driver code 
if __name__=='__main__':
    values = [10, 4, 3] 
    weight = [5, 4, 2] 
    W = 9
    n = len(values) 
    print('The knapsack value is : ')
    print(knapSack(W, weight, values, n)) 
  