# Python program to sort a list of tuples and dictionaries using Lambda

# The sort() method sorts the list ascending by default.
# list.sort(reverse=True|False, key=myFunc)...key- A function to specify
# the sorting criteria


roll_list = [('Jack', 76), ('Emma', 78), ('Adam', 77), ('Simon', 79)]
mobile_list = [{'make': 'Nokia', 'model': '216', 'color': 'Black'},
               {'make': 'Samsung', 'model': '7', 'color': 'Blue'},
               {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

roll_list.sort(key=lambda a: a[1])
mobile_list.sort(key=lambda val: val['color'], reverse=True)

print(roll_list)
print(mobile_list)
