#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#
def binary_search_lower_upper(arr,val,n):
    s = 0
    e = n - 1
    
    if val >= arr[s]:
        return 0
    if val <= arr[e]:
        return e
    
    while(s<=e):
        mid = (s+e) // 2
        
        if arr[mid] == val:
            return mid
        elif arr[mid]>val:
            s = mid + 1
        else:
            e = mid - 1
            
    return s-1,e+1

def climbingLeaderboard(scores, player):
    rank = 0
    prev = -1
    ranks = []
    queries = []
    n = len(scores)
    for each in scores:
        if each!=prev:
            ranks.append(rank+1)
            rank += 1
            prev = each
        else:
            ranks.append(rank)
            prev = each
    
    for each in player:
        val = binary_search_lower_upper(scores,each,n)
        
        if type(val) == tuple:
            lower = scores[val[1]]
            upper = scores[val[0]]
            
            queries.append(ranks[val[0]+1])
            
        else:
            if val == 0:
                queries.append(1)
            elif val == n - 1:
                if each == scores[val]:
                    queries.append(ranks[-1])
                else:
                    queries.append(ranks[-1]+1)
            else:
                queries.append(ranks[val])    
    
    return queries
                
    
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
