# -*- coding: utf-8 -*-
"""
Created on Wed Jan  13 23:10:22 2021

@author: Emir
"""

def calculate(n):
    if n==1:
        return 0
    else:
        return 1 + calculate(n/2)


if __name__ == '__main__':			#Main
    print("Logn  : {}".format(calculate(128)))