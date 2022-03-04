# Python function that accepts a string and calculate the number of upper case
# letters and lower case letters.

def upper_lower_count(str_val):
    upper_letter = lower_letter = 0

    for val in str_val:
        if val.isupper():

            upper_letter += 1
        elif val.islower():
            lower_letter += 1
        else:
            pass

    print(f"No of uppercase letters are {upper_letter}")
    print(f"No of lowercase letters are {lower_letter}")


str_val = input("Enter a string: ")
upper_lower_count(str_val)
