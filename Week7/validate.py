# April 17th 2025

"""
# First iteration

email = input("What's your email? ").strip()

if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")

# Second iteration

email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
"""

# Third iteration

# re patterns

# .      any character except a newline
# *      0 or more repetitions
# +      1 or more repetitions
# ?      0 or 1 repetition
# {m}    m repetitions
# {m,n}  m-n repetitions

# ^      matches the start of the string
# $      matches the end of the string just before
#        the newline at the end of the string

# []     set of characters
# [^]    complementing the set

# \d     decimal digit
# \D     decimal not a decimal digit
# \s     whitespace characters
# \S     not a whitespace character
# \w     word character and numbers/underscore
# \W     not a word character

# re flags
# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

import re

email = input("What's your email? ").strip()

if re.fullmatch(r"[a-z0-9_\.]+@(\w+\.)?\w+\.(edu|com|gov|org|net)", email, re.IGNORECASE): # r - raw string passed exactly as is
    print("Valid")
else:
    print("Invalid")

