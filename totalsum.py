n=[10,11,12,13,14,17,18,19]
i=0
b=[]
while i<len(n):
    c=[]
    j=i+1
    while j<len(n):
        a=n[i]+n[j]
        if a==30:
           c.append(n[i])
           c.append(n[j])
           b.append(c)
        j=j+1
    i=i+1
print(b)
