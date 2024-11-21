sea_fish = ["shark", "flounder", "tuna", "cod", "herring", "Marlin"]
freshwater_fish = ["Asp", "Pike", "Carp", "Salmon", "Ide", "Trout"]

all_fish = sea_fish + freshwater_fish
print(sorted(all_fish,key=str.lower))
