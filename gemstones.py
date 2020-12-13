#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the gemstones function below.
def gemstones(arr):
    n = len(arr)
    
    found = defaultdict(int)
    for word in arr:
        word_wise_char = defaultdict()
        for char in word:
            word_wise_char[char] = 1
        for each in word_wise_char.keys():
            found[each] += 1
    
    count = 0
    for each in found.keys():
        if found[each] == n:
            count += 1
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
