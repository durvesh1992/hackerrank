import re

#greedy match
haVal = re.compile(r'(ha){3,5}')
haobj = haVal.search("hahahaha")
print haobj.group()

haobj = haVal.search("hahaha")
print haobj.group()

haobj = haVal.search("hahahahaha")
print haobj.group()