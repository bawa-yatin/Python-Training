# Python program to count the number of characters (character frequency) in a string.

str_1 = "Mississippi"
char_count = {}

for i in str_1:
    if i in char_count.keys():
        char_count[i] += 1
    else:
        char_count[i] = 1

print(char_count)