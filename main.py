import math


# Function that enforces each line list within the entire list should have at less 3 values
def format_all_lines(lines_list):
    for i in range(len(lines_list)):
        assert type(lines_list[i]) is list
        # Check if the single line list has less than 3 values
        if len(lines_list[i]) < 3:
            # Add zero where an element or elements is missing
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

    return round(upper_side / math.sqrt(lower_side), 2)

# Sample array that will be created
# physics = [0, 76, 76, 95, 96, 79, 74, 97, 97, 90, 90, 78, 91, 76, 90, 95, 95, 75, 100, 87, 90]
# chemistry = [0, 72, 67, 92, 95, 59, 58, 95, 94, 84, 83, 70, 79, 67, 73, 87, 86, 63, 92, 80, 76]
# maths = [20, 73, 48, 95, 95, 33, 47, 98, 91, 95, 93, 70, 85, 33, 47, 95, 84, 43, 95, 54, 72]

# Get the data from the input
with open("data.dat") as data:
    # Loop to get the data
    lines = [line.split() for line in data]
    # Remove empty lists
    lines = filter(None, lines)

# Log
print "The lines list is: ", lines

# Make sure the a single line has no less than 3 values
lines = format_all_lines(lines)

# Log
print "The new lines list is: ", lines

# Get the first 3 rows required
maths = [handle_value(row[0]) for row in lines]
chemistry = [handle_value(row[1]) for row in lines]
physics = [handle_value(row[2]) for row in lines]

print "Maths list is: ", maths, "\n Chemistry list is: ", chemistry,\
    "\n Physics list is: ", physics, "\n"

print pearson_coefficient(maths, physics)
print pearson_coefficient(physics, chemistry)
print pearson_coefficient(chemistry, maths)