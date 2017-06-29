#!/bin/python

import sys

def solve(n, s, d, m):
    # Complete this function
    count = 0

    for  i in range(n-m + 1):
        #print sum(s[i:i+m])
        if sum(s[i:i+m]) == d:
            count += 1
    return count
n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
