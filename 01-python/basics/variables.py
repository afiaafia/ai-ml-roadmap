# Python Variables
# ----------------
# A variable is a name used to store a value.
# Python does not require you to declare the variable type explicitly.


# 1. Creating variables

name = "Afia"
age = 20
height = 5.4
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# 2. Checking variable types

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# 3. Multiple variables

first_name, last_name = "Afia", "Mubassira"

print(first_name)
print(last_name)


# 4. Assigning the same value to multiple variables

x = y = z = 10

print(x)
print(y)
print(z)


# 5. Updating a variable

score = 80
print(score)

score = 90
print(score)


# 6. Variables can store different types of values

message = "Hello, Python!"
number = 100
price = 99.99
available = True

print(message)
print(number)
print(price)
print(available)


# 7. Variable naming

# Valid variable names:
student_name = "Afia"
student_age = 20
total_marks = 100

print(student_name)
print(student_age)
print(total_marks)


# Invalid examples (kept as comments):
# 2name = "Afia"       # Cannot start with a number
# student-name = "A"   # Hyphen is not allowed
# class = "Python"     # "class" is a Python keyword


# 8. Python uses snake_case by convention

user_name = "Afia"
total_score = 95
is_logged_in = True

print(user_name)
print(total_score)
print(is_logged_in)


# 9. Variables can be reassigned

language = "Python"
print(language)

language = "JavaScript"
print(language)


# 10. Basic calculation with variables

num1 = 10
num2 = 20

sum_result = num1 + num2
difference = num2 - num1
product = num1 * num2
division = num2 / num1

print(sum_result)
print(difference)
print(product)
print(division)
