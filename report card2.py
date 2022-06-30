marks=[[54,65,90,75,50],[43,67,88,73,45],[56,67,70,55,48]]
i=0
year=1
while i<len(marks):
    j=0
    sum=0
    while j<len(marks[i]):
        k=marks[i][j]
        sum=sum+k
        j=j+1
    b=sum/len(marks[i])
    print('average of',year,'is',b)
    year+=1
    i=i+1


