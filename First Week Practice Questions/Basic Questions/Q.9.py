# Python program to find numbers between 100 and 400 (both included) where each digit
# of a number is an even number.

even_items = []
for val in range(100, 401):
    s = str(val)

    if (int(s[0]) % 2 == 0) and (int(s[1]) % 2 == 0) and (int(s[2]) % 2 == 0):
        even_items.append(s)

print(",".join(even_items))
