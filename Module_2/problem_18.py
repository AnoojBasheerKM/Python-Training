# write a program to print each line of a file in reverse order.


f = open('she.txt','r')
file = f.readlines()
# print(file)

def reserve(filename):
    for i in filename:
        print(i.strip()[::-1])



reserve(file)

