# Week 0 Functions
# CS50 Introduction to Python
# 3/9/25

# Ask user for their name
# Remove whitespace from str and capitalize user's name
name = input("What's your name? ").strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

# Say hello to user
print(f"Hello, {first}") 

# Python print function documentation
# print(*objects, sep=' ', end = '\n', file=sys.stdout, flush = False)

# -------------------------------------------------------

# def = define | used to define functions
def main(): 
    name = input("What's your name? ")
    hello(name)

def hello(to="world"): 
    print("hello,", to)

main()
