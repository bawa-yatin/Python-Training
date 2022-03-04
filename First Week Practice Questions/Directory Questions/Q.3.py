# Python program to convert string values of a given dictionary, into
# integer/float datatypes

dict_items = [{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
new_dict = {}

for val in dict_items:
    for key, value in val.items():
        if isinstance(value, str):  # method to check to which particular data type class
            # the value belongs to.
            new_dict[key] = int(value)

print(new_dict)
