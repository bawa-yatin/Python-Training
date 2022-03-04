# Python program to combine two dictionary adding values for common keys

dict_1 = {'x': 10, 'y': 25, 'z': 12, 'u': 18}
dict_2 = {'x': 30, 'y': 17, 'z': 51, 't': 8}
dict_3 = {}

dict_1_keys = dict_1.keys()
dict_2_keys = dict_2.keys()

for key_1 in dict_1_keys:
    for key_2 in dict_2_keys:
        if key_1 == key_2:
            dict_3[key_1] = dict_1[key_1] + dict_2[key_2]


print(dict_3)