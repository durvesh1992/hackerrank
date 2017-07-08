import re

charClass = re.compile(r'\d+\s\w+')
matchobj = charClass.findall("My num is 669-264-8414 and 669-999-8888 call 12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids")
print matchobj


