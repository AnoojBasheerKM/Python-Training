lst = [1, 2, 3, 4, 5, 6]

def cumulative_product(lstss):
    result = []
    product = 1
    for i in lstss:
        product = product*i
        result.append(product)
    return result

print(cumulative_product(lst))
