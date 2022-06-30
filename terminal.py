a=1
b=int(input('enter no.'))
for i in range(b):
    for j in range(i):
        print(a,end='')
        a=a+1
    print()