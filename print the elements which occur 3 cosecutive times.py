list=[9,2,3,2,2,4,8,6,5,5,5]
k=2
a=0
c=[]
while a<len(list):
    b=a+1
    sum=0
    while b<len(list):
        sum=sum+1
        if list[a]==list[b] and k<=sum:
            d=list[a]
            if d not in c:
                c.append(d)
        b=b+1
    a=a+1
print(c)