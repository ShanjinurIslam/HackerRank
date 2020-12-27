#!/bin/python3

import math
import os
import random
import re
import sys

def individual(arr,x,y):
    total = 0
    for i in range(x,x+3):
        for j in range(y,y+3):
            total += arr[i][j]
    
    return total - arr[x+1][y] - arr[x+1][y+2]
# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_val = -2e10
    for i in range(0,4):
        for j in range(0,4):
            val = individual(arr,i,j)
            print(i,j,val)
            max_val = max(max_val,val)
        
            
    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
