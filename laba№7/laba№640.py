import sys


def sum_three(a, b, c):
    """Return the sum of three integers.
    If any two values are equal, return 0."""
    # Check all possible pairs for equality
    if a == b or a == c or b == c:
        return 0
    return a + b + c


# Process every input line (each line holds three integers)
for line in sys.stdin:
    parts = line.split()

    # Skip empty or malformed lines
    if len(parts) != 3:
        continue

    a, b, c = map(int, parts)
    print(sum_three(a, b, c))