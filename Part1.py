def print_Race(place):
    races = open(place)
    names = []
    times = []
    for line in races:
        line_data = line.split(",")
        name = line_data[0]
        time = int(line_data[1])
        names.append(line_data[0])
        times.append(int(line_data[1]))
        mins = time // 60
        secs = time % 60
        print(f"{name} {mins}min {secs}seconds")
    low_time = times.index(min(times))
    low_sec = min(times)
    print(f"\nThe winner was {names[low_time]}.")
    times.remove(min(times))
    secondlow_time = times.index(min(times))
    secondlow_sec = min(times)
    print(f"in second place was {names[secondlow_time]} (The difference was {secondlow_sec - low_sec} seconds)")

print_Race("glengarriff.txt")