#!/bin/python3

import math
import os
import random
import re
import sys

def binary_search(arr,V):
    s = 0
    e = len(arr)-1
    
    while(s<=e):
        mid = (s+e)//2
        
        if arr[mid] < V:
            s = mid + 1
        elif arr[mid] > V:
            e = mid - 1
        else:
            return mid

# Complete the introTutorial function below.
def introTutorial(V, arr):
    return binary_search(arr,V)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
