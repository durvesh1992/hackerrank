import re

# make your own character clss
charClass = re.compile(r'[aeiou]')
matchobj = charClass.findall("My num is 669-264-9999 and 669-999-8888 call 12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids")
print matchobj

# negative of the defined character class
charClass = re.compile(r'[^aeiou]')
matchobj = charClass.findall("My num is 669-264-9999 and 669-999-8888 call 12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids")
print matchobj


