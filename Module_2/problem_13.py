lst = ['python', 'pearl', 'java', 'c', 'haskell', 'ruby']

def lensort(lst):
    return sorted(lst, key=len)
sorted_list = lensort(lst)
print(sorted_list)