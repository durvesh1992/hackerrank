#!/bin/python

import sys

n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))
# your code goes here
d = {}
#d = d.fromkeys(types, 0)
for typ in types:
    d[typ] = d.get(typ, 0) + 1
#    print d
    
#print max(bird_count, key=lambda x: bird_count[x])
print max(d, key =d.get)
