# Python class to find a pair of elements (indices of the two numbers) from a given
# array whose sum equals a specific target number.

class elementsPair:
    def find_pairs(self, list_items):
        pairs = list()
        global target_sum  # Using global variable inside a function with 'global' keyword
        target_sum = 70

        for i in range(len(list_items)):
            for j in range(i + 1, len(list_items)):
                if list_items[i] + list_items[j] == target_sum:
                    pairs.append((list_items[i], list_items[j]))

        print(list(set(pairs)))


list_items = [10, 20, 10, 40, 50, 60, 70]
target_sum = 60  # global variable not passed as a parameter inside the function

ep = elementsPair()
ep.find_pairs(list_items)
