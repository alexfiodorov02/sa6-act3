numbers = [1, 2, 3, 4, 5]  # example list
n = 2  # example power

power_n = lambda x: x ** n
result = list(map(power_n, numbers))

print(result)