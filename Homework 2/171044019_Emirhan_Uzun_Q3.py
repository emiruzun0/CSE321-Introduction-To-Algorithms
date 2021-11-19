# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 00:32:14 2020

@author: Emirhan UZUN
"""

def mergeSort(givenArray):
    if len(givenArray) > 1:
 
         # Finding the mid of the array
        middle = len(givenArray)//2
 
        # Dividing the array elements
        left = givenArray[:middle]
 
        # into 2 halves
        right = givenArray[middle:]
 
        # Sorting the first half
        mergeSort(left)
 
        # Sorting the second half
        mergeSort(right)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                givenArray[k] = left[i]
                i += 1
            else:
                givenArray[k] = right[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(left):
            givenArray[k] = left[i]
            i += 1
            k += 1
 
        while j < len(right):
            givenArray[k] = right[j]
            j += 1
            k += 1


def findPairMultiplication(givenArray, desiredNumber):
     
   
    mergeSort(givenArray)
    
    low = 0             #lowest index 
    high = len(givenArray) -1   #highest index
    
    while low < high:           #turns until low index pass the high index
        if givenArray[low] * givenArray[high] == desiredNumber:
            print("({},{})".format(givenArray[low],givenArray[high]))   #print if multiplicity is equal to desired number
        
        if givenArray[low] * givenArray[high] < desiredNumber:  #if the desired number is bigger than multiplication, then increment the lower index
            low = low + 1 
        else:
            high = high -1
     
   
if __name__ == '__main__':			#Main
    givenArray = [1,2,3,6,5,4]
    desiredNumber = 6
    findPairMultiplication(givenArray, desiredNumber)
