# Python program to check whether the given number is Armstrong number or not

num_1 = int(input("Enter a number: "))
temp = num_1
digits_sum = 0

while temp != 0:
    rem = temp % 10
    digits_sum += rem ** 3
    temp = temp // 10

if num_1 == digits_sum:
    print(num_1, "is an Armstrong Number")
else:
    print(num_1, "is not an Armstrong Number")
