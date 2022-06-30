marks=[[74,68,84,50,40],[91,71,96,65,45],[49,69,93,65,55]]
i=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        k=marks[i][j]
        sum=sum+k
        j=j+1
    i=i+1
print(sum)