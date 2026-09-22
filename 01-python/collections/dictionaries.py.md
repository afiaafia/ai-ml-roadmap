# Dictionaries in Python

# A dictionary stores data as key-value pairs.
student = {
    "name": "Alex",
    "score": 92,
    "passed": True
}

print(student)


# Accessing values using keys.
print(student["name"])
print(student["score"])


# Using get() to safely access a value.
print(student.get("name"))
print(student.get("grade"))


# Providing a default value with get().
print(student.get("grade", "Not available"))


# Adding a new key-value pair.
student["grade"] = "A"

print(student)


# Updating an existing value.
student["score"] = 95

print(student)


# Updating multiple values.
student.update({
    "score": 98,
    "passed": True
})

print(student)


# Removing an item using pop().
removed_value = student.pop("grade")

print(removed_value)
print(student)


# Checking whether a key exists.
print("name" in student)
print("age" in student)


# Getting all keys.
print(student.keys())


# Getting all values.
print(student.values())


# Getting key-value pairs.
print(student.items())


# Looping through a dictionary.
for key, value in student.items():
    print(key, value)


# Dictionary with a list as a value.
product = {
    "name": "Notebook",
    "price": 49.99,
    "tags": ["study", "office", "paper"]
}

print(product)
print(product["tags"])


# Nested dictionary.
inventory = {
    "product": {
        "name": "Keyboard",
        "price": 75
    },
    "stock": 20
}

print(inventory)
print(inventory["product"]["name"])
print(inventory["product"]["price"])
