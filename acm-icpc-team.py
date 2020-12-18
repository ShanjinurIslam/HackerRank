#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations
from collections import defaultdict

def acmTeam(topic):
    pairs = combinations(list(range(0,len(topic))), 2)
    found = defaultdict(int)
    
    for each in pairs:
        m1 = each[0]
        m2 = each[1]
        b1 = int(topic[m1],2)
        b2 = int(topic[m2],2)
        found[bin(b1 | b2).count('1')] += 1
        
    max_val = max(found.keys())
    
    return max_val,found[max_val]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
