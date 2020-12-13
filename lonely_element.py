#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the lonelyinteger function below.
def lonelyinteger(a):
    found = defaultdict(int)
    
    for each in a:
        found[each] += 1
        
    for each in found.keys():
        if found[each] == 1:
            return each

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
