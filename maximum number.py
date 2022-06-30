list=[11,2,23,4]
maxval=list[0]
for i in range(0,len(list),1):
    if maxval<list[i]:
        maxval=list[i]
print(maxval)