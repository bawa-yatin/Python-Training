# Given a list of numbers, write a program to turn every item of a list into its square.

num_list = [1, 2, 3, 4, 5, 6, 7]
new_list = []

for val in num_list:
    new_list.append(val ** 2)

print(new_list)