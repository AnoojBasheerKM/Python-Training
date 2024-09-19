# Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively



def head(file_path, n=10):
    with open(file_path, 'r') as file:
        for _ in range(n):
            line = file.readline()
            if not line:
                break
            print(line, end='')

def tail(file_path, n=10):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[-n:]:
            print(line, end='')

head('she.txt')

