# Enter your code here. Read input from STDIN. Print output to STDOUT
s = raw_input("")
#tmp = s
#x = ""
i = 0
#s = "lrfkqyuqfjjfquyqkfrlkxyqvnrtyssytrnvqyxkfrzrmzlygffgylzmrzrfveulqfpdbhhbdpfqluevlqdqrrcrwddwrcrrqdql"
#s = "aaabccddd"

while (i < len(s)-1):
    if s[i] == s[i+1]:
        s = s[:i] + s[i+2:]
        i = 0
        continue
    i += 1

if len(s) == 2 and (s[:] ==s[::-1]):
    s = ""

if len(s) == 0:
    print "Empty String"
else:
    print s