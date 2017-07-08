import re

pipeVal = re.compile(r'Tanmay | Gigamon')
pipeObj = pipeVal.search("Tanmay and Gigamon is a good combo")

print pipeObj.group()

pipeVal = re.compile(r'Giga(mon|man|can|dan|fan)')
pipeObj = pipeVal.search("Gigacan delicacy and Gigamon")
print pipeObj.group(1)