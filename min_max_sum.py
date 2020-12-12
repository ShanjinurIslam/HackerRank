#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    min_val = 2e10
    max_val = -1
    total = 0
    
    for each in arr:
        if min_val > each:
            min_val = each
        if max_val < each:
            max_val = each
        total += each
        
    print(total-max_val,total-min_val)
        

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
