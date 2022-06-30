integerX=[1,2,2,1]
i=1
y=[]
while i<=len(integerX):
    a=integerX[-i]
    y.append(a)
    i=i+1
print(y)
if y==integerX:
    print("true")
else:
    print("false")

