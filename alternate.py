#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict
def new_string(s,a,b):
    new = ""
    for each in s:
        if each == a or each == b:
            new += each
        else:
            continue
    return new

def isAlternating(s,n):
    for i in range(n-1):
        if s[i] == s[i+1]:
            return False
    return True

def alternate(word):
    hash_map = defaultdict(int)

    for each in word:
        hash_map[each] += 1

    chars = list(hash_map.keys())
    n = len(chars)

    max_val = 0

    for i in range(n-1):
        for j in range(i+1,n):
            temp = new_string(word,chars[i],chars[j])
            x = len(temp)
            if isAlternating(temp,x):
                print(temp)
                if x>max_val:
                    max_val = x
            
            

    return max_val 
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
