#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    # your code goes here
    
    flag = 'NO'
    digit = ''
    for i in range(0, len(s)//2):

        digit = digit + (s[i])
        series = ''

        for j in range(len(s)//(i+1)):
            if j == 0:
                series = series + digit
            elif len(series) <= (len(s)-i):
                series = series + str(int(digit)+j)

            if s == series:
                flag = 'YES ' + s[:i+1]

    print flag