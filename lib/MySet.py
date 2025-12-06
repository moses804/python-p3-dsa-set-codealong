class MySet:
    def __init__(self, enumerable=[]):
        """Initialize the set with unique values from a list."""
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True

    def has(self, value):
        """Check if the value exists in the set."""
        return value in self.dictionary

    def add(self, value):
        """Add a value to the set."""
        self.dictionary[value] = True
        return self

    def delete(self, value):
        """Remove a value from the set."""
        self.dictionary.pop(value, None)
        return self

    def size(self):
        """Return the number of elements in the set."""
        return len(self.dictionary)

    def clear(self):
        """Remove all elements from the set."""
        self.dictionary.clear()
        return self

    def __str__(self):
        """Return a readable string representation of the set."""
        values = ", ".join(map(str, self.dictionary.keys()))
        return f"MySet: {{{values}}}"
