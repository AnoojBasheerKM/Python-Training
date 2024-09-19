# Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions.


def square(x):
    return x * x
def custom_map(func, iterable):
    return [func(x) for x in iterable]

lst = []






for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end = " ")
    print()