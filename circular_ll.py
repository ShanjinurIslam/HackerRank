#!/bin/python3

import math
import os
import random
import re
import sys

class ListNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def circularArrayRotation(a, k, queries):
    head = None
    tail = head

    reference = dict()

    for i,each in enumerate(a):
        if head == None:
            head = ListNode(each)
            tail = head
            reference[i] = head
        else:
            tail.next = ListNode(each)
            tail = tail.next
            reference[i] = tail
    
    tail.next = head

    n = len(a)

    if n>=k:
        start = n-k
    else:
        k = k%n
        start = n-k

    for query in queries:
        p = reference[start]
        i = 0
        while(i<query):
            p = p.next
            i += 1
        print(p.val)

if __name__ == '__main__':
    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    circularArrayRotation(a, k, queries)

    
