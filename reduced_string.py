#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    stack = []
    n = 0
    
    for each in s:
        if n == 0:
            stack.append(each)
            n += 1
        elif stack[-1] != each:
            stack.append(each)
            n += 1
        else:
            stack.pop()
            n -= 1
    
    final = ""
    if n > 0:
        for each in stack:
            final += each
        return final
    else:
        return "Empty String"        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
