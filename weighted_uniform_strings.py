#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

def weightedUniformStrings(s, queries):
    char_weight = dict()
    for i in range(26):
        char_weight[chr(97+i)] = i+1

    U = dict()
    
    prev = s[0]
    weight = char_weight[prev]
    count = 1
    n = len(s)
    
    if n == 1:
        U[weight] = 1
    
    for i in range(1,n):
        if s[i] == s[i-1] and i!=n-1:
            U[weight*count] = 1
            count += 1
        elif s[i] == s[i-1] and i == n-1:
            U[weight*(count+1)] = 1
            break
        else:
            U[weight*count] = 1
            prev = s[i]
            weight = char_weight[prev]
            count = 1
            
            if i == n-1:
                U[weight*count] = 1
            
    result = ""
    for each in queries:
        if each in U:
            result += "Yes\n"
        else:
            result += "No\n"
            
    return result

if __name__ == '__main__':

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)
    print(result[:-1])