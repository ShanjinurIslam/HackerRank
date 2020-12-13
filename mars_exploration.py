#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    template = "SOS"
    
    counter = 0
    invalid = 0
    
    for each in s:
        if each!=template[counter]:
            invalid += 1
        counter = (counter+1)%3
            
    return invalid

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
