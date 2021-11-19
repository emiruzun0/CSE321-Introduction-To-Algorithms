# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

c = 0
d = 0

def insertionSort(arr): 
  
    # Traverse through 1 to len(arr) 
    for i in range(1, len(arr)): 
        global d
  
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
                d = d +1
        arr[j+1] = key 


def partition(arr, low, high):
    i = (low-1)         # index of smaller element
    pivot = arr[high]     # pivot
    global c
 
    for j in range(low, high):
 
        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
 
            # increment index of smaller element
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            c = c+1
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    c = c+1
    return (i+1)
 
# The main function that implements QuickSort
# arr[] --> Array to be sorted,
# low  --> Starting index,
# high  --> Ending index
 
# Function to do Quick sort
 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
 
        # pi is partitioning index, arr[p] is now
        # at right place
        pi = partition(arr, low, high)
 
        # Separately sort elements before
        # partition and after partition
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)


if __name__ == '__main__':			#Main
    givenArray = [235,383,436,63,19,90,22]
    givenArray2 = [235,383,436,63,19,90,22]
    quickSort(givenArray, 0, len(givenArray)-1)
    print(givenArray)
    print("Swap number for quick sort : {}".format(c))
    insertionSort(givenArray2)
    print(givenArray2)
    print("Swap number for insertion sort : {}".format(d))








{10, 7, 8, 9, 1, 5};











