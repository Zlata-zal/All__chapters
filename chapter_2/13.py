import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))

current_year = datetime.datetime.now().year
year_at_100 = current_year + (100 - age)

print(f"Hello, {name}. You will turn 100 years old in the year {year_at_100}.")