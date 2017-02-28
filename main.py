import math
# import sys


# Function that enforces each line list within the entire list should have at least 3 values
# This handles situations that data is not present such as chemistry marks are not present
def format_all_lines(lines_list):
    for i in range(len(lines_list)):
        assert type(lines_list[i]) is list
        # Check if the single line list has less than 3 values
        if len(lines_list[i]) < 3:
            # Add zero where an element or elements is/are missing
            for _ in range(3 - len(lines_list[i])):
                lines_list[i].append("0")

    return lines_list


# Function to check if the value passed is null or greater than 100
def handle_value(val):
    try:
        assert val
        new_value = int(val)
    except:
        return 0
    if new_value < 0:
        return 0
    elif new_value > 100:
        return 100
    return new_value


# Function to calculate the pearson correlation coefficient and round off to two decimal points
def pearson_coefficient(x, y):
    # Check if the length is the same
    assert len(x) == len(y)
    # Get the length
    length = len(x)
    # Calculate the xy list pairing
    xy = [x_value * y_value for x_value, y_value in zip(x, y)]
    # Calculate the power of each value in the list x, y
    pow_x = [pow(i, 2) for i in x]
    pow_y = [pow(i, 2) for i in y]
    # Calculate the sum of the list
    sum_xy = sum(xy)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_pow_x = sum(pow_x)
    sum_pow_y = sum(pow_y)

    # Perform the calculation
    upper_side = (length * sum_xy) - (sum_x * sum_y)
    lower_side = ((length * sum_pow_x) - pow(sum_x, 2)) * ((length * sum_pow_y) - pow(sum_y, 2))

    # Account for any zero division errors
    assert upper_side != 0
    assert lower_side != 0

    return round(upper_side / math.sqrt(lower_side), 2)

# Get the data from the input

# Uncomment this if you are running from hacker rank / Reading from input
# data = sys.stdin.readlines()

# Comment this if you are running from hacker rank / Reading from the data.dat file
with open("data.dat") as data:
    # Loop to get the data
    lines = [line.split() for line in data]

# Removing the first line that is the number of students
lines.pop(0)

# Make sure the a single line has no less than 3 values. i.e maths, chemistry, physics
lines = format_all_lines(lines)

# Get the first 3 rows required
maths = [handle_value(row[0]) for row in lines]
physics = [handle_value(row[1]) for row in lines]
chemistry = [handle_value(row[2]) for row in lines]

# print("Maths list is: ", maths, "\n Chemistry list is: ", chemistry,
#       "\n Physics list is: ", physics, "\n")

print(pearson_coefficient(maths, physics))
print(pearson_coefficient(physics, chemistry))
print(pearson_coefficient(chemistry, maths))
