#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def getTotalX(a, b):
    m = len(b)

    temp = factors(b[0])

    for i in range(1,m):
        factor_set = factors(b[i])
        temp = temp.intersection(factor_set)

    count = 0

    for each in  temp:
        flag = True
        for i in a:
            if each%i !=0:
                flag = False
                break
        if flag:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
