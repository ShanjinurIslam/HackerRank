#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    hash_map = defaultdict(int)
    
    for each in ar:
        hash_map[each] += 1
    
    total = 0
    
    for each in hash_map.keys():
        total += hash_map[each]//2
        
    return total
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
