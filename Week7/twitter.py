# April 17th 2025

"""
# First iteration

url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/", "")
print(f"Username: {username}") 

# Second iteration

import re

url = input("URL: ").strip()

username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
print(f"Username: {username}") 
"""

# Third iteration

import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))