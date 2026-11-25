import sys


def reverse_words(text):
    """Reverse every word in the text, keeping the word order."""
    # Split by spaces, reverse each word with a slice, join back
    return ' '.join(word[::-1] for word in text.split(' '))


# Process every input line
for line in sys.stdin:
    # Remove the trailing newline before processing
    print(reverse_words(line.rstrip('\n')))