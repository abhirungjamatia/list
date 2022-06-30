list=[1,2,3,3,4,5,3,2]
dup=[]
i=0
while i<len(list):
    j=i+1
    while j<len(list):
        if list[i]==list[j] and list[i] not in dup:
            dup.append(list[i])
        j=j+1
    i=i+1
print(dup)


         
