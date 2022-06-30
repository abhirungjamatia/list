a=[]
for i in range(3):
    b=[]
    for j in range(3):
        j=int(input('enter number'))
        b.append(j)
    a.append(b)
print('matrix is')
for i in range(3):
    for j in range (3):
        print(a[i][j],end='')
    print()
sum1=0
sum2=0
for i in range(3):
    for j in range(3):
        if i==j:
            sum1+=a[i][j]
        if i+j==3-1:
            sum2+=a[i][j]
