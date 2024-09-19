def product(num):
    result = 1
    for i in num:
        result *= i
    return result


lst = [1,3,5]

products = product(lst)
print(products)