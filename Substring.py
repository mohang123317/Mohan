a=input()
b=list(a)
b.sort()
d=b.copy()
for i in range(1,len(b)):
    if(b[0]==b[i]):
        d.pop(i)
print(len(d))