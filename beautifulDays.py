#!/bin/python3

import math
import os
import random
import re
import sys

def reverse_number(n):
    out = 0
    while(n):
        out *= 10
        out += n % 10
        n //= 10

    return out


def beautifulDays(i, j, k):
    count = 0
    
    for i in range(i,j+1):
        if(abs(i-reverse_number(i))%k == 0):
            count +=1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
