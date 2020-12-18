#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the repeatedString function below.
def repeatedString(s, n):
    count_in_full_string = 0
    for each in s:
        if each == 'a':
            count_in_full_string += 1
            
    div = n//len(s)
    mod = n%len(s)
    
    total = count_in_full_string*div
    
    for i in range(mod):
        if s[i] == 'a':
            total += 1
    
    return total
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
