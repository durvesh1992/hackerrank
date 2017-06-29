# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
#print n

for a0 in xrange(n):
    s = raw_input().strip()
    flag = 0
    #print s
    j = len(s) - 1
    for i in range(len(s) - 1):
        #print abs(ord(s[i+1]) - ord(s[i]))
        #print abs(ord(s[j-1]) - ord(s[j]))
        if abs(ord(s[i+1]) - ord(s[i])) != abs(ord(s[j-1]) - ord(s[j])):
            print "Not Funny"
            flag = 1
            break
        j -= 1
    if flag == 0:
        print "Funny"
    
    #print "val of i ",i
#            if i == len(s) - 1
##        print ord(s[i+1]) - ord(s[i])
#        print ord(s[j-1]) - ord(s[j])
#        j -= 1