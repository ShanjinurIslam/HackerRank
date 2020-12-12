#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    n = 0
    
    for each in arr:
        if each > 0:
            pos += 1
        elif each < 0:
            neg += 1
        else:
            zero += 1
        n += 1
            
    print(pos/n)
    print(neg/n)
    print(zero/n)
    
    
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
