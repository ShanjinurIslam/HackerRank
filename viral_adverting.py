#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    total_liked = 0
    curr = 5
    
    for _ in range(1,n+1):
        total_liked += math.floor(curr/2)
        curr = math.floor(curr/2)*3
        
    return total_liked
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
