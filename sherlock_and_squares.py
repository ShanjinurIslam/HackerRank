#!/bin/python3

import math
import os
import random
import re
import sys
from math import sqrt

# Complete the squares function below.
def squares(a, b):
    start = math.floor(sqrt(a))
    end = math.floor(sqrt(b))
    
    count = 0
    
    for i in range(start,end+1):
        val = i*i 
        if val >=a and val<=b:
            count += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
