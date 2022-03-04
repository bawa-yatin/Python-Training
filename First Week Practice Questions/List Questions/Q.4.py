# Python program find a list of integers with exactly two occurrences of
# nineteen and at least three occurrences of five.

list_items = [19, 19, 15, 5, 3, 5, 5, 2]

occur_times_19 = list_items.count(19)
occur_times_5 = list_items.count(5)

if occur_times_19 == 2 and occur_times_5 >= 3:
    print("Condition Satisfied")
else:
    print("Condition Not Satisfied")