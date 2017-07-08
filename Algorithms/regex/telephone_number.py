import re

phoneNum = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matchobj = phoneNum.search("My num is 669-264-8414")
print matchobj.group()

phoneNum = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
matchobj = phoneNum.search("My num is 6692648414")
print matchobj.group()

phoneNum = re.compile(r'\d\d\d\d\d\d\d\d\d\d')
matchobj = phoneNum.search("My num is 6692648417 and 6692648414")
print matchobj.group()