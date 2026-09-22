# Sets in Python

# A set is an unordered collection of unique values.
numbers = {10, 20, 30, 40}

print(numbers)


# Duplicate values are automatically removed.
values = {10, 20, 20, 30, 30, 30}

print(values)


# Creating an empty set.
empty_set = set()

print(empty_set)
print(type(empty_set))


# Adding an element.
numbers.add(50)

print(numbers)


# Adding multiple elements.
numbers.update({60, 70, 80})

print(numbers)


# Removing an element using remove().
numbers.remove(80)

print(numbers)


# discard() does not raise an error if the value does not exist.
numbers.discard(100)

print(numbers)


# Checking whether an element exists.
print(20 in numbers)
print(100 in numbers)


# Set union.
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

union = set_a | set_b

print(union)


# Set intersection.
intersection = set_a & set_b

print(intersection)


# Set difference.
difference = set_a - set_b

print(difference)


# Symmetric difference.
symmetric_difference = set_a ^ set_b

print(symmetric_difference)


# Using set() to remove duplicates from a list.
numbers_with_duplicates = [10, 20, 10, 30, 20, 40]

unique_numbers = set(numbers_with_duplicates)

print(unique_numbers)


# Finding the number of unique elements.
print(len(unique_numbers))


# Sets are unordered and do not support indexing.
# The following would cause an error:
# print(numbers[0])
