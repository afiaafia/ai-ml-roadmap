# Lists in Python

# A list is an ordered and mutable collection.
numbers = [10, 20, 30, 40, 50]

print(numbers)


# Lists can contain different data types.
items = ["Notebook", 25, 49.99, True]

print(items)


# Accessing elements using indexing.
fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])
print(fruits[2])
print(fruits[-1])


# Slicing a list.
print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])


# Changing an element.
fruits[1] = "Grapes"

print(fruits)


# Adding an element using append().
fruits.append("Pineapple")

print(fruits)


# Adding an element at a specific position.
fruits.insert(1, "Banana")

print(fruits)


# Adding multiple elements using extend().
fruits.extend(["Peach", "Watermelon"])

print(fruits)


# Removing an element by value.
fruits.remove("Peach")

print(fruits)


# Removing an element by index using pop().
removed_fruit = fruits.pop()

print(removed_fruit)
print(fruits)


# Finding the number of elements.
print(len(fruits))


# Checking whether an element exists.
print("Mango" in fruits)
print("Kiwi" in fruits)


# Sorting a list.
scores = [85, 62, 91, 74, 68]

scores.sort()

print(scores)


# Reversing a list.
scores.reverse()

print(scores)


# Looping through a list.
for fruit in fruits:
    print(fruit)
