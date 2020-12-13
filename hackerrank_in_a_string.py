#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    template = "hackerrank"
    p = [-1]*len(template)
    i = 0
    n = len(s)
    index = 0
    
    for curr in template:
        for j in range(i,n):
            if s[j] == curr:
                p[index] = j
                i = j+1
                break
        index += 1
        
    for i in range(len(template)-1):
        if p[i]>p[i+1]:
            return "NO"
    
    return "YES"
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
