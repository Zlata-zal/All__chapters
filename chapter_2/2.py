km = float(input("Enter distance in kilometers: "))
m = float(input("Enter distance in meters: "))

km_in_meters = km * 1000

if km_in_meters < m:
    print(f"The smallest distance is {km_in_meters} meters (converted from kilometers)")
else:
    print(f"The smallest distance is {m} meters")