def sort_strings(lst):
    return sorted(lst, key=lambda x: (len(x), x))

# Example usage:
strings = ["apple", "banana", "cherry", "kiwi", "mango"]
sorted_strings = sort_strings(strings)
print(sorted_strings)