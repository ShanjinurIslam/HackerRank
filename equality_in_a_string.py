#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the equalizeArray function below.
def equalizeArray(arr):
    n = len(arr)
    found = defaultdict(int)
    
    for each in arr:
        found[each] += 1
        
    return n-max(found.values())
    
        
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
