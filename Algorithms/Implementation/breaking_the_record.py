#!/bin/python

import sys

def getRecord(s):
    # Complete this function
    maxi = s[0]
    mini = s[0]
    maxCount = 0
    miniCount = 0
    for i in range(1, len(s)):
        if s[i] > maxi:
            maxi = s[i]
            maxCount += 1
        if s[i] < mini:
            mini = s[i]
            miniCount += 1
    print maxCount, miniCount
    

n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
result = getRecord(s)
print " ".join(map(str, result))
