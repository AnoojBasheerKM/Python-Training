# Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string


def grep(pattern, file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if pattern in line:
                print(line, end='')

grep('sure','she.txt')