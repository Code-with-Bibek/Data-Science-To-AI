'''
Program 2 — Temperature Analyzer

Ask the user to enter temperatures for 7 days.

Then determine:

Average temperature
Highest temperature
Lowest temperature
Standard deviation

Then use a Python if statement:

If average > 30:
    "It was a hot week"
else:
    "It was not a hot week"

Notice the combination:

NumPy calculates → Python makes the decision.
'''

# It has asked for 7 days, so we will use a loop 7 times
# rather than asking the user how many days to enter.

import numpy as np

temp_in_list = []

for i in range(7):
    temp = int(input(f"Enter the temperature of day {i + 1}: "))
    temp_in_list.append(temp)

print(temp_in_list)

# Convert Python list into NumPy array
temp_array = np.array(temp_in_list)

# NumPy calculations
average_temp = np.mean(temp_array)
highest_temp = np.max(temp_array)
lowest_temp = np.min(temp_array)
standard_deviation = np.std(temp_array)

# Display results
print("The average temperature is:", average_temp)
print("The highest temperature is:", highest_temp)
print("The lowest temperature is:", lowest_temp)
print("The standard deviation is:", standard_deviation)

# Python makes the decision
if average_temp > 30:
    print("It was a hot week")
else:
    print("It was not a hot week")
