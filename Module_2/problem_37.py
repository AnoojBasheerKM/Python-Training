
def valuesort(d):
    return [d[key] for key in sorted(d.keys())]

# Example usage:
result = valuesort({'x': 1, 'y': 2, 'a': 3})
print(result)