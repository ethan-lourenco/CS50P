x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(f"{z:,}")

# ---------------------------------------------

def main(): 
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n
    
main()