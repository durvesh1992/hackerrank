import re

#greedy match
haVal = re.compile(r'(ha){3,5}')
haobj = haVal.search("hahahaha")
print haobj.group()

haobj = haVal.search("hahaha")
print haobj.group()

haobj = haVal.search("hahahahaha")
print haobj.group()

#Non greedy match
haVal = re.compile(r'(ha){3,5}?')
haObj = haVal.search("hahahaha")

#will print only 3 hahaha
print "Non greedy approac..choose minimum number of 'ha'"
print haObj.group()