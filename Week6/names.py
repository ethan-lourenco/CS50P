# names.py

# BASIC
names = []

for _ in range(3):
	names.append(input("What's your name? "))

for name in sorted(names):
	print(f"hello, {name}")

	
# WRITE TO FILE
name = input("What's your name? ")

with open("names.txt", "a") as file: # a == append, w == write
	file.write(f"{name}\n") 


# READ SORTED NAMES FROM FILE
names = []

with open("names.txt") as file: # r == read is the default
	for line in sorted(file):
		print("hello,", line.rstrip())