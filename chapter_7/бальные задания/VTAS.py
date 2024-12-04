from datetime import timedelta

def parse_time(time_str):
    if len(time_str) < 4 or not time_str.isdigit():
        raise ValueError(f"Invalid time format: {time_str}")
    hour = int(time_str[:-2])
    minute = int(time_str[-2:])
    return timedelta(hours=hour, minutes=minute)

def format_time(timedelta_obj):
    total_minutes = int(timedelta_obj.total_seconds() // 60)
    hours = total_minutes // 60
    minutes = total_minutes % 60
    return f"{hours:02}{minutes:02}"

def vtas(input_data):
    lines = input_data.split("\n")
    n_points = int(lines[0])
    waypoints = list(lines[1])
    distances = []

    for i in range(2, 2 + n_points):
        distances.append(list(map(float, lines[i].split())))

    traffic = []
    i = 2 + n_points
    while i < len(lines) and lines[i] != "*****":
        name = lines[i]
        time_speed = lines[i + 1].split()

        if len(time_speed) < 2:
            raise ValueError(f"Missing time or speed in line: {lines[i + 1]}")

        start_time = parse_time(time_speed[0])
        speed = float(time_speed[1])
        route = lines[i + 2]
        traffic.append({"name": name, "start_time": start_time, "speed": speed, "route": route})
        i += 3

    results = []
    for vessel in traffic:
        name = vessel["name"]
        start_time = vessel["start_time"]
        speed = vessel["speed"]
        route = vessel["route"]

        invalid_route = False
        arrival_times = []
        time = start_time

        for j in range(len(route) - 1):
            if route[j] not in waypoints or route[j + 1] not in waypoints:
                invalid_route = True
                break

            wp_from = waypoints.index(route[j])
            wp_to = waypoints.index(route[j + 1])
            distance = distances[wp_from][wp_to]

            if distance == 0:
                invalid_route = True
                break

            travel_time = distance / speed
            travel_time_minutes = travel_time * 60
            time += timedelta(minutes=travel_time_minutes)
            arrival_times.append((route[j + 1], time))

        result = f"Ship: {name}\n"
        result += f"Enter time: {format_time(start_time)}, Speed: {speed} knots\n"
        if invalid_route:
            result += "Invalid route detected.\n"
        else:
            result += "Route:\n"
            for wp, t in arrival_times:
                result += f"{wp}: {format_time(t)}\n"

        results.append(result)

    for res in results:
        print(res)


input_data = """6
ABCDEF
0 3 0 0 0 0
3 0 0 2 0 0
0 3 0 0 0 0
0 0 0 0 3 0
0 0 2 0 0 4
0 0 0 0 4 0
Tug
2330 12
ABDEF
WhiteSailboat
2345 6
ECBDE
TugWBarge
2355 5
DECBA
PowerCruiser
0 15
FECBA
LiberianFreighter
7 18
ABDXF
ChineseJunk
45 8
ACEF
*****"""

vtas(input_data)

