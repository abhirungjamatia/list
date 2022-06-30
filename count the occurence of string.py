list=['a','n','t','a','a','t','n','n','a','x','u','g','a','x','a']
b=97
c=122
d=[]
while b<=c:
    a=0
    sum=0
    e=[]
    while a<len(list):
        if list[a]==chr(b):
            f=list[a]
            sum=sum+1
        a=a+1
    if sum>0:
        e.append(f)
        e.append(sum)
        d.append(e)
    b=b+1
print(d)
