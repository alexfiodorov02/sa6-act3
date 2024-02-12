# Define the two lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

# Use filter() to filter out the common elements
intersection = list(filter(lambda x: x in list1, list2))

print("The intersection of the two lists is:", intersection)