# F-Strings in Python

# F-strings provide a convenient way to insert variables
# and expressions inside a string.

product = "Notebook"
price = 49.99

message = f"The {product} costs ${price}."

print(message)


# Multiple variables can be used in one f-string.
quantity = 3
total = price * quantity

summary = f"Product: {product}, Quantity: {quantity}, Total: ${total}"

print(summary)


# Expressions can be written directly inside an f-string.
length = 10
width = 5

area = f"The area is {length * width} square units."

print(area)


# Different data types can be used.
item = "Keyboard"
quantity = 2
available = True

print(f"Item: {item}")
print(f"Quantity: {quantity}")
print(f"Available: {available}")


# Number formatting
amount = 1234.5678

print(f"Amount: {amount:.2f}")


# Percentage formatting
score = 0.875

print(f"Score: {score:.1%}")


# F-strings can make output easier to read.
name = "Alex"
score = 92

print(f"{name} scored {score} marks.")


# F-strings can contain calculations.
first_number = 20
second_number = 8

print(f"Sum: {first_number + second_number}")
print(f"Difference: {first_number - second_number}")
print(f"Product: {first_number * second_number}")
print(f"Division: {first_number / second_number}")
