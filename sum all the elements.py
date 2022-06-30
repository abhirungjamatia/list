list=[[1,2,3],[5,2,10],[20,5,6]]
list1=[]
i=0
while i<len(list):
    j=0
    while j<len(list):
        list1.append(list[i][j])
        j=j+1
    i=i+1
print(list1)
k=0
sum=0
while k<len(list1):
    sum=sum+list1[k]
    k=k+1
print(sum)
    