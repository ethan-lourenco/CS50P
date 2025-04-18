# April 17th 2025

""" 
# First iteration

name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"hello, {name}")
"""

# Second iteration

import re
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name): # walrus operator := (can both assign value and ask boolean question)
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")