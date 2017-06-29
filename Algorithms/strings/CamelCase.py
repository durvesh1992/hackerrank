#!/bin/python

import sys


s = raw_input().strip()
count = 0
for i in range(len(s)):
#    print ord(s[i])
    if ord(s[i]) >= 65 and ord(s[i]) < 97:
        count += 1
count += 1
print count 