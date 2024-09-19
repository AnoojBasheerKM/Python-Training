from audioop import reverse


def reverses(lists):
    rev_lst = []
    for i in lists[::-1]:
        rev_lst.append(i)


    return rev_lst

lst = [2,3,4,5,6]

print(reverses(lst))