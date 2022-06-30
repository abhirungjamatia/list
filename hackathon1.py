num=[2,7,11,15]
num1=[]
i=0
target=9
while i<len(num):
    a=i+1
    while a<len(num):
        if num[i]+num[a]==target:
            num1.append(i)
            num1.append(a)
        a=a+1
    i=i+1
print(num1)