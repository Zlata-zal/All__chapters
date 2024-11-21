def parse_shark_data(file_path):
    sharks = {}
    current_family = None
    current_genus = None

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.endswith(':'):
                current_family = line[:-1]
                sharks[current_family] = {}
                current_genus = None

            elif line.startswith('    '):
                species, common_name = line.split(': ')
                sharks[current_family][current_genus][species] = common_name

            elif line.startswith('  '):
                current_genus = line.strip()
                sharks[current_family][current_genus] = {}

    return sharks



shark_data = parse_shark_data('data/shark-species.txt')

print(shark_data['Lamniformes']['Lamnidae']['Carcharodon']['C. carcharias'])
