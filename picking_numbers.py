#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    a.sort()
    n = len(a)
    max_val = 0
    for i in range(n-1):
        curr_max = 1
        curr = 1
        for j in range(i+1,n):
            if a[j]-a[i]<=1:
                curr += 1
                curr_max = max(curr_max,curr)
            else:
                curr = 1
        max_val = max(max_val,curr_max)
        
    return max_val
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()
