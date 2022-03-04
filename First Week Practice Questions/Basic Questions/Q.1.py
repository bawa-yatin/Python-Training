# Python program which accepts the radius of a circle from the user and compute the area

PI = 3.147  # Constant Variable

# Converting the string value into integer value using built-in int function
circle_radius = int(input("Enter the radius of your circle: "))
area = (PI * circle_radius ** 2)
print("Area of circle is ", area)
