#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
d = {}
d = d.fromkeys(c,0)

for i in range(n):
    if d[c[i]] > 0:
        continue
    d[c[i]] = c.count(c[i])
#print d

count = 0
for keys in d:
    count += d[keys] / 2
print count