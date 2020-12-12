#!/bin/python3

import math
import os
import random
import re
import sys

def birthday(s, d, m):
    count = 0

    s.insert(0,0)
    n = len(s)
    curr = sum(s[:m])


    for i in range(1,n-m+1):
        curr = sum(s[i:i+m])
        if curr == d:
            count += 1
    
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
