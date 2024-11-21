def get_fragrances(flowers):
    return [combo for r in range(1, len(flowers) + 1) for combo in combinations(flowers, r)]

flowers_set1 = {"rose", "jasmine", "lily"}
flowers_set2 = {"orchid", "tulip", "violet", "daisy"}
flowers_set3 = {"lavender", "sunflower"}

print(get_fragrances(flowers_set1))
print(get_fragrances(flowers_set2))
print(get_fragrances(flowers_set3))