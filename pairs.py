#!/bin/python3
# 2 Sum Technique

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
    arr.sort()
    count = 0
    
    found = dict()
    
    for each in arr:
        target = each + k
        if target in found:
            count += 1
        target -= 2*k
        if target in found:
            count += 1
        
        found[each] = 1
        
    return count
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
