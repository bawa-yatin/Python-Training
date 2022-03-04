# Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings

list_items = ['1221', 'banana', 'ababa', 'xyzqa']
count = 0
for item in list_items:
    if len(item) >= 2 and (item[0] == item[-1]):
        count += 1

print("No of elements having length 2 or more:", count)
