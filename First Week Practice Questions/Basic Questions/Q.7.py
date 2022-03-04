# Python program to generate and print a dictionary that contains a number
# (between 1 and n) in the form (x, x*x)

num_val = int(input("Enter a number: "))
dict_values = {}

for val in range(1, num_val+1):
    dict_values[val] = val ** 2

print("Values of new dictionary are:", dict_values)