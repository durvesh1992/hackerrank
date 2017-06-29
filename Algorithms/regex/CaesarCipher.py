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