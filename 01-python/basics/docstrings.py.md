# Docstrings in Python

# A docstring is a string used to document a module, function, class,
# or method.

# Module-level docstring
"""
This module demonstrates how docstrings work in Python.
"""


# Function with a docstring
def calculate_total(price, quantity):
    """
    Calculate the total cost of a product.

    Args:
        price: The price of one item.
        quantity: The number of items.

    Returns:
        The total cost.
    """
    return price * quantity


total = calculate_total(25.50, 4)

print(total)


# Accessing a function's docstring
print(calculate_total.__doc__)


# Another example
def greet(message):
    """Display a greeting message."""
    print(message)


greet("Hello, Python!")


# Docstrings are different from regular comments.
# Comments explain code to developers.
# Docstrings document modules, functions, classes, and methods.
