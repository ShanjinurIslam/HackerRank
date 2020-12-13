#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the funnyString function below.
def funnyString(s):
    rev = s[::-1]
    
    ord_forward = [ord(each) for each in s]
    ord_backward = [ord(each) for each in rev]
    
    n = len(s)
    abs_for = [-1]*(n-1)
    abs_back = [-1]*(n-1)
    
    
    for i in range(n-1):
        abs_for[i] = abs(ord_forward[i]-ord_forward[i+1])
        abs_back[i] = abs(ord_backward[i]-ord_backward[i+1])
        
        if abs_for[i]!=abs_back[i]:
            return "Not Funny"
    
    return "Funny"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = funnyString(s)

        fptr.write(result + '\n')

    fptr.close()
