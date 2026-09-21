# Python Data Types
# -----------------
# Python has several built-in data types for storing different kinds of values.


# 1. Integer
age = 20
year = 2026

print(age)
print(type(age))


# 2. Float
height = 5.4
price = 99.99

print(height)
print(type(height))


# 3. Complex number
complex_number = 3 + 4j

print(complex_number)
print(type(complex_number))


# 4. String
name = "Afia"
message = "Learning Python for AI and Machine Learning"

print(name)
print(type(name))


# 5. Boolean
is_student = True
is_completed = False

print(is_student)
print(type(is_student))


# 6. List
languages = ["Python", "JavaScript", "TypeScript"]

print(languages)
print(type(languages))


# 7. Tuple
coordinates = (23.8103, 90.4125)

print(coordinates)
print(type(coordinates))


# 8. Set
unique_numbers = {1, 2, 3, 4, 5}

print(unique_numbers)
print(type(unique_numbers))


# 9. Dictionary
student = {
    "name": "Afia",
    "age": 20,
    "course": "AI & Machine Learning"
}

print(student)
print(type(student))


# 10. None
result = None

print(result)
print(type(result))


# 11. Checking multiple data types

values = [
    100,
    10.5,
    "Python",
    True,
    [1, 2, 3],
    (1, 2, 3),
    {1, 2, 3},
    {"name": "Afia"},
    None
]

for value in values:
    print(value, "->", type(value))
