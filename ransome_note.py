#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    found = defaultdict(int)
    
    for each in magazine:
        found[each] += 1
    
    for each in note:
        if (not each in found) or found[each] == 0:
            print('No')
            return
        else:
            found[each] -= 1
        
    print('Yes')

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
