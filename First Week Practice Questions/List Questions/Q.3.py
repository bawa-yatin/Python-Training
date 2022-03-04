# Python program to get the most frequent element in a given list of numbers

list_items = [1, 2, 3, 1, 2, 3, 2, 1, 4, 3, 3]
ele_freq = {}
ele_key = ''

for val in list_items:
    count_element = list_items.count(val)
    ele_freq[val] = count_element

# First Way
for key, value in ele_freq.items():
    if value == max(ele_freq):
        ele_key = key

# Second Way- Shorter Way
print(f"Most frequent element in the given list is {max(ele_freq, key=ele_freq.get)}")

print(f"Most frequent element in the given list is {ele_key}")