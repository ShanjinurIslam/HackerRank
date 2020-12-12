#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict 
# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    hash_map = defaultdict(int)
    
    for each in arr:
        hash_map[each] += 1
        
    max_val = -1
    id = -1
    
    for each in hash_map.items():
        if each[1] > max_val:
            max_val = each[1]
            id = each[0]
        elif each[1] == max_val:
            if id > each[0]:
                id = each[0]
        else:
            continue
        
    return id

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
