# Function to compute sum of digits
sum_of_digits = lambda num: sum(int(digit) for digit in str(num))

# Test the function
number = 12345
print(f"The sum of the digits of {number} is {sum_of_digits(number)}")