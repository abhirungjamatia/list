list=[['g','f','g'],['i','s'],['b','e','s','t']]
list1=[]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        list1.append(list[i][j])
        j=j+1
    i=i+1  
print(list1)    
k=0
sum=""
while k<len(list1):
    sum=sum+list1[k]
    k=k+1
print(sum)    