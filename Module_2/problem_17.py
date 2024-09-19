f = open('she.txt','r')
text = f.readlines()
for i in range(len(text)-1,-1,-1):
    print(text[i])
f.close()