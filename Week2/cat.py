# Week 2 Loops
# 3/13/25

def main():
    number = get_number()
    meow(number)
   

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0: 
            return n
        

def meow(n):
    for _ in range(n):
        print("meow")

main()

# ------------------------------------------------------

while True: 
    n = int(input("What's n? "))
    if n > 0: 
        break

for _ in range(n):
    print("meow")

# ------------------------------------------------------

# _ signals that the variable isn't used later in code
for _ in range(3):
    print("meow")

print("meow\n" * 3, end="")

i = 0
while i < 3:
    print("meow")
    i += 1