#!/bin/python

import sys

n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
# your code goes here
d = {}
for typ in types:
    d[typ] = d.get(typ, 0) + 1
    
print max(d, key =d.get)
