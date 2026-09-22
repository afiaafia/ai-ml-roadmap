# Type Casting in Python

# Type casting means converting a value from one data type to another.


# Converting an integer to a float
number = 10
decimal_number = float(number)

print(decimal_number)
print(type(decimal_number))


# Converting a float to an integer
price = 99.99
whole_price = int(price)

print(whole_price)
print(type(whole_price))


# Converting an integer to a string
score = 100
score_text = str(score)

print(score_text)
print(type(score_text))


# Converting a string containing a number to an integer
number_text = "50"
number = int(number_text)

print(number)
print(type(number))


# Converting a string containing a decimal number to a float
price_text = "49.99"
price = float(price_text)

print(price)
print(type(price))


# Converting values to boolean
print(bool(1))
print(bool(0))

print(bool("Python"))
print(bool(""))


# Type casting can be useful when working with user input.
# input() always returns a string.

quantity_text = "5"
price_text = "20"

quantity = int(quantity_text)
price = float(price_text)

total = quantity * price

print(total)


# Be careful when converting incompatible values.
# int("Python") would cause a ValueError.

# Example:
# invalid_number = int("Python")
