#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    arr = sorted(arr)
    brr = sorted(brr)
    
    original_map = defaultdict(int)
    actual_map = defaultdict(int)
    
    for each in brr:
        original_map[each] += 1
        
    for each in arr:
        actual_map[each] += 1
        
    missing = []
        
    for each in original_map.keys():
        if each in actual_map:
            if actual_map[each] == original_map[each]:
                continue
            else:
                missing.extend(abs(actual_map[each] - original_map[each])*[each])
        else:
            missing.extend(original_map[each]*[each])
            
    return sorted(set(missing))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
