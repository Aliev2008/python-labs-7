def int_to_str(n):
    """Convert an integer to a string."""
    return str(n)


# Read an integer from input
n = int(input())

# Call the function to get the string
s = int_to_str(n)

# Print with quotes using repr(), so the output looks like '8'
print(repr(s))