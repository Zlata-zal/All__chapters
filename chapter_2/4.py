a = int(input("Enter number a: "))
b = int(input("Enter number b: "))

if b % a == 0:
    print(f"{a} is a divisor of {b}")
else:
    print(f"{a} is not a divisor of {b}")