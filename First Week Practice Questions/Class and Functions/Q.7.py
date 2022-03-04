# Python class which has two methods get_String and print_String. get_String accept a
# string from the user and print_String print the string in upper case.

class strInput():
    str_1 = ""

    def get_string(self):
        self.str_1 = input("Enter a string: ")

    def print_string(self):
        print(self.str_1.upper())


str_1 = strInput()
str_1.get_string()
str_1.print_string()
