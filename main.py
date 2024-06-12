mission_names = ['Apollo 11', 'Challenger', 'Curiosity Rover', 'Viking 1', 'Mars Pathfinder', 'Hubble Telescope', 'Apollo 13']
mission_years = [1969, 1986, 2012, 1975, 1996, 1990, 1970]
mission_success = [True, False, True, True, True, True, False]

total_missions = 0
for mission in mission_names:
    total_missions += 1
print("Total number of missions:", total_missions)


success_count = 0
for success in mission_success:
    if success:
        success_count += 1
print("Number of successful missions:", success_count)

success_rate = 0
for success in mission_success:
    if success:
        success_rate += 1

success_rate = (success_rate / total_missions) * 100

print("Success rate: {:.2f}%".format(success_rate))

for i in range(len(mission_names)):
    if mission_years[i] < 2000:
        print("-", mission_names[i])

