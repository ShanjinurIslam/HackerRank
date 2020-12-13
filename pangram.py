#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    s = s.lower()
    char_map = [-1]*26
    
    for each in s:
        val = ord(each)
        if val>=97 and val<=122:
            val = val-97
            char_map[val] = 1
    
    for each in char_map:
        if each == -1:
            return "not pangram"
    return "pangram"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
