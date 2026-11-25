def factorial(n):
    """Return the factorial of a non-negative integer n."""
    result = 1

    # Multiply result by every number from 2 to n
    for i in range(2, n + 1):
        result *= i

    return result


# Read the number from input
n = int(input())

# Print its factorial
print(factorial(n))