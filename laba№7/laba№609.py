def add(a, b):
    """Return the sum of two integers."""
    return a + b


# Read two integers from a single line of input, separated by a space
a, b = map(int, input().split())

# Call the function and print the result
print(add(a, b))