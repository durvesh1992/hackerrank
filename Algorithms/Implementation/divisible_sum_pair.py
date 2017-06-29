#!/bin/python

import sys

n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int, raw_input().strip().split(' '))
# write your code here
#print n
#print a
count = 0
for i in range(n-1):
    for j in range(i+1, n):
        if (i < j) and ((a[i] + a[j]) % k == 0):
            #print a[i],a[j]
            count += 1
print count
    