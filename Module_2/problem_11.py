def duplicates(values):
    i = 0
    new_lst=[]
    for val in values:
        #print(val)
        if i == val:
            new_lst.append(i)
        i+=1
    return new_lst

lst = [1, 1, 3, 4, 5, 6, 7, 8]
print(duplicates(lst))
