#!/bin/python

import sys

def solve(grades):
    # Complete this function
#    print grades
    for i in range(len(grades)):            
        if grades[i] % 5 > 2 and grades[i] < 35 :
            continue
        elif grades[i] % 5 < 2 :
            continue
        elif grades[i] % 5 > 2 :
            if grades[i] > 35 and grades[i] < 40:
                grades[i] = 40
                continue
            grades[i] = grades[i] + (5 - grades[i] % 5)
            continue
    return grades
    
n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))


