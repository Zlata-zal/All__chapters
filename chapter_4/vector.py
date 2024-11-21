def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def cross_product(a, b):
    cx = a[1] * b[2] - a[2] * b[1]
    cy = a[2] * b[0] - a[0] * b[2]
    cz = a[0] * b[1] - a[1] * b[0]
    return [cx, cy, cz]

def scalar_product(a, b, c):
    return dot_product(a, cross_product(b, c))

def vector_product(a, b, c):
    return cross_product(a, cross_product(b, c))

a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

print("Скалярное произведение a · b:", dot_product(a, b))
print("Векторное произведение a × b:", cross_product(a, b))
print("Скалярное смешанное произведение a · (b × c):", scalar_triple_product(a, b, c))
print("Векторное смешанное произведение a × (b × c):", vector_triple_product(a, b, c))