#!/bin/python3
# Used Bellman-Ford Shortest Path Algorithm
import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    edges = []
    n = len(c)
    
    for i,each in enumerate(c):
        if i+1<n and c[i+1] == 0:
            edges.append((i,i+1,1))
        if i+2<n and c[i+2] == 0:
            edges.append((i,i+2,1))
    
    dist = [2e10]*n
    dist[0] = 0
    
    for i in range(n-1):
        for each in edges:
            a,b,w = each
            dist[b] = min(dist[b],dist[a]+w)
            
    return dist[n-1]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
