#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    found = dict()
    
    for i,each in enumerate(p):
        found[each] = i+1
        
    for x in range(1,len(p)+1):
        print(found[found[x]])
    
        
        
if __name__ == '__main__':
    n = int(input())

    p = list(map(int, input().rstrip().split()))

    permutationEquation(p)
