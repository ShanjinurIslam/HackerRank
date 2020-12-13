#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the beautifulBinaryString function below.
def arr_to_str(arr):
    string = ""
    for each in arr:
        string += each

    return string

# Complete the beautifulBinaryString function below.
def beautifulBinaryString(binary):
    stack = []
    n = 0
    count = 0

    for b in binary:
        if n < 2:
            stack.append(b)
            n += 1
        else:
            stack.append(b)
            n += 1

            start = n-3
            end = n

            temp = arr_to_str(stack[start:end])
            
            if temp == "010":
                count += 1
                stack[end-1] = '1'


    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    b = input()

    result = beautifulBinaryString(b)

    fptr.write(str(result) + '\n')

    fptr.close()
