import re

# Split on space
line = "here are some words"
print re.split(r'\s', line)

# Split on space for all the line
line = "here are some words"
print re.split(r'(\s*)', line)

# Split on space for all the line and include the line as well
line = "here are some words"
print re.split(r'(s*)', line)

# Split on alphabets in range a-f
line = "here are some words"
print re.split(r'[a-f]', line)

# Split on alphabets in range a-f
line = "here are some words"
print re.split(r'[a-fA-Z0-9]', line)


# Multiline or ignore case
line = "Here are some words"
print re.split(r'[a-f]', line, re.I | re.M)

# digits
line = "Here are some words0987"
print re.findall(r'\d', line, re.I | re.M)

# non digits
line = "Here are some words0987"
print re.findall(r'\D', line, re.I | re.M)

# get number from string
line = "ocinwe324 main st. words0987"
print re.findall(r'\d{1,9}', line)

# address
line = "ocinwe324 main st. words0987"
print re.findall(r'\d{1,9}\s\w+\s\w+\.', line)
