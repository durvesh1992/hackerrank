# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
q = raw_input().strip()

#q = "We promptly judged antique ivory buckles for the prize"
q = q.lower()

d = dict.fromkeys(string.ascii_lowercase, 0)
#print d

for i in range(len(q)):
    if q[i] == " ":
        continue
    d[q[i]] += 1

values = d.values()
if 0 in values:
    print "not pangram"
else:
    print "pangram"
