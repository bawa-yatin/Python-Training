# Python program to filter the height and width of students, which are stored
# in a dictionary.(Height >= 6ft and Weight >= 70kg)

dict_items = {'Cierra Vega': (6.2, 70),
              'Alden Cantrell': (5.9, 65),
              'Kierra Gentry': (6.0, 68),
              'Pierre Cox': (5.8, 66)}

new_dict = {}

for key, value in dict_items.items():
    if value[0] >= 6.0 and value[1] >= 70:
        new_dict[key] = (value[0], value[1])

print(new_dict)
