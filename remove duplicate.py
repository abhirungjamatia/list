list=[1,2,3,1,3,4,5,6]
a=[]
i=0
while i<len(list):
    if list[i] not in a:
        a.append(list[i])
    i=i+1
print(a)