# Tuples in Python

# A tuple is an ordered and immutable collection.
coordinates = (10, 20)

print(coordinates)


# Accessing tuple elements using indexing.
print(coordinates[0])
print(coordinates[1])


# Negative indexing.
colors = ("Red", "Green", "Blue")

print(colors[-1])


# Tuple slicing.
numbers = (10, 20, 30, 40, 50)

print(numbers[1:4])
print(numbers[:3])
print(numbers[2:])


# Tuples can contain different data types.
student_data = ("Alex", 25, 3.75, True)

print(student_data)


# Tuple unpacking.
point = (100, 200)

x, y = point

print(x)
print(y)


# Multiple assignment is based on tuple unpacking.
first, second, third = "Python", "JavaScript", "TypeScript"

print(first)
print(second)
print(third)


# Counting occurrences of a value.
values = (10, 20, 10, 30, 10)

print(values.count(10))


# Finding the position of a value.
print(values.index(30))


# Checking whether a value exists.
print(20 in values)
print(50 in values)


# Finding the number of elements.
print(len(values))


# Tuples are immutable.
# The following would cause a TypeError:
# colors[0] = "Yellow"


# A single-element tuple requires a trailing comma.
single_value = ("Python",)

print(single_value)
print(type(single_value))
