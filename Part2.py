course = input("Enter location\n>>> ")
runners = open("Runners.txt")
names = []
times = []
for line in runners:
    line_data = line.split(",")
    name = line_data[0]
    names.append(name)
    time = int(input(f"Time for {name} >> "))
    times.append(time)
print(names)
print(times)
with open(f'{course}.txt', 'w') as f:
    for i, time in enumerate(times):
        if time > 0:
            f.write(f"{names[i]},{time}\n")
        else:
            print()
