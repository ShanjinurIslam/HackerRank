#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    new_string = ""
    
    for each in s:
        val = ord(each)
        
        if val>=65 and val <= 90:
            val = val-65
            val = (val+k)%26
            val = val+65
            new_string += chr(val)
        elif val >= 97 and val <= 122:
            val = val-97
            val = (val+k)%26
            val = val+97
            new_string += chr(val)
        else:
            new_string += each
     
    
    return new_string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
