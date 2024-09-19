

def create_2d_array(rows, cols):
    return [[None for i in range(cols)] for j in range(rows)]

rows = 3
cols = 4
array = create_2d_array(rows, cols)
print(array)