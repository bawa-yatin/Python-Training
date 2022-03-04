# Python program to convert given a dictionary to a list of tuples.

dict_items = {'Red': 1, 'Green': 3, 'White': 5, 'Black': 2, 'Pink': 4}

print("Original form of Items: ")
print(dict_items)

print("New form of Items: ")
print(list(dict_items.items()))