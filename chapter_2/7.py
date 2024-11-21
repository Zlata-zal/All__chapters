import math

radius = float(input("Enter the radius of the circle: "))
diameter = 2 * radius
print(f"The diameter of the circle is: {diameter}")

sum_100_to_500 = sum(range(100, 501))
print(f"Sum of all integers from 100 to 500: {sum_100_to_500}")

a = int(input("Enter a number less than 500: "))
if a < 500:
    sum_a_to_500 = sum(range(a, 501))
    print(f"Sum of all integers from {a} to 500: {sum_a_to_500}")
else:
    print("Number must be less than 500.")