a = 'HelWo, World!'
s=[]
for i in range(len(a)):
    if a[i] == "W":
        s.append(i+1)
print(s)