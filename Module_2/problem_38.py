def invertdict(d):
    return {v: k for k, v in d.items()}

d = {'x': 1, 'y': 2, 'z': 3}
inverted = invertdict(d)
print(inverted)