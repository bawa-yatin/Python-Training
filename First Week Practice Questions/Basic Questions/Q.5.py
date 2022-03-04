# Python program to get a single string from two given strings, separated by a space
# and swap the first two characters of each string.

str_1 = input("Enter the first string: ")
str_2 = input("Enter the second string: ")

new_str_1 = str_2[:2] + str_1[2:]
new_str_2 = str_1[:2] + str_2[2:]

print("Resultant String is", new_str_1, new_str_2)
