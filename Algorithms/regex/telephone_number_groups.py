import re
phoneNum = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchobj = phoneNum.search("My num is 669-264-8414")
print matchobj.group()
print matchobj.group(1)
print matchobj.group(2)
