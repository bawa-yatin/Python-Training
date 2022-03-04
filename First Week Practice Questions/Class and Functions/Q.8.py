# Python function that checks whether a passed string is palindrome or not.

class palindromeString:
    def check_string(self, str_val):
        if str_val.lower() == str_val.lower()[::-1]:
            print("Palindrome String!")
        else:
            print("Not a Palindrome String!")


str_val = "Radar"
ps = palindromeString()
ps.check_string(str_val)