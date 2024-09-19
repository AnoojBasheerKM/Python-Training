

def enumerates(lst):
    return [(i, item) for i, item in enumerate(lst)]

my_list = ['a', 'b', 'c', 'd']

result = enumerates(my_list)
print(result)


