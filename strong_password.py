#!/bin/python3

import math
import os
import random
import re
import sys

# O(n) solution
# Complete the minimumNumber function below.
def minimumNumber(n, password):
    count_number = 0
    count_lower_case = 0
    count_upper_case = 0
    count_sc = 0
    
    for each in password:
        val = ord(each)
        if val>=48 and val<=57:
            count_number += 1
        elif val>=97 and val<=122:
            count_lower_case += 1
        elif val>=65 and val<=90:
            count_upper_case += 1
        else:
            count_sc += 1   
    
    # Filling minimum requirement
    required = 0
            
    if count_number == 0:
        required += 1
    if count_lower_case == 0:
        required += 1
    if count_upper_case == 0:
        required += 1
    if count_sc == 0:
        required += 1
    
    # check if length < 6
    remaining = 0
    if n < 6:
        remaining = 6-n
    
    # if length is less than 6 and remaining greater or equal to required   
    if remaining >= required:
        return remaining
    else:
        return required
            
    
    # Return the minimum number of characters to make the password strong

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
