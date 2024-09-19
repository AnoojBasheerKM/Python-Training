def cumulative_lst(lists):
    new_lst = []
    sum = 0
    for i in range(0,len(lists)):
        sum += lists[i]
        new_lst.append(sum)
    return new_lst

lsts = [1,2,3,4,5]
