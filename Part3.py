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
