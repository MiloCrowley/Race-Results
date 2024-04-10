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
    print(f"in second place was {names[secondlow_time]} "
          f"(The difference was {secondlow_sec - low_sec} seconds)")


def add_Race(course):
    runners = open("Runners.txt")
    with open("Races.txt", "a") as h:
        h.write(f"\n{course}")
    names = []
    times = []
    for line in runners:
        line_data = line.split(",")
        name = line_data[0]
        names.append(name)
        time = int(input(f"Time for {name} >> "))
        times.append(time)
    with open(f'{course}.txt', 'w') as f:
        for i, time in enumerate(times):
            if time > 0:
                f.write(f"{names[i]},{time}\n")
            else:
                print()

def get_List():
    runners = open("Runners.txt")
    names = []
    counties = []
    years = []
    currentyear = 2024
    count = 0
    count_ = 0
    for line in runners:
        line_data = line.split(",")
        name = names.append(line_data[0])
        county = counties.append(line_data[1])
        year = years.append(line_data[2])
    for num in counties:
        if num == "CK":
            count += 1
    print(f"Cork Runners ({count})")
    print("-------------------")
    for i, county_ in enumerate(counties):
        if county_ == "CK":
            age = currentyear - int(years[i])
            print(f"{names[i]}    {age}")
    for num in counties:
        if num == "KY":
            count_ += 1

    print(f"\nKerry Runners ({count_})")
    print("-------------------")
    for i, county_ in enumerate(counties):
        if county_ == "KY":
            age = currentyear - int(years[i])
            print(f"{names[i]}    {age}")

while True:
    menu = int(input("\n1. Show the results of a race\n2. Add the results for a race"
              "\n3. Show a list of competitors by County (show age)\n>>> "))
    if menu == 1:
        Courses = []
        count__ = 1
        races = open("Races.txt")
        for line in races:
            line_data = line.strip()
            Courses.append(line_data)
            print(f"{count__}. {line_data}")
            count__ += 1
        menu_1 = int(input("Choose a race:"))
        if menu_1 in range(1,999):
            print_Race(f"{Courses[menu_1 - 1]}.txt")

    elif menu == 2:
        course = input("Enter location\n>>> ")
        add_Race(course)
    elif menu == 3:
        get_List()