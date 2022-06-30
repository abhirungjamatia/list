num=[[8,3,4],[1,5,9],[6,7,2]]
sum=0
i=0
while i<len(num):
    a=num[i][0]
    sum=sum+a
    row=sum
    j=0
    sum1=0
    while j<len(num):
        b=num[j][0]
        sum1=sum1+b
        j=j+1
        col=sum1
    i=i+1
print(row)
print(col)
d=0
f=0
d1=0
while d<len(num):
    while f<len(num[d]):
        if d==f:
            c=num[d][f]
            d1+=c
            break
        f+=1
    d+=1
print(d1)
g=0
h=0
d2=0
while g<len(num):
    while h<len(num[g]):
        if g==h:
            c1=num[g][h]
            d2+=c1
            break
        h=h+1
    g=g+1
print(d2)
if row==col and d1==d2:
    print('it is magic square')
else:
    print('it is not a magic square')

    