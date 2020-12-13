#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumLoss function below.
def minimumLoss(price):
    pairs = []
    
    for i,each in enumerate(price):
        pairs.append((each,i))
        
    pairs.sort()
    
    n = len(pairs)
    min_val = 10e10
    
    for i in range(n-1):
        if pairs[i+1][1] < pairs[i][1]:
            if min_val > (pairs[i+1][0]-pairs[i][0]):
                min_val = (pairs[i+1][0]-pairs[i][0])
    
    return min_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    fptr.write(str(result) + '\n')

    fptr.close()
