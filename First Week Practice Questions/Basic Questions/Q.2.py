# Python program to swap two variables without using Third Variable

num_val_1 = int(input("Enter the first number: "))
num_val_2 = int(input("Enter the second number: "))

print("\nBefore Swapping")
print("First Number: ", num_val_1, "\nSecond Number: ", num_val_2)

num_val_1 = num_val_1 + num_val_2
num_val_2 = num_val_1 - num_val_2
num_val_1 = num_val_1 - num_val_2

print("\nAfter Swapping")
print("First Number: ", num_val_1, "\nSecond Number: ", num_val_2)