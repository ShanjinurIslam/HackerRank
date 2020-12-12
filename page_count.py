#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n == 1:
        return 0
    else:
        arr = [(1,1)]
        for i in range(2,n,2):
            arr.append((i,i+1))
            
        if n%2 == 0:
            arr.append((n,n))
            
        print(arr)
        
        forward = 0
        
        for i in arr:
            if p in i:
                break
            forward += 1
        
        backward = 0
        
        
        for i in arr[::-1]:
            if p in i:
                break
            backward += 1
            
        return min(forward,backward)
        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
