#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here
    #print s
    mystr = "hackerrank"
    j = 0
    for i in range(len(s)):
        
        if  j < len(mystr) and s[i] == mystr[j]:
            j += 1

    if j == len(mystr):
        print "YES"
    else:
        print "NO"
        