import re

phoneNum = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matchobj = phoneNum.findall("My num is 669-264-8414 and 669-999-8888")
print matchobj


