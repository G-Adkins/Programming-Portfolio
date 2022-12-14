# Make the variables
num_runners = 0
total_time = 0
fastest_time = float("inf")
slowest_time = 0

# dictionary to store all runners data
runners_dict = {}

# Loop until all runners have been seen
while True:
    # Get input from user
    try:
        runner = input("> ")
        if runner.upper() == 'END':
            break
        runner = runner.split("::")
        if len(runner) != 2:
            raise ValueError
        # Update total number of runners and total time
        total_time += int(runner[1])

        # Update dictionary, if runner time is re input it will overload the data already stored
        runners_dict[runner[0]] = runner[1]

    except ValueError:
        print('Error. Error Ignored.')
        continue
# check if any runners have been entered

num_runners = len(runners_dict)

if num_runners == 0:
    exit()

# adds all the times to the list to get fastest, slowest and average times
runners_time = []
for runner in runners_dict:
    runners_time.append(float(runners_dict[runner]))

sorted_runners = sorted(runners_time)

# Calculate average, fastest and slowest times
average_time = total_time / num_runners
slowest_time = float(sorted_runners[len(runners_time) - 1])
fastest_time = float(sorted_runners[0])
# Checks for the fastest time
fastest_runners = []
for runner in runners_dict:
    if fastest_time == float(runners_dict[runner]):
        fastest_runners.append(runner)

# Convert times to minutes and seconds
fastest_minutes = fastest_time // 60
fastest_seconds = fastest_time % 60
slowest_minutes = slowest_time // 60
slowest_seconds = slowest_time % 60
average_minutes = average_time // 60
average_seconds = average_time % 60

# Print results
print("Total number of runners:", num_runners)
print("Average time: %d minutes %d seconds" % (average_minutes, average_seconds))
print("Fastest time: %d minutes %d seconds" % (fastest_minutes, fastest_seconds))
print("Slowest time: %d minutes %d seconds" % (slowest_minutes, slowest_seconds))

print("Best Time(s) Here: #" + (" #".join(fastest_runners)))
