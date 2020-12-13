#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    if s == s[::-1]:
        return -1
    
    n = len(s)
    for i in range(n):
        if i == 0:
            new = s[i+1:]
        else:
            new = s[:i] + s[i+1:]
            
        if new == new[::-1]:
            return i
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
