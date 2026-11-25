import sys


def contains(big, small):
    """Return True if the list `small` appears inside `big`
    as a contiguous block of elements."""
    n, m = len(big), len(small)

    # Try every possible starting position in the big list
    for i in range(n - m + 1):
        # Compare a slice of the big list with the small list
        if big[i:i + m] == small:
            return True
    return False


# Read all non-empty lines and split them into numbers
lines = [line.split() for line in sys.stdin if line.strip()]

# Process the lines in pairs: (big list, small list)
for k in range(0, len(lines) - 1, 2):
    big = list(map(int, lines[k]))
    small = list(map(int, lines[k + 1]))
    print(contains(big, small))