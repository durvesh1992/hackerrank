# Enter your code here. Read input from STDIN. Print output to STDOUT
n = map(int,raw_input().strip().split(' '))
#print n

costList = map(int,raw_input().strip().split(' '))
#print costList

amountCharged = int(raw_input())
#print amountCharged

dinnerCost = sum(costList)- costList[n[1]]
#print dinnerCost

perPerson = dinnerCost / 2

if amountCharged == perPerson:
    print "Bon Appetit"
else:
    print (amountCharged - perPerson )
