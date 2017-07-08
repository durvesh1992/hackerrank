import re

optionalVal = re.compile(r'Tanmay | Giga(wo)?(man)')
optionalObj = optionalVal.search("Tanmaya and Gigaman is a good combo")

# will  print gigaman
print optionalObj.group()

pipeVal = re.compile(r'Giga(wo)?(mon|man|can|dan|fan)')
pipeObj = pipeVal.search("Gigac-anada delicacy and Gigawomon")
print pipeObj.group()