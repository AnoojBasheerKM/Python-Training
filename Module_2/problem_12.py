def grouping(lst,size):
    result_lst = []
    for i in range(0,len(lst),size):
        # print(i)
        grp = lst[i:i+size]
        # print(grp)
        result_lst.append(grp)
    return result_lst
lst_1 = [1,2,3,4,5,6,7,8,9]
print(grouping(lst_1,3))
