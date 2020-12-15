#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    arr.sort()
    n = len(arr)
    out_arr = []
    
    while(n>0):
        min_val = arr[0]
        max_val = arr[-1]
        out_arr.append(n)
        
        while(n>0 and arr[0]==min_val):
            arr.pop(0)
            n -= 1
        
        for i in range(n):
            arr[i] -= min_val
            
    return out_arr
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
