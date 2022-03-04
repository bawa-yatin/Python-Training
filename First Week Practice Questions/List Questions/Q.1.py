# Python Program to remove all occurrences of item 20 from the given list.

list_items = [5, 20, 15, 20, 25, 50, 20]

for val in list_items:
    if val == 20:
        list_items.remove(val)

print(list_items)