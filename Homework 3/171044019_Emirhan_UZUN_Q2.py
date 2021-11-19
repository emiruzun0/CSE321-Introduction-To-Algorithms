# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 01:25:34 2020

@author: Emir
"""
lineNumber = 0

def function(n):
    global lineNumber
    if n <= 1:
        print("**")
        lineNumber = lineNumber + 1
    else:
        for i in range(1,n+1):
            function(n//2)



if __name__ == '__main__':			#Main
    #function(2)
    #function(4)
    #function(8)
    function(16)
    #function(32)
    
    print("Line counter  : {}".format(lineNumber))