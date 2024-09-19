original_lists = [1, 2, 1, 3, 2, 5]
def find_unique(unique):
    unique = set(unique)
    result = list(unique)
    return result

print(find_unique(original_lists))