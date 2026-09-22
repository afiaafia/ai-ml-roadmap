# Strings in Python

# A string is a sequence of characters.
message = "Hello, Python!"

print(message)
print(type(message))


# Strings can use single or double quotes.
single_quote = 'Python'
double_quote = "Programming"

print(single_quote)
print(double_quote)


# Strings can contain numbers and special characters.
course = "AI & Machine Learning"
version = "Python 3"

print(course)
print(version)


# String length
text = "Python"

print(len(text))


# Accessing characters using indexing
language = "Python"

print(language[0])
print(language[1])
print(language[-1])


# String slicing
word = "Programming"

print(word[0:6])
print(word[3:8])
print(word[:6])
print(word[6:])
print(word[:])


# Strings are immutable.
# You cannot directly change an individual character.
text = "Python"

# text[0] = "J"  # This would cause a TypeError.

print(text)


# Combining strings using the + operator
first_word = "Machine"
second_word = "Learning"

full_phrase = first_word + " " + second_word

print(full_phrase)


# Repeating strings using the * operator
separator = "-"
print(separator * 10)


# Checking whether text exists inside another string
sentence = "Python is useful for AI."

print("Python" in sentence)
print("Java" in sentence)


# Converting values to strings
number = 100
number_text = str(number)

print(number_text)
print(type(number_text))
