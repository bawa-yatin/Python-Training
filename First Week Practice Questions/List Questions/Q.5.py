# Python program to remove specific words from a given list using lambda

list_items = []

for i in range(5):
    list_items.append(input("Enter any element: "))

words_remove = []

for i in range(2):
    words_remove.append(input("Enter element you want to remove: "))

final_list = list(filter(lambda word: word not in words_remove, list_items))
print(final_list)
