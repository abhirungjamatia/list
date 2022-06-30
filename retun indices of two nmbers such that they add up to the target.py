list=[2,7,11,15]
target=9
i=0
num=[]
while i<len(list):
    a=i+1
    while a<len(list):
        if list[i]+list[a]==target:
            num.append(i)
            num.append(a)
        a=a+1
i=i+1
print(num)