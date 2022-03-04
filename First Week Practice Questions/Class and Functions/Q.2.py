# Create an outer function that will accept two parameters, a and b.
# Create an inner function inside an outer function that will calculate the
# addition of a and b.
# At last, an outer function will add 5 into addition and return it.

def outer_fun(a, b):
    def add_nos(a, b):
        return a + b

    add = add_nos(a, b)
    return add + 5


result = outer_fun(15, 17)
print(result)
