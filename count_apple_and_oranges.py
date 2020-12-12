#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    total_apples = 0
    total_oranges = 0
    
    for each in apples:
        pos = a + each
        
        if pos >= s and pos<=t:
            total_apples += 1
     
    for each in oranges:
        pos = b + each
        
        if pos >= s and pos<=t:
            total_oranges += 1
            
    print(total_apples)
    print(total_oranges)
    
            
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
