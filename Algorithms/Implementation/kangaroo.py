#!/bin/python

import sys


x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

if x2 > x1 and v2 > v1 :
    print "NO"
elif x2 < x1 and v2 < v1:
    print "NO"
else:
    if((v1!=v2) and ((x2-x1)%(v1-v2))==0):
        print "YES"
    else:
        print "NO"
#while x1 != x2:
#    x1 += v1
#    x2 += v2
#    if x1 == x2:
#        print "YES"
#        break