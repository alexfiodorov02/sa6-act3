def find_max(numbers, compare):
    max_num = numbers[0]
    for num in numbers:
        max_num = compare(max_num, num)
    return max_num

# Define the lambda function
compare = lambda x, y: x if x > y else y

# Test the function
numbers = [1, 2, 3, 4, 5]
print(find_max(numbers, compare))  # Output: 5