import math

def tetration(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x ** tetration(x, n - 1)

tetration_3_5 = tetration(3, 5)
tetration_5_2 = tetration(5, 2)

print("3^5 (тетрация):", tetration_3_5)
print("5^2 (тетрация):", tetration_5_2)

print("Количество цифр в 3^5:", len(str(tetration_3_5)))
print("Количество цифр в 5^2:", len(str(tetration_5_2)))
